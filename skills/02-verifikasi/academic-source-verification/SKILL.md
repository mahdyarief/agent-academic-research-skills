---
name: academic-source-verification
description: Use when verifying a citation, retraction, or OA full text.
version: 1.0.0
author: Mahdy Arief (mahdyarief)
license: MIT
platforms: [linux, macos, windows]
adapted_from: xngg1021/academic-research-kernel @ 439ce4a (MIT, Junfu Shi)
required_environment_variables:
  - name: OPENALEX_API_KEY
    prompt: "OpenAlex API key (opsional, bisa pakai akses anonim)"
    help: "Ambil key gratis di akun OpenAlex. Jangan pernah menuliskan key ke dalam skill atau ke chat."
    required_for: "Permintaan OpenAlex terautentikasi; query anonim tetap tersedia."
  - name: UNPAYWALL_EMAIL
    prompt: "Email kontak Unpaywall (opsional, lewati bila tidak dipakai)"
    help: "Isi email Anda yang sebenarnya. Tanpa email, pengecekan Unpaywall dilewati."
    required_for: "Pencarian full text OA di Unpaywall saja."
metadata:
  hermes:
    tags: [research, citations, open-access, crossref, openalex, semantic-scholar, unpaywall, retraction, integrity]
    related_skills: [arxiv, pdf, grounded-citations, literature-analysis, claim-evidence-map]
---

# Verifikasi Sumber Akademik

Memastikan satu karya ilmiah benar-benar ada, metadata cocok, tidak ditarik, dan full text yang didapat memang karya yang dimaksud. Skill ini melengkapi `arxiv`: `arxiv` menemukan paper, skill ini memeriksa paper dan mengambil full text.

Prinsip dasarnya sederhana: sebelum mengutip satu simpulan ilmiah, periksa dulu identitas literaturnya, status retraksi, konteks counted citation, dan kalimat aslinya. Jangan mengandalkan ingatan atau kutipan tangan kedua.

## Kapan dipakai

- Diminta memeriksa apakah sebuah sitasi benar-benar ada, atau membandingkan jumlah sitasi antar basis data.
- Argumen atau model memakai rujukan, dan klaim judul, penulis, tahun, jurnal, atau jumlah sitasi harus dipastikan.
- Perlu mengunduh full text open access dan memastikan unduhannya bukan paper yang salah.
- Perlu memeriksa apakah sebuah karya sudah ditarik (retraction) atau pernah dikoreksi.
- Perlu memeriksa teks asli karya klasik domain publik, misalnya Ebbinghaus 1885 atau Miller 1956.

Jangan pakai untuk: pencarian atau penemuan paper baru (gunakan `arxiv`), dan OCR atau parsing isi PDF yang sudah diunduh (gunakan `pdf`).

## Prasyarat

Permintaan jaringan memakai Python stdlib urllib. Ekstraksi PDF butuh pymupdf yang diperiksa terpisah. OpenAlex bisa ditanyai anonim dalam skala kecil; key gratis disarankan. Unpaywall mewajibkan email kontak yang benar. Semua layanan punya kuota, dan akses gratis tidak berarti tanpa batas:

- OpenAlex: metadata, topik, tanda OA, tanda retraksi. Anonim sekitar 0,10 dolar per hari, key gratis sekitar 1 dolar per hari. Lewat anggaran atau 100 req/s menghasilkan 429.
- Crossref: jumlah sitasi versi Crossref, plus catatan retraksi dan koreksi. DOI yang tidak terdaftar di Crossref bisa 404, misalnya DOI arXiv yang terdaftar lewat DataCite.
- Semantic Scholar: angka sitasi dari basis data lain. Kuota anonim bersama mudah kena 429; key mulai dari 1 req/s.
- Unpaywall: lokasi full text OA lewat `is_oa` dan `best_oa_location`. Wajib membawa parameter email.

## Empat pemeriksaan

