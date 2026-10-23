# agent-academic-research-skills

Paket skill akademik untuk Hermes Agent. Berisi tiga skill yang dipakai saat mengerjakan
penelitian: memverifikasi sumber, menganalisis literatur, dan menuntun berpikir lewat
dialog socratic. Dua skill pertama bekerja lewat API publik yang gratis, dengan
penanganan eksplisit saat kuota atau kredensial belum tersedia.

## Isi paket

- `skills/academic-source-verification` memastikan sebuah sitasi benar-benar ada,
  metadata-nya cocok, tidak ditarik, dan full text yang diunduh adalah karya yang dimaksud.
- `skills/literature-analysis` menganalisis area sekitar satu paper: paper mirip,
  kemiripan teks, kontradiksi dan bukti lawan, profil penulis, simulasi review,
  kesalahan logika, matriks tinjauan, rekomendasi jurnal, BibTeX, pembacaan dwibahasa,
  analisis kepadatan topik, dan pencarian kode untuk reproduksi.
- `skills/socratic-research-dialogue` menuntun pengguna berpikir sendiri lewat lima lapis
  pertanyaan (T-A-B-K-A: Tujuan, Asumsi, Bukti, Konsekuensi, Alternatif), dengan jangkar
  fakta ke skill lain agar tidak mengarang. Ditulis dari nol, bukan turunan repo lain.

## Pemasangan

Salin folder skill ke direktori skill profil Hermes:

```
cp -r skills/academic-source-verification "$HERMES_PROFILE/skills/research/"
cp -r skills/literature-analysis "$HERMES_PROFILE/skills/research/"
cp -r skills/socratic-research-dialogue "$HERMES_PROFILE/skills/research/"
```

Pada Windows dengan profil `scholar-assist`, direktori tujuannya
`D:/ai-agent/.hermes/profiles/scholar-assist/skills/research/`.

Hermes memuat isi skill ke dalam konteks saat skill dipanggil, jadi skill di paket ini
sebaiknya dipakai satu per satu sesuai kebutuhan, bukan dimuat bersamaan tanpa alasan.

## Variabel lingkungan opsional

Tidak ada yang wajib. Tanpa variabel di bawah, skill tetap berjalan dengan kemampuan
terbatas dan melaporkan apa yang tidak bisa diperiksa.

- `OPENALEX_API_KEY` key gratis dari openalex.org. Tanpa key, query anonim tetap bisa,
  tetapi paginasi cursor halaman kedua ke atas ditolak OpenAlex.
- `UNPAYWALL_EMAIL` email kontak yang sebenarnya. Tanpa ini, pencarian full text
  open access lewat Unpaywall dilewati.

Jangan pernah menuliskan nilai variabel ini ke dalam berkas skill atau ke dalam chat.

## Cara memeriksa bahwa skill ini benar-benar jalan

Setiap skill punya bagian `Verifikasi` berisi blok Python yang bisa dijalankan langsung.
Jalankan blok itu setelah pemasangan. Yang diharapkan muncul:

- `academic-source-verification` mencetak hasil pencocokan identitas OpenAlex dan
  Crossref, plus catatan SKIP bila `UNPAYWALL_EMAIL` belum diisi.
- `literature-analysis` mencetak hasil uji work, irisan topik, group by sumber,
  pencarian teks, dan filter penulis, plus catatan SKIP untuk paginasi halaman kedua
  bila `OPENALEX_API_KEY` belum diisi.

SKIP berarti layanan itu belum diuji, bukan lulus. Perlakukan keduanya berbeda.

## Batas yang perlu diketahui

Skill ini tidak menggantikan penilaian manusia. Simulasi review, penandaan kesalahan
logika, dan penilaian sifat sitasi adalah penilaian model yang harus dipisahkan dari
fakta data. Laporan selalu menyertakan kutipan agar bisa diperiksa ulang.

Pembandingan kemiripan teks bersifat lokal dan hanya mencakup kandidat yang full text-nya
berhasil diunduh. Itu bukan pemeriksaan plagiarisme seluruh web.

## Lisensi dan asal usul

MIT. Lihat `LICENSE`. Paket ini adaptasi dari `xngg1021/hermes-academic-skills` pada
commit `439ce4a`, yang saat itu berlisensi MIT. Rincian perubahan dan dua bug yang
diperbaiki ada di `NOTICE.md`.
