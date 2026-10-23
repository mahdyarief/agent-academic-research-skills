---
name: thesis-docx-writing
description: 'Convert thesis markdown draft to clean docx.'
version: 0.1.0
author: Mahdy, Hermes Agent
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [thesis, docx, markdown, writing, naskah]
    related_skills: [docx, thesis-proposal, dosen-ready-academic-prose]
---

# Penulisan Tesis: Markdown -> DOCX

Mahdy menulis naskah tesis dalam markdown (sumber tunggal, murah direvisi), lalu
di-render ke .docx untuk diserahkan ke dosen. Tool: `tools/md2docx.py` di folder
tesis.

## Why

Alur `docx_create.py` (spec JSON) memecah draft hard-wrap jadi satu paragraf per
baris, sehingga tiap baris dapat enter sendiri di Word. Spec JSON juga merepotkan:
3 file per revisi, mudah tidak sinkron dengan .md.

## How to apply

1. Draft bab sebagai `.md` dengan hard-wrap ~80 karakter, paragraf dipisah baris
   kosong. Heading: `# Judul Bab` (h1) dan `## Subbab` (h2).
2. Sisipkan gambar dengan sintaks `![Caption Gambar 1.1](../04-diagram/nama.png)`
   tepat setelah paragraf yang relevan.
3. Semua catatan penulisan ditaruh di bawah separator `---`; tool membuangnya
   otomatis sehingga tidak masuk naskah.
4. Render: `python tools/md2docx.py draft.md draft.docx --img-mm 160`
5. Verifikasi: `docx_read.py draft.docx --text` (kunci JSON `body`, bukan
   `paragraphs`) lalu cek string kunci; `docx_validate.py draft.docx` harus ok.

## Pitfalls

- Path gambar relatif dipecahkan terhadap folder file .md, bukan working
  directory. Jangan lupa flag `--img-mm` (lebar mm) agar gambar tidak melebihi
  lebar area cetak A4.
- Baris `# ...` di sumber .md harus dibuang di parser, kalau tidak ikut jadi
  paragraf teks dan judul bab Terduplikasi. Buang di parser, bukan manual.
- Nomor list memakai style bawaan Word (`List Number`); daftar terpisah bisa
  melanjutkan penomoran. Kalau presisi dibutuhkan, tulis manual.
- Template Telkom resmi mungkin berbeda dari default tool (Times New Roman 12,
  spasi 1.5, A4, margin 30/30/35/30) dan perlu penyesuaian satu kali.
- `docx_read.py` keluarannya JSON dengan key `body`. Salah key bikin verifikasi
  string lolos padahal isinya kosong.
- Di kernel `execute_code`, python berbeda dari python terminal: `python-docx`
  harus dipasang di kernel via `subprocess`+`sys.executable` kalau tool
  dijalankan dari sana.

## Alur Google Docs (opsional, untuk mengedit dengan UI nyaman)

- Google Docs TIDAK mengedit file .md di disk. Edit di sana, lalu
  `File > Download > Markdown (.md)`, simpan ke Downloads, lalu
  `python tools/tarik_gdocs.py ~/Downloads/bab1.md bab1-pendahuluan-draft2`.
- Sumber tunggal tetap .md di folder tesis. Kalau .docx jadi sumber, render ulang
  dari .md akan menimpa edit-an di docx.
- `md2docx.py` sudah membersihkan penanda inline Google Docs (`**tebal**`,
  `*miring*`, backtick) lewat `bersihkan_teks()`.
- Quirk ekspor Google Docs: daftar bernomor kadang jadi bullet atau teks biasa,
  bukan `1.`. Kalau muncul, tambahkan penanganan di parser `md2docx.py`.

## Aturan isi naskah

- Bahasa Indonesia akademik natural, tanpa em dash dan en dash.
- Frasa kebaruan: "belum ditemukan pada literatur yang ditinjau".
- Angka selalu dengan penyebut, bukan persen telanjang.
- Jembatan keledai dan mnemonic hanya di chat, tidak di naskah.
- Hindari jargon yang sendiri penulis tak paham: "korpus" diganti "data penelitian".
- Angka di naskah wajib dihitung ulang dari sumber (bukan mengikuti catatan lama):
  penghitungan ulang membongkar kesalahan yang sudah masuk draft. Contoh nyata:
  rentang pending tertulis 6-14 persen, ternyata 6,59-15,66 persen pada lima studi
  yang punya angka persen eksplisit (dari enam studi total). Cek ulang sebelum
  render final, dan perbaiki juga catatan di diagram.

## Aturan diagram untuk naskah cetak

- Lebar desain HTML ~800 px bila gambar mau dicetak 16 cm. Desain lebih lebar
  (misal 1180 px) membuat huruf kecil di kertas.
- Font CSS minimal 13 px; target >= 8 pt saat dicetak. Ukur: dpi efektif =
  px / (lebar_cm / 2,54); tinggi huruf di kertas = device_px / px_per_cm.
- Render Chrome headless dengan --force-device-scale-factor=3.
- Potong baris kosong bawah (cari baris terakhir yang masih punya piksel konten),
  lalu cek tepi kanan tidak ada piksel gelap (overflow).
- Kalau rasio lebar/tinggi tidak hemat tempat, percependek teks kotak, bukan
  mengecilkan font.
