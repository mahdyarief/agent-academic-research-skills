# Catatan Atribusi

Paket ini **kurasi**, bukan karya tunggal. Saya memilih, menata, membersihkan, dan
beberapa di antaranya mengubah skill yang sudah ada di profil Hermes Agent saya. Siapa
penulis aslinya tercantum di bawah, dan nama di frontmatter setiap skill adalah penulis
aslinya, bukan diganti atas nama saya.

Alasan atribusi dipertahankan: menghapus nama penulis asli lalu menggantinya dengan nama
penyunting adalah klaim kepengarangan yang tidak benar. Mengurasi bukan menulis.

## Cakupan

Paket ini sengaja **tidak** memuat skill yang terikat langsung ke satu data penelitian
tertentu. Dua skill seperti itu sengaja dikeluarkan: satu untuk verifikasi angka terhadap
data penelitian, satu untuk penentuan posisi klaim saat pembelaan. Keduanya berguna untuk
satu proyek tertentu, tapi tidak bisa dipakai orang lain tanpa data dan konteks yang sama,
dan tetap tinggal di profil pemiliknya.

Yang tersisa adalah prosedur umum: merumuskan masalah, memetakan literatur, memverifikasi
sumber, menulis, meninjau, dan mengirim artikel. Bisa dipakai untuk tesis maupun paper.

## Asal usul per kelompok

- **`Mahdy Arief (mahdyarief)`** tujuh skill. Dua di antaranya adaptasi dari snapshot MIT
  `xngg1021/hermes-academic-skills` commit `439ce4a`: `academic-source-verification` dan
  `literature-analysis`, diterjemahkan ke Bahasa Indonesia, frontmatter disesuaikan
  standar Hermes, dan dua bug di kode verifikasinya diperbaiki. Lima lainnya ditulis dari
  nol: `socratic-research-dialogue`, `socratic-reading-probe`, `claim-evidence-map`,
  `manuscript-review-simulation`, dan `reviewer-response-coach`.
- **`Mahdy, Hermes Agent`** delapan skill. Saya yang menulis atau memodifikasi isinya,
  dengan Hermes Agent sebagai alat bantu penyusunan.
- **`Hermes Agent`** empat skill. Skill bawaan Hermes Agent yang tidak saya ubah
  substansinya, hanya dikurasi ke dalam paket ini.
- **`Hermes Agent + Teknium`** satu skill, `grounded-citations`. Hak cipta tetap milik
  penulis aslinya.

## Daftar lengkap

| lapis | skill | penulis asli | versi |
|---|---|---|---|
| 01-riset | `arxiv` | Hermes Agent | 1.0.0 |
| 01-riset | `design-science-research-positioning` | Mahdy, Hermes Agent | 0.1.0 |
| 01-riset | `dsr-self-audit` | Mahdy, Hermes Agent | 0.1.0 |
| 01-riset | `journal-scouting` | Mahdy, Hermes Agent | 0.2.0 |
| 01-riset | `literature-mapping` | Hermes Agent | 0.1.0 |
| 01-riset | `research-problem-and-gap` | Mahdy, Hermes Agent | 0.1.0 |
| 01-riset | `socratic-reading-probe` | Mahdy Arief (mahdyarief) | 1.0.0 |
| 01-riset | `socratic-research-dialogue` | Mahdy Arief (mahdyarief) | 1.0.0 |
| 02-verifikasi | `academic-source-verification` | Mahdy Arief (mahdyarief) | 1.0.0 |
| 02-verifikasi | `claim-evidence-map` | Mahdy Arief (mahdyarief) | 1.0.0 |
| 02-verifikasi | `grounded-citations` | Hermes Agent + Teknium | 1.2.0 |
| 02-verifikasi | `literature-analysis` | Mahdy Arief (mahdyarief) | 1.0.0 |
| 03-penulisan | `manuscript-review-simulation` | Mahdy Arief (mahdyarief) | 1.0.0 |
| 03-penulisan | `paper-writing` | Mahdy, Hermes Agent | 0.1.0 |
| 03-penulisan | `reviewer-response-coach` | Mahdy Arief (mahdyarief) | 1.0.0 |
| 03-penulisan | `thesis-docx-writing` | Mahdy, Hermes Agent | 0.1.0 |
| 03-penulisan | `thesis-proposal` | Mahdy, Hermes Agent | 0.1.0 |
| 03-penulisan | `thesis-supervisor-outreach` | Hermes Agent | 0.1.0 |
| 04-publikasi | `indo-journal-scouting` | Mahdy, Hermes Agent | 0.1.0 |
| 04-publikasi | `survey-instrument-design` | Hermes Agent | 1.0.0 |

## Yang saya ubah saat mengurasi

1. Menyusun skill ke dalam empat lapis: riset, verifikasi, penulisan, publikasi.
2. Mengganti path mesin lokal menjadi placeholder generik `<HERMES_HOME>` dan
   `<WORKSPACE>`. Tiga skill terdampak: `journal-scouting`, `thesis-proposal`, dan
   `indo-journal-scouting`.
3. Mengeluarkan berkas `openalex-keys.json` dari paket, karena berkas itu memuat kunci
   API milik pemakai mesin dan tidak boleh ikut dibagikan. Polanya ditambahkan ke
   `.gitignore`.
4. Membuang dua skill yang terikat ke satu data penelitian tertentu.
5. Menambah lima skill baru yang ditulis dari nol, tanpa menyalin teks dari repo lain.

## Ide yang diserap, teks yang tidak

Tiga penambahan terakhir berangkat dari ide yang dibaca di repo publik lain. Teksnya
ditulis ulang sepenuhnya dalam Bahasa Indonesia, dengan struktur dan contoh yang berbeda.
Tidak ada satu berkas pun yang disalin lalu didistribusikan ulang di sini.

- *Pemeriksaan integritas bibliografi* di `academic-source-verification`: gagasan memisahkan
  kelas bukti, mencatat status pemeriksaan secara terpisah dari temuannya, dan menghitung
  asal-usul sumber yang independen. Tidak ada nomor sinyal, istilah, atau tabel yang
  disalin.
- *`manuscript-review-simulation`*: gagasan dimensi review dan kategori keputusan editorial.
  Kriteria penilaian di sini disusun ulang dengan label dan ambang sendiri.
- *`reviewer-response-coach`*: gagasan memisahkan pekerjaan menyusun jawaban reviewer dari
  pekerjaan mengaudit jawaban yang sudah ada.
- *Bagian PRISMA* di skill SLR milik pemilik profil (tidak dipublikasikan di paket ini):
  prinsip konsistensi angka pelaporan. PRISMA sendiri adalah standar publik, bukan milik
  repo mana pun.

Sumber inspirasi: `Imbad0202/academic-research-skills`, berlisensi CC BY-NC 4.0. Karena
lisensi itu melarang pemakaian komersial dan paket ini MIT, tidak ada materi aslinya yang
disalin.

## Lisensi

Semua skill berlisensi MIT pada frontmatter-nya. Paket disusun dengan lisensi MIT. Hak
cipta tiap skill tetap milik penulis yang tercantum, dan notis ini memenuhi kewajiban
atribusi MIT untuk redistribusi.
