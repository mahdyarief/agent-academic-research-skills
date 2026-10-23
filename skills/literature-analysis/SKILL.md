---
name: literature-analysis
description: Use when analyzing a paper or concept across literature.
version: 1.0.0
author: Mahdy Arief (mahdyarief)
license: MIT
platforms: [linux, macos, windows]
adapted_from: xngg1021/academic-research-kernel @ 439ce4a (MIT, Junfu Shi)
required_environment_variables:
  - name: OPENALEX_API_KEY
    prompt: "OpenAlex API key (opsional, bisa pakai akses anonim)"
    help: "Ambil key gratis di akun OpenAlex. Jangan menuliskan key ke dalam skill atau ke chat."
    required_for: "Permintaan OpenAlex terautentikasi; query anonim tetap tersedia."
metadata:
  hermes:
    tags: [research, literature, similarity, plagiarism, peer-review, fallacy, openalex]
    related_skills: [academic-source-verification, arxiv, grounded-citations]
---

# Analisis Literatur

Menganalisis satu paper atau satu konsep dari banyak sudut: cari paper mirip, bandingkan kemiripan teks, cari kontradiksi dan bukti lawan, profil penulis, simulasi reviewer, dan penandaan kesalahan logika. Skill ini melengkapi `academic-source-verification`: yang itu memeriksa "apakah paper ini nyata, apakah ditarik, full text-nya di mana", skill ini mengerjakan "analisis penelitian di sekitarnya".

Prinsip kerjanya: setiap simpulan menyebut sumber datanya, yaitu API mana, field mana, kutipan mana. Yang bisa diotomasi diotomasi. Yang tidak bisa diotomasi, seperti penilaian reviewer dan penentuan kesalahan logika, dikerjakan model dengan template dan tetap menyertakan kutipan yang bisa diperiksa ulang.

## Kapan dipakai

- Pengguna memberi satu konsep atau pertanyaan penelitian dan minta paper dengan tema serupa.
- Pengguna memberi tautan atau PDF dan minta "cari yang mirip", "cek kemiripan", atau "sudah ada yang mengerjakan ini".
- Pengguna minta bukti lawan: "ada paper yang membantah simpulan ini?".
- Pengguna minta simulasi review atau penandaan kesalahan logika pada satu artikel.
- Pengguna memberi nama penulis dan minta profil akademiknya.
- Pengguna minta matriks tinjauan dari banyak paper, rekomendasi jurnal dari topik, atau entri BibTeX.
- Pengguna minta pembacaan dwibahasa, analisis celah penelitian, atau pencarian kode dan dataset resmi untuk reproduksi.

## Prasyarat dan saluran akses

Ada tiga lapis saluran. Lapis gratis dipakai secara default. Lapis berbayar memakai key milik pengguna sendiri, disimpan di variabel lingkungan, dan tidak boleh ditulis ke dalam berkas skill.

Lapis gratis: OpenAlex (anonim sekitar 0,10 dolar per hari, key gratis sekitar 1 dolar per hari, lewat anggaran atau 100 req/s membalas 429), Crossref (tanpa key), Unpaywall (wajib parameter email), arXiv, Europe PMC di `api.europepmc.org` (tanpa key), PubMed E-utilities (tanpa key, bidang biomedis), dan DOAJ. Untuk literatur Indonesia, Garuda dan SINTA diakses lewat halaman web tanpa API publik; skill `indo-journal-scouting` menanganinya.

Lapis akun opsional, syarat aksesnya harus diperiksa dulu: Semantic Scholar (kuota terpisah mulai 1 req/s, ketersediaan field `contexts` tidak dijamin walau punya key), Scite (untuk membaca posisi sitasi), Dimensions versi gratis (hanya web, tanpa API), dan CiNii untuk literatur Jepang.

Lapis berbayar: Scopus API, Web of Science API, Dimensions API, dan Scite Pro. Bila MCP `journal_scout` tersedia, utamakan itu untuk Scopus karena sudah menangani autentikasi.

Semua permintaan membawa `User-Agent` berisi mailto. Pakai domain `https://api.openalex.org/works/...` untuk mesin, karena ID entitas seperti `https://openalex.org/W...` bukan alamat API.

### Konvensi query OpenAlex

