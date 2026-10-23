# Catatan Asal Usul

Paket skill ini adalah adaptasi untuk Hermes Agent, bukan karya orisinal dari nol.

Sumber asal: `xngg1021/hermes-academic-skills`, yang kemudian berganti nama menjadi
`xngg1021/academic-research-kernel`.

Snapshot yang diambil: commit `439ce4a29d6d2d9137308d7f9f045863e9f0c5b3`, yaitu commit
terakhir sebelum proyek itu mengganti lisensinya dari MIT ke Source Lineage License 1.0.
Snapshot itu diverifikasi berlisensi MIT, dengan copyright Junfu Shi (xngg1021).

Yang berubah dari sumber asli:

- Prosa dan dokumen pendukung diterjemahkan ke Bahasa Indonesia. Istilah teknis tetap
  dalam Bahasa Inggris karena itu yang dipakai saat mencari di mesin pencari dan paper.
- Frontmatter disesuaikan dengan standar Hermes: deskripsi maksimal 60 karakter dan
  berawalan "Use when", penambahan field `adapted_from`, serta penyesuaian nama variabel
  lingkungan.
- Konteks Mandarin (CNKI, Wanfang, biblatex-gb7714-2015) diganti konteks literatur
  Indonesia (Garuda, SINTA, biblatex-apa), dengan gb7714 tetap disebut bila jurnal meminta.
- Dua bug di kode verifikasi sumber asli diperbaiki. Rinciannya ada di bawah.
- Referensi ke skill yang tidak ada di paket ini diberi jalur keluar yang jelas.

## Bug yang diperbaiki saat adaptasi

1. Paginasi cursor OpenAlex pada `literature-analysis` gagal dengan kode 401. Setelah
   dilacak, penyebabnya bukan kesalahan kredensial: OpenAlex mewajibkan API key gratis
   untuk halaman kedua dan seterusnya. Kode asli langsung crash karena menganggapnya
   galat fatal. Versi ini mendeteksi kondisi itu dan melaporkan SKIP secara eksplisit
   bila key belum dikonfigurasi, lalu menguji paginasi penuh bila key tersedia.
2. Gaya BibTeX untuk literatur berbahasa Indonesia pada sumber asli mengarah ke
   biblatex-gb7714-2015, yang ditujukan untuk literatur berbahasa Mandarin. Versi ini
   memakai biblatex-apa sebagai default dan menyebut gb7714 hanya sebagai opsi bila
   jurnal memintanya.

Semua kode verifikasi di paket ini dijalankan sungguhan sebelum dirilis. Yang tidak bisa
diuji karena layanan atau kredensial belum tersedia dilaporkan sebagai SKIP, bukan
diklaim lulus.
