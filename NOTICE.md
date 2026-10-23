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
satu proyek tertentu, tapi tidak bisa dipakai orang lain tanpa data dan konteks yang sama.

Yang tersisa adalah prosedur umum: merumuskan masalah, memetakan literatur, memverifikasi
sumber, menulis, dan mengirim artikel. Bisa dipakai untuk tesis maupun paper.

## Asal usul per kelompok

- **`Mahdy Arief (mahdyarief)`** tiga skill. Dua di antaranya adaptasi dari snapshot MIT
  `xngg1021/hermes-academic-skills` commit `439ce4a`: `academic-source-verification` dan
  `literature-analysis`, diterjemahkan ke Bahasa Indonesia, frontmatter disesuaikan
  standar Hermes, dan dua bug di kode verifikasinya diperbaiki. Satu lagi,
  `socratic-research-dialogue`, ditulis dari nol.
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
| 01-riset | `socratic-research-dialogue` | Mahdy Arief (mahdyarief) | 1.0.0 |
| 02-verifikasi | `academic-source-verification` | Mahdy Arief (mahdyarief) | 1.0.0 |
| 02-verifikasi | `grounded-citations` | Hermes Agent + Teknium | 1.2.0 |
| 02-verifikasi | `literature-analysis` | Mahdy Arief (mahdyarief) | 1.0.0 |
| 03-penulisan | `paper-writing` | Mahdy, Hermes Agent | 0.1.0 |
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

Tidak ada materi berlisensi CC BY-NC dari repo lain di paket ini.

## Lisensi

Semua skill berlisensi MIT pada frontmatter-nya. Paket disusun dengan lisensi MIT. Hak
cipta tiap skill tetap milik penulis yang tercantum, dan notis ini memenuhi kewajiban
atribusi MIT untuk redistribusi.