Semua URL di bawah adalah template; parameter sebenarnya dienkode dengan `urllib.parse.urlencode`. Untuk key gratis, kirim `Authorization: Bearer <OPENALEX_API_KEY>`.

Paginasi dimulai dari `cursor=*`, lalu `meta.next_cursor` dibawa kembali apa adanya sampai bernilai null, hasil kosong, atau batas anggaran yang sudah ditetapkan. Bila berhenti karena batas, tulis "sampel sebagian", jangan menyebutnya seluruh sitasi. Perbandingan jumlah dan tren diseragamkan dengan `corpus=core`; bila memakai perluasan, semua query harus memakai `corpus=all`. Sertakan juga jendela tanggal, jenis terbitan, dan waktu query.

Field `Concepts` sudah tidak dipelihara dan bukan jalur utama. Analisis data lama dengan field ini harus diberi label legacy. Bibliographic coupling yang sebenarnya memerlukan irisan atau gabungan `referenced_works` dua paper, sedangkan co-citation memerlukan hitungan paper yang mengutip keduanya. `related_works` tidak bisa menggantikan keduanya.

Rujukan resmi: [autentikasi dan kuota](https://help.openalex.org/api/authentication/), [ringkasan query](https://help.openalex.org/api/llm-quick-reference/), [semantik field](https://help.openalex.org/data/works/attributes/), [paginasi](https://help.openalex.org/api/paging/).

## Alur kerja A: mencari paper mirip

Input datang dalam tiga bentuk, dan semuanya dinormalkan dulu menjadi DOI atau teks konsep.

1. Teks konsep, misalnya "hallucination suppression in retrieval augmented generation", dicari dengan `https://api.openalex.org/works?search=<konsep>&per_page=10&sort=relevance_score:desc&select=title,publication_year,cited_by_count,doi`.
2. Tautan atau DOI paper. Ambil paper aslinya, lalu tiga lapis kesamaan: `related_works` (rekomendasi algoritmik berbasis topik bersama, bukan coupling sitasi), irisan ID `topics` (field `primary_topic` menandai topik utama, `score` adalah skor klasifikasi, bukan probabilitas kemiripan), dan pencarian ulang memakai kata kunci judul.
3. Berkas PDF. Ekstrak judul dan abstrak halaman pertama dengan pymupdf, lalu pakai sebagai teks pencarian.

Format keluaran: satu baris per kandidat berisi judul, tahun, jumlah sitasi, DOI, dan dasar kemiripannya, yaitu pencarian teks, rekomendasi algoritmik, atau irisan topik. Urutkan berdasarkan kekuatan dasar kemiripan. Untuk hasil pencarian konsep, urutkan berdasarkan `relevance_score`.

## Alur kerja B: membandingkan kemiripan teks

Batas jujurnya dinyatakan lebih dulu. Uji kemiripan seluruh web memerlukan layanan komersial seperti iThenticate atau Turnitin. Yang dikerjakan di sini adalah pembandingan tingkat kalimat antara satu paper target dan kumpulan paper kandidat yang berhasil diunduh, untuk menemukan tumpang tindih harfiah atau hampir harfiah dengan kumpulan itu. Tidak ada klaim cakupan seluruh web.

Langkahnya:

1. Kumpulkan 10 sampai 20 kandidat dari alur kerja A, dan unduh full text OA sebanyak mungkin.
2. Ekstrak teks target: `doc = pymupdf.open(path); text = " ".join(p.get_text() for p in doc)`.
3. Pecah menjadi kalimat, buang spasi berlebih, nomor halaman, dan bagian daftar rujukan, ubah ke huruf kecil, buang kalimat di bawah 20 karakter.
4. Lakukan hal sama untuk setiap kandidat.
5. Bandingkan: kalimat identik, dan kalimat sangat mirip bila `difflib.SequenceMatcher.ratio() > 0.85`.
6. Laporkan jumlah pasangan kalimat yang bertumpang tindih, proporsinya terhadap total kalimat target, teks kalimat yang bertumpang tindih, dan letaknya di paragraf mana.

```python
from difflib import SequenceMatcher
def overlap_ratio(a, b):
    return SequenceMatcher(None, a, b).ratio()
```

Ambang rujukan: satu kandidat dengan tumpang tindih di atas 5 persen, atau tiga kalimat berurutan identik, ditandai kuning; di atas 15 persen ditandai merah. Sertakan versi dan tanggal terbit, bagian yang dikutip dengan tanda kutip, serta teks metode yang memang umum. Ambang ini hanya penanda awal, karena urutan waktu dan tumpang tindih kalimat tidak membuktikan plagiarisme. Setiap kalimat target dihitung sekali agar proporsi tidak melebihi 100 persen.

## Alur kerja C: mencari kontradiksi dan bukti lawan

Dua lapis, dijalankan berurutan.

Lapis pertama, penyaringan kumpulan sitasi, adalah jalur utama. Ambil paper yang mengutip target sebagai kumpulan kandidat, dengan batas halaman yang ditetapkan dan dilaporkan:

`https://api.openalex.org/works?filter=cites:<WID>&per_page=25&select=id,title,abstract_inverted_index,publication_year,doi`

Abstrak dicari dengan tiga tingkat cadangan, karena tingkat ketiadaannya berbeda antar bidang dan periode dan tidak bisa diperkirakan dari beberapa sampel. Tingkat pertama rekonstruksi `abstract_inverted_index`. Bila kosong, tingkat kedua ambil `message.abstract` dari Crossref. Bila masih kosong, tandai "bukti tidak cukup" dan coba full text OA lewat `academic-source-verification`. Judul hanya dipakai untuk penyaringan kandidat, tidak untuk menyimpulkan dukungan, kritik, atau kegagalan replikasi. Setelah itu model menilai satu per satu sifat sitasinya dan hanya menyimpan yang bersifat kritik atau gagal direplikasi, lengkap dengan dasar penilaiannya.

Lapis kedua, pencarian kata negasi, bersifat pembantu. Pakai pola seperti `search=fail to replicate <topik>`, `search=challenges <topik> findings`, dan `search=<topik> irreproducible`. Hasilnya cenderung berupa tinjauan, jadi perlu disaring manual.

Keluaran: daftar paper pembantah, masing-masing dengan jenis bantahan (kritik metode, kontradiksi simpulan, gagal direplikasi, bantahan batas berlaku) dan kalimat buktinya. Sertakan pernyataan jujur bahwa recall dibatasi ketersediaan abstrak dan kritik di balik paywall bisa terlewat. Bila punya key Semantic Scholar, tambahkan `citations?fields=contexts` untuk memperluas cakupan.

## Alur kerja D: profil penulis

Ambil `author.id` dari `authorships`, misalnya `A5023888391`, lalu:

1. Profil: `https://api.openalex.org/authors/<A-ID>` memberi `display_name`, `works_count`, `cited_by_count`, `h_index` di dalam `summary_stats`, dan `last_known_institutions`.
2. Karya utama: `https://api.openalex.org/works?filter=authorships.author.id:<A-ID>&sort=cited_by_count:desc&per_page=10&select=title,cited_by_count,publication_year`.
3. Jaringan kolaborasi, opsional: filter yang sama dengan `select=authorships`, lalu hitung frekuensi rekan penulis.

## Alur kerja E: simulasi review

Template dan rubrik penilaian ada di `references/peer-review-template.md`. Poin utamanya: nyatakan lebih dulu bahwa ini simulasi dan tidak menggantikan peer review sebenarnya; beri tanggapan bersusun untuk tiap bagian dengan kolom kelebihan, masalah, dan saran; akhiri dengan skor 1 sampai 5 dan tiga alasan penentu; setiap kritik wajib menunjuk paragraf dan mengutip kalimatnya.

## Alur kerja F: menandai kesalahan logika

Daftar periksa ada di `references/fallacy-checklist.md`. Format penandaan: letak paragraf, jenis kesalahan, alasan kesalahan itu berlaku, dan saran perbaikan. Sertakan distribusi jenisnya. Tandai hanya yang pasti; yang meragukan masuk bagian "belum pasti" dan tidak dipaksakan.

## Alur kerja G: matriks tinjauan

Mampatkan 20 sampai 50 paper menjadi tabel lima kolom berisi metode, sampel, simpulan utama, dan keterbatasan, lalu kelompokkan berdasarkan tema. Rincian ada di `references/review-matrix.md`.

## Alur kerja H: rekomendasi jurnal

Saring works berdasarkan ID topik, lalu agregasi `primary_location.source.id` untuk mendapatkan kandidat jurnal beserta alasan kecocokannya. Peringkat dan impact factor tidak ada di data ini, jadi harus dinyatakan perlu diperiksa terpisah. Rincian ada di `references/journal-matching.md`. Untuk jurnal Indonesia, lanjutkan dengan `indo-journal-scouting`.

## Alur kerja I: ekspor BibTeX

Buat entri BibTeX dari metadata OpenAlex, termasuk saran gaya untuk literatur Indonesia. Rincian ada di `references/bibtex-guide.md`.

## Alur kerja J: pembacaan dwibahasa

Ringkas per bagian dalam bahasa target, sertakan kalimat kunci aslinya, dan susun daftar istilah yang konsisten. Bahasa target default mengikuti pengguna. Rincian ada di `references/bilingual-reading.md`.

## Alur kerja K: analisis celah penelitian

Bandingkan kepadatan paper dan tren waktu antar kombinasi topik, lalu laporkan area yang sepi. Kata yang boleh dipakai hanya "kepadatan rendah"; jangan menyimpulkan "ada celah". Rincian ada di `references/research-gap.md`. Untuk membangun argumen celah yang lebih kuat, sambungkan dengan skill `research-problem-and-gap`.

## Alur kerja L: bantuan reproduksi

Cari kode dan dataset resmi. API lama Papers with Code tidak boleh dijadikan sandaran; periksa status layanannya dulu, lalu pakai pencarian GitHub, Hugging Face, dan pencarian web. Rincian ada di `references/reproduction.md`.

## Prosedur

1. Kenali bentuk input: teks konsep, tautan, PDF, nama penulis, atau instruksi langsung seperti review, kesalahan logika, dan pembandingan kemiripan.
2. Normalkan: tautan menjadi DOI lewat `https://api.openalex.org/works/https://doi.org/{DOI}`, PDF menjadi judul dan abstrak.
3. Pilih alur kerja A sampai L. Untuk tugas gabungan, jalankan A lalu B lalu C.
4. Setiap simpulan membawa sumber data dan kalimat buktinya. Untuk penilaian yang tidak bisa diotomasi, sertakan letak teks aslinya.
5. Laporkan dalam teks biasa yang bisa diperiksa baris per baris, dan pisahkan "fakta data" dari "penilaian model".
6. Bahasa keluaran mengikuti bahasa pengguna. Judul dan kutipan paper tetap dalam bahasa aslinya, dan terjemahan pertama disertai teks aslinya.

## Jebakan

1. Format permintaan OpenAlex. Domain API adalah `api.openalex.org`. ID entitas seperti `https://openalex.org/W...` hanya berlaku sebagai ID; bila dijadikan alamat permintaan hasilnya 403. Nilai filter memakai ekor ID, misalnya `cites:W2919115771` atau `author.id:A5023888391`.
2. Ketersediaan Semantic Scholar bergantung kuota dan konfigurasi. Bila 429 berlanjut, laporkan sebagai tidak terperiksa, bukan hasil kosong. Key tidak menjamin field `contexts` ada.
3. Batas jujur pembandingan kemiripan: cakupannya hanya kandidat yang full text-nya berhasil diunduh. Cakupan itu wajib ditulis di laporan.
4. Recall bukti lawan terbatas. `abstract_inverted_index` sering kosong, dan `abstract` di Crossref juga bisa kosong; paper Nature 2015 pernah terukur kosong. Bila abstrak tidak ada, ambil full text atau tandai bukti tidak cukup. Judul hanya untuk kandidat. Kalimat yang benar adalah "pada N sitasi yang dapat diakses, tidak ditemukan sitasi kritis", bukan "tidak ada bukti lawan".
5. Kemiripan bukan plagiarisme. `related_works` adalah kedekatan akademik yang wajar dan bukan sinyal plagiarisme. Alur kerja B hanya memberi bukti tumpang tindih teks; simpulan plagiarisme memerlukan konteks, sitasi, dan bukti versi.
6. Review dan penandaan kesalahan logika adalah penilaian model, bukan fakta data. Pisahkan kolom "data API" dan "penilaian model", dan biarkan pengguna memeriksa ulang.
7. Kesopanan laju. OpenAlex punya anggaran harian dan batas 100 req/s. Batasi jumlah halaman, mundur secara terbatas saat 429, dan jangan mengulang endpoint yang sama dalam satu sesi.

## Verifikasi

```python
import json, os, time
from urllib.request import Request, urlopen
from urllib.parse import urlsplit, urlencode
from urllib.error import HTTPError

HAS_KEY = bool(os.environ.get('OPENALEX_API_KEY'))

def get(url):
    headers = {'User-Agent': 'agent-academic-research-skills/1.0 (mailto:mahdyarief@users.noreply.github.com)'}
    if urlsplit(url).netloc == 'api.openalex.org' and HAS_KEY:
        headers['Authorization'] = 'Bearer ' + os.environ['OPENALEX_API_KEY']
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers=headers), timeout=20) as response:
                return json.load(response)
        except HTTPError as error:
            # 401 disini bukan salah kredensial: OpenAlex menolak paginasi cursor
            # di halaman kedua ke atas bila tidak ada API key.
            if error.code not in {429, 500, 502, 503, 504} or attempt == 2:
                raise
            retry = error.headers.get('Retry-After', '')
            delay = float(retry) if retry.isdigit() else 2**attempt
            if delay > 10:
                raise
            time.sleep(delay)

wid = 'W2741809807'
w = get('https://api.openalex.org/works/' + wid + '?' + urlencode({
    'select': 'id,title,doi,topics,primary_topic,related_works,authorships,is_retracted'}))
assert w['id'].endswith('/' + wid) and w['authorships'] and w['topics']
assert all(t['id'].split('/')[-1].startswith('T') for t in w['topics'])
assert isinstance(w['related_works'], list)

topic_ids = [t['id'].split('/')[-1] for t in w['topics'][:2]]
both = get('https://api.openalex.org/works?' + urlencode({
    'filter': ','.join('topics.id:' + t for t in topic_ids), 'per_page': 1,
    'select': 'id,topics', 'corpus': 'core'}))
assert both['results'] and all(
    set(topic_ids) <= {t['id'].split('/')[-1] for t in r['topics']} for r in both['results'])

groups = get('https://api.openalex.org/works?' + urlencode({
    'filter': 'topics.id:' + topic_ids[0], 'group_by': 'primary_location.source.id',
    'per_page': 5, 'corpus': 'core'}))
assert groups['group_by'] and all(isinstance(g['count'], int) for g in groups['group_by'])

search = get('https://api.openalex.org/works?' + urlencode({
    'search': 'attention is all you need', 'per_page': 1,
    'select': 'id,title', 'sort': 'relevance_score:desc'}))
assert search['results'] and search['results'][0]['title']

author_id = w['authorships'][0]['author']['id'].split('/')[-1]
author_works = get('https://api.openalex.org/works?' + urlencode({
    'filter': 'authorships.author.id:' + author_id, 'per_page': 1, 'select': 'id,authorships'}))
assert author_works['results'] and any(
    a['author']['id'].endswith('/' + author_id) for a in author_works['results'][0]['authorships'])
print('work, topic AND, source grouping, search, author filter passed')

# Paginasi cursor: halaman pertama boleh anonim, halaman kedua butuh key gratis.
query = {'filter': 'topics.id:' + topic_ids[0], 'per_page': 1,
         'cursor': '*', 'select': 'id,topics', 'corpus': 'core'}
first = get('https://api.openalex.org/works?' + urlencode(query))
assert first['results'] and first['meta']['next_cursor']
if HAS_KEY:
    query['cursor'] = first['meta']['next_cursor']
    second = get('https://api.openalex.org/works?' + urlencode(query))
    assert second['results'] and first['results'][0]['id'] != second['results'][0]['id']
    print('cursor pagination page 2 passed')
else:
    print('SKIP cursor page 2: OPENALEX_API_KEY belum dikonfigurasi; '
          'OpenAlex mewajibkan key gratis untuk halaman kedua ke atas. '
          'Halaman pertama terbukti berjalan.')
```


Bagian yang membutuhkan Semantic Scholar diperiksa terpisah karena endpoint-nya rapuh dan sering membalas 429 atau 404 untuk DOI tertentu.