### 1. Cocokkan tiga basis data

Bandingkan DOI, judul, penulis, dan versi, lalu catat perbedaannya. Basis data bisa berbagi data penerbit atau Crossref, jadi kesepakatan antar ketiganya bukan tiga bukti independen. Jumlah sitasi tidak dipakai untuk menilai identitas karya.

- OpenAlex: `https://api.openalex.org/works/https://doi.org/{DOI}` dengan field `cited_by_count`, `publication_year`, `authorships`, `primary_location.source.display_name`, `open_access.oa_status`, `oa_url`.
- Crossref: `https://api.crossref.org/works/{DOI}` dengan field `message.is-referenced-by-count`.
- Semantic Scholar: `https://api.semanticscholar.org/graph/v1/paper/DOI:{DOI}?fields=title,authors,year,venue,citationCount,influentialCitationCount,openAccessPdf`, atau `arXiv:{id}`.

Selalu kirim `User-Agent`, lebih sopan bila berisi mailto, karena sebagian endpoint menolak tanpa itu. Angka sitasi antar basis data pasti berbeda karena cakupan indeksnya berbeda. Selisih besar bisa berasal dari penggabungan versi atau cakupan, jadi jelaskan, jangan langsung menolak identitas paper.

Pakai `execute_code` untuk menanyai beberapa DOI sekaligus dan mencetak tabel perbandingan. Ikuti kuota masing-masing layanan; jeda tetap tidak menjamin bebas dari 429 pada kuota bersama.

### 2. Periksa retraksi dan koreksi

Sejak Januari 2025 Crossref memasukkan sinyal dari Retraction Watch ke REST API, kolaborasinya sendiri dimulai sekitar September 2023. Catat DOI asli, DOI notifikasi, jenisnya, sumbernya, dan waktu pengecekan. Field `update-to` biasanya berada pada catatan notifikasi dan menunjuk ke objek yang diperbarui. Jangan menyebut catatan notifikasi sebagai paper yang ditarik. Field `message.type` adalah jenis terbitan, bukan jenis retraksi.

Langkahnya:

1. Ambil metadata DOI asli. Awalan judul `RETRACTED:` atau `WITHDRAWN:` hanya tanda yang harus diverifikasi, bukan kesimpulan.
2. Cari arah balik lewat `https://api.crossref.org/works?filter=updates:<DOI>&rows=100`, lalu periksa apakah `update-to[].DOI` memang menunjuk ke DOI target. Bila lebih dari satu halaman, lanjutkan dengan aturan cursor milik Crossref dan catat bahwa hasilnya terpotong.
3. Pisahkan `retraction`, `withdrawal`, `correction`, dan `expression-of-concern`. Catat sumbernya, penerbit atau Retraction Watch. Jangan menggabungkan sinyal yang berbeda menjadi satu label retraksi.
4. Di OpenAlex, `is_retracted=true` berarti basis data mencatat sinyal retraksi, sedangkan false tidak menutup kemungkinan ada yang terlewat. Untuk arXiv, periksa halaman abs dan riwayat versinya. Bila ragu, cek notifikasi penerbit atau catatan asli Retraction Watch.

Fungsi berikut hanya menyaring sinyal pembaruan yang terhubung ke DOI target, dan inputnya harus berasal dari hasil query Crossref yang berhasil:

```python
def update_signals(target_doi, records):
    target = target_doi.lower().removeprefix('https://doi.org/')
    signals = []
    for record in records:
        for update in record.get('update-to') or []:
            updated_doi = str(update.get('DOI') or '').lower().removeprefix('https://doi.org/')
            if updated_doi == target:
                signals.append({'type': update.get('type'), 'source': update.get('source'),
                                'record_doi': record.get('DOI'), 'target_doi': updated_doi})
    return signals

fixture = {'DOI': '10.1234/notice', 'update-to': [
    {'DOI': '10.1234/original', 'type': 'retraction', 'source': 'publisher'}]}
assert update_signals('10.1234/original', [fixture])[0]['type'] == 'retraction'
assert update_signals('10.1234/notice', [fixture]) == []
assert update_signals('10.1234/original', [{'DOI': '10.1234/original'}]) == []
```

Bila tidak ada sinyal, laporkan apa adanya: "pada sumber data yang diperiksa tidak ditemukan catatan retraksi atau penarikan", lengkap dengan sumber, waktu, dan apa saja yang gagal atau belum diperiksa. Request yang gagal tidak sama dengan tidak ditemukannya catatan. Bila ada sinyal, sebutkan tingkat buktinya, apakah tanda di basis data atau notifikasi penerbit. Paper yang ditarik tetap bisa menjadi objek kajian tentang peristiwa retraksi, tetapi tidak boleh dipakai sebagai dasar simpulan tanpa penjelasan.

Rujukan resmi: [integrasi Retraction Watch di Crossref](https://www.crossref.org/blog/retraction-watch-retractions-now-in-the-crossref-api/) dan [filter query pembaruan](https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-filters/).

### 3. Cari full text open access

Unpaywall hanya salah satu jalur pencarian OA. Cakupan dan jeda pembaruannya berbeda dengan sumber lain, jadi jangan dianggap selalu yang terbaik. Potongan kode berikut mengandalkan fungsi `get()` dari bagian Verifikasi dan variabel `doi`:

```python
import os
from urllib.parse import quote, urlencode
email = os.environ['UNPAYWALL_EMAIL']
r = get('https://api.unpaywall.org/v2/' + quote(doi, safe='') + '?' + urlencode({'email': email}))
if r.get("is_oa"):
    loc = r.get("best_oa_location")  # url_for_pdf / url; versi published, accepted, atau submitted
else:
    loc = None  # layanan ini tidak menemukan versi OA, bukan bukti versi OA tidak ada
```

Urutan pencarian: `best_oa_location` Unpaywall, lalu `oa_url` OpenAlex, lalu `openAccessPdf.url` Semantic Scholar, terakhir archive.org untuk buku domain publik. Jangan berulang kali memaksa halaman di balik paywall yang membalas 403.

### 4. Unduh dan cocokkan isinya

- arXiv (green OA): `https://arxiv.org/pdf/{id}`. Bisa gagal karena pembatasan laju, penarikan, atau jaringan.
- Buku atau monograf domain publik, misalnya Ebbinghaus 1885, lewat archive.org. Cari identifier dengan `https://archive.org/advancedsearch.php?q=<judul>&fl[]=identifier,title,year,mediatype&rows=3&output=json`, lalu periksa `https://archive.org/metadata/{identifier}` untuk memilih nama file PDF yang sebenarnya. Jangan mengasumsikan nama file sama dengan identifier, dan cek status aksesnya.

Untuk memeriksa isi PDF:

```python
import pymupdf
doc = pymupdf.open(path)
print(" ".join(doc[0].get_text().split())[:400])  # teks halaman pertama, untuk mencocokkan judul dan penulis
print(doc.page_count)
doc.close()
```

Simpan unduhan di folder tetap, misalnya `Path("~/papers").expanduser()` yang dibuat dengan `mkdir(parents=True, exist_ok=True)`, dan pastikan path-nya aman untuk UTF-8. Laporkan path absolut, ukuran byte, dan jumlah halaman.

### 5. Periksa integritas bibliografi

Empat pemeriksaan di atas menjawab "apakah sumber ini nyata". Bagian ini menjawab
pertanyaan lain: "apakah bibliografi naskah ini bisa dipercaya". Beda dua hal itu penting,
karena sitasi yang lolos pemeriksaan identitas tetap bisa jadi bagian dari pola yang
bermasalah.

#### Tiga kelas bukti, jangan dicampur

Setiap sinyal yang kamu laporkan harus jelas masuk kelas apa. Mencampurnya membuat hasil
pemeriksaan terdengar lebih pasti daripada kenyataannya.

- *Fakta pengamat*: apa yang dikembalikan sebuah layanan pada waktu tertentu. Contoh:
  OpenAlex membalas `is_retracted` bernilai false pada 23 Oktober 2026. Itu bukan bukti
  bahwa paper tidak pernah ditarik, hanya catatan apa yang dikatakan basis data.
- *Petunjuk heuristik*: hasil aturan atau pola yang dicocokkan, misalnya deteksi sitasi
  yang semuanya terbit dalam rentang dua tahun dengan pola penulis berulang. Ini sinyal
  untuk diperiksa, bukan temuan.
- *Atestasi proses*: catatan bahwa sebuah pemeriksaan sudah dijalankan. Ini paling rendah
  nilainya, karena tidak menyatakan apa hasilnya. "Sudah dicek" bukan "aman".

Status dan temuan juga dua hal terpisah. Pemeriksaan yang berstatus tidak dijalankan,
tidak diketahui, atau gagal sebagian *tidak boleh* dilaporkan sebagai bersih. Kalau
sebuah layanan menolak atau tidak bisa dihubungi, hasilnya unresolved, bukan lolos.

#### Sembilan sinyal yang layak diperiksa

- *Satu*, sitasi yang DOI-nya tidak resolve ke record apa pun. Ini sinyal paling kuat,
  tapi juga paling sering salah karena DOI preprint didaftarkan di DataCite, bukan Crossref.
  Periksa kedua jalur sebelum menyimpulkan.
- *Dua*, metadata yang berubah antar versi: nama penulis berbeda, tahun berbeda, atau
  judul bergeser makna. Catat versi mana yang kamu pakai.
- *Tiga*, penulis yang tidak punya jejak lain di bidang itu. Bukan bukti pemalsuan, tapi
  alasan untuk membuka halaman penulis di penerbit, bukan di agregator.
- *Empat*, jurnal yang mengaku terindeks tapi tidak muncul di direktori resmi yang
  diklaimnya. Cek langsung di direktori, jangan di situs jurnal.
- *Satu artikel di banyak jurnal berbeda* dengan isi hampir sama. Ini pola jurnal predator.
- *Enam*, rentang sitasi yang terlalu rapat ke satu penulis, terutama bila penulis itu
  juga penulis naskahnya.
- *Tujuh*, klaim yang dipasangkan pada sitasi tapi kalimat pendukungnya tidak ada di
  paper yang dikutip. Ini yang paling sering lolos, dan paling merusak.
- *Delapan*, retraksi yang hanya muncul di penerbit, tidak di basis data. Karena itu
  pemeriksaan retraksi di bagian 2 harus dibaca bersama halaman paper aslinya.
- *Sembilan*, daftar pustaka yang memuat karya yang tidak pernah dikutip di badan teks,
  atau sebaliknya. Ini sinyal bahwa daftar pustaka disusun terpisah dari argumen.

#### Satu bukti, bukan tiga

Tiga berita yang mengutip satu siaran pers adalah *satu* bukti, bukan tiga. Begitu juga
tiga basis data yang menarik data dari Crossref yang sama.

- Kesesuaian antar sumber hanya bermakna kalau asal-usulnya independen.
- Kalau semua sumber berasal dari satu asal, katakan itu dan turunkan keyakinan, jangan
  biarkan pengulangan terbaca sebagai replikasi.
- Untuk angka juga begitu: kalau dua sumber menyebut angka yang sama, periksa apakah
  sumber kedua mengutip yang pertama.

#### Cara melaporkan

Untuk setiap sinyal, tulis empat hal: sinyal apa, kelas buktinya apa, status pemeriksaan
(bersih, dicurigai, atau belum bisa diputuskan), dan apa yang belum diperiksa. Yang
berstatus belum bisa diputuskan tetap harus muncul di laporan, jangan disembunyikan
karena terlihat seperti pekerjaan yang belum selesai.

Bedakan tegas antara "tidak ditemukan sinyal" dan "tidak diperiksa". Kalimat "tidak
ditemukan" hanya boleh dipakai kalau pemeriksaannya benar-benar berjalan dan berhasil.

## Prosedur

1. Tetapkan DOI, arXiv ID, atau judul. Paper jurnal pakai DOI, preprint arXiv pakai arXiv ID.
2. Jalankan `execute_code` untuk query OpenAlex dan Crossref, tambahkan Semantic Scholar bila tersedia, lalu cetak tabel judul, penulis, tahun, jurnal, dan sitasi dari tiap basis data.
3. Periksa hubungan pembaruan dua arah, tanda di OpenAlex, serta status di penerbit atau arXiv. Klasifikasikan, dan jangan menyebut catatan notifikasi sebagai objek yang ditarik.
4. Simpulkan identitas. Bila DOI dan metadata cocok, laporkan bahwa identitas sudah terverifikasi. Bila tidak cocok, catat selisihnya dan laporkan apa adanya.
5. Unduh full text OA bila tersedia, lalu cocokkan halaman pertamanya dengan pymupdf.
6. Bila terhalang paywall atau 403, laporkan pemeriksaan yang sudah berhasil dan status "akses full text terbatas". Kode 403 juga bisa berarti anti-scraping atau kebijakan akses, jadi jangan dipakai untuk menyimpulkan status paywall atau retraksi, dan jangan mencoba berulang.
7. Jalankan pemeriksaan integritas bibliografi bila yang diminta bukan satu sitasi, tapi satu daftar pustaka atau satu naskah. Laporkan per sinyal, bukan satu angka kesimpulan.

## Jebakan

1. Jumlah sitasi selalu punya konteks sumber. Penggabungan preprint dengan versi terbit, catatan duplikat, dan cakupan basis data memengaruhi angka. Sebutkan sumber dan tanggal query, dan jangan menyebut angka satu basis data sebagai dampak sebenarnya atau batas bawah yang ketat.
2. DOI data arXiv di Crossref dan OpenAlex bisa 404 atau terlambat. DOI `10.48550/arXiv.<id>` terdaftar lewat DataCite sehingga Crossref sering 404, sementara OpenAlex kadang terlambat mengindeksnya. Dalam kasus ini panggil API resmi arXiv (`http://export.arxiv.org/api/query?id_list=<id>` atau `search_query=ti:<judul>`) untuk memastikan judul, abstrak, riwayat versi, dan status penarikan.
3. Judul karya klasik mudah bertabrakan dengan artikel tinjauan yang terbit belakangan oleh penulis yang sama. Pencarian dengan judul pendek dan umum, misalnya "Working Memory", mudah mengenai artikel ulasan dengan judul identik. Untuk karya pendiri, batasi tahun terbit lewat Crossref `filter=from-pub-date:YYYY-01-01,until-pub-date:YYYY-12-31` dan periksa urutan penulisnya.
4. Semantic Scholar tanpa key sangat mudah kena 429. Beri jeda minimal 1,1 detik, mundur dan ulangi bila gagal. Bila 429 terus muncul, kembali ke OpenAlex dan Crossref, lalu nyatakan keterbatasan itu dengan jujur.
5. `update-to` tidak kosong bukan berarti retraksi. Periksa arah pembaruan, DOI target, dan `update.type`. Koreksi dan expression of concern dicatat terpisah.
6. PDF penerbit yang berbayar menghasilkan 403 saat diunduh skrip. `oa_status: "bronze"` di OpenAlex hanya berarti dapat dibaca gratis di situs penerbit, bukan berarti bisa diunduh otomatis. Contohnya pdfdirect Wiley yang membalas 403. Setelah 403, laporkan akses terbatas dan jangan mengulang.
7. Unduhan berhasil bukan berarti isinya benar. Ekstrak teks halaman pertama untuk mencocokkan judul dan penulis, agar tidak salah mengunduh file bernama mirip.
8. Parameter email Unpaywall diperiksa ketat. Pakai email kontak Anda yang sebenarnya. Layanan bisa membalas 422 untuk email yang kosong atau contoh. Saat `is_oa=false`, `best_oa_location` bernilai null, jadi periksa dulu sebelum mengambilnya.
9. Jangan mengubah status pemeriksaan yang gagal menjadi "bersih". Layanan yang menolak, timeout, atau belum dikonfigurasi menghasilkan status belum bisa diputuskan. Laporan yang mengubahnya jadi bersih adalah laporan palsu, walaupun niatnya baik.
10. Jangan menyimpulkan naskah memakai sitasi karangan hanya dari satu sinyal. Pola bermasalah butuh minimal dua sinyal independen, dan tetap dilaporkan sebagai kecurigaan, bukan vonis.

Bahasa keluaran: ikuti bahasa yang dipakai pengguna. Judul dan kutipan paper tetap dalam bahasa aslinya; saat terjemahan pertama kali muncul, sertakan teks aslinya.

## Verifikasi

```python
import json, os, time
from urllib.request import Request, urlopen
from urllib.parse import urlsplit, urlencode, quote
from urllib.error import HTTPError

def get(url):
    headers = {'User-Agent': 'agent-academic-research-skills/1.0 (mailto:mahdyarief@users.noreply.github.com)'}
    if urlsplit(url).netloc == 'api.openalex.org' and os.environ.get('OPENALEX_API_KEY'):
        headers['Authorization'] = 'Bearer ' + os.environ['OPENALEX_API_KEY']
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers=headers), timeout=20) as response:
                return json.load(response)
        except HTTPError as error:
            if error.code not in {429, 500, 502, 503, 504} or attempt == 2:
                raise
            # Mundur terbatas. Blokir beranggaran panjang dilaporkan pemanggil, bukan diulang tanpa henti.
            retry = error.headers.get('Retry-After', '')
            delay = float(retry) if retry.isdigit() else 2**attempt
            if delay > 10:
                raise
            time.sleep(delay)

doi = '10.1038/nature14539'
oa = get('https://api.openalex.org/works/https://doi.org/' + quote(doi, safe=''))
assert oa.get('doi', '').lower() == 'https://doi.org/' + doi
assert 'deep learning' in oa['title'].lower()
assert isinstance(oa.get('is_retracted'), bool)
cr = get('https://api.crossref.org/works/' + quote(doi, safe=''))['message']
assert cr['DOI'].lower() == doi and 'deep learning' in ' '.join(cr['title']).lower()
original = '10.1177/1758835920922055'
updates = get('https://api.crossref.org/works?' + urlencode({'filter': 'updates:' + original, 'rows': 5}))['message']
assert any(u.get('DOI', '').lower() == original and u.get('type') == 'retraction'
           for item in updates['items'] for u in item.get('update-to', []))
print('OpenAlex/Crossref identity + reverse retraction lookup passed')
email = os.environ.get('UNPAYWALL_EMAIL')
if email:
    up = get('https://api.unpaywall.org/v2/' + quote(doi, safe='') + '?' + urlencode({'email': email}))
    assert isinstance(up.get('is_oa'), bool) and up['doi'].lower() == doi
    print('Unpaywall passed')
else:
    print('SKIP Unpaywall: UNPAYWALL_EMAIL belum dikonfigurasi; tidak ada hasil yang disimpulkan')
```

Tanpa key, query OpenAlex berjalan lewat jalur anonim. Jalur dengan key hanya berjalan saat `OPENALEX_API_KEY` dikonfigurasi. Layanan yang belum dikonfigurasi harus dilaporkan SKIP, bukan dianggap lulus. Semantic Scholar diperiksa terpisah sesuai tugas dan kuota yang tersedia.
