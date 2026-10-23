# academic-research-skills-kit

Kumpulan skill akademik untuk Hermes Agent, disusun berlapis dari riset sampai publikasi.
Tujuannya satu: dipakai untuk mengerjakan tesis dan menulis paper tanpa harus memilih
dari delapan puluh lebih skill profil setiap kali.

Enam belas skill ini bukan semuanya tulisan saya. Tiga di antaranya adaptasi dari
snapshot MIT `xngg1021/hermes-academic-skills`, sisanya skill profil Hermes Agent yang
saya pakai, sebagian saya modifikasi. Atribusi lengkap per skill ada di `NOTICE.md`.

## Apa yang sengaja tidak ikut

Paket ini tidak memuat skill yang terikat langsung ke satu data penelitian tertentu.
Dua skill seperti itu dikeluarkan karena hanya berguna untuk satu proyek, dan tidak bisa
dipakai orang lain tanpa data dan konteks yang sama. Isinya bukan rahasia, tapi memang
tidak general.

Yang tersisa murni prosedur: cara merumuskan masalah, cara memetakan literatur, cara
memverifikasi sumber, cara menulis, cara mengirim. Bisa dipakai untuk tesis maupun paper,
di bidang apa pun.

## Struktur

### 01-riset: merumuskan dan memetakan

- `research-problem-and-gap` merumuskan masalah, isu, dan celah penelitian dengan rumus
  yang bisa dipertanggungjawabkan.
- `design-science-research-positioning` menempatkan kerangka DSR (Hevner, Peffers, Leavitt)
  di proposal atau tesis.
- `dsr-self-audit` memeriksa tesis DSR sendiri sebelum masuk bimbingan.
- `literature-mapping` memetakan lanskap riset untuk membangun bukti celah.
- `socratic-research-dialogue` menuntun berpikir lewat lima lapis pertanyaan T-A-B-K-A,
  dengan jangkar fakta ke skill lain supaya tidak mengarang.
- `arxiv` mencari paper di arXiv.
- `journal-scouting` mencari paper dan mengumpulkan URL akses terbuka.

### 02-verifikasi: memeriksa sebelum mengutip

- `academic-source-verification` memastikan sitasi nyata, metadata cocok, tidak ditarik,
  dan full text yang diunduh benar.
- `literature-analysis` mencari paper mirip, kontradiksi, profil penulis, dan kepadatan
  topik. Dua belas alur kerja.
- `grounded-citations` mengikat jawaban dan dokumen pada sumber yang bisa diperiksa.

### 03-penulisan: menyusun naskah

- `paper-writing` menulis manuskrip jurnal dengan struktur IMRAD.
- `thesis-proposal` menyusun proposal atau problem statement.
- `thesis-docx-writing` mengubah draf markdown menjadi docx yang bersih.
- `thesis-supervisor-outreach` mendekati calon pembimbing.

### 04-publikasi: mengirim

- `indo-journal-scouting` menelusuri jurnal Indonesia lewat Garuda dan SINTA.
- `survey-instrument-design` menyusun atau merevisi item kuesioner.

## Pemasangan

Salin seluruh folder lapis ke direktori skill profil Hermes:

```
cp -r skills/01-riset/*        "$HERMES_PROFILE/skills/research/"
cp -r skills/02-verifikasi/*   "$HERMES_PROFILE/skills/research/"
cp -r skills/03-penulisan/*    "$HERMES_PROFILE/skills/research/"
cp -r skills/04-publikasi/*    "$HERMES_PROFILE/skills/research/"
```

Pada Hermes dengan profil terpisah, tujuannya `$HERMES_HOME/skills/research/`. Di Windows,
ganti `$HERMES_HOME` dengan folder profil Hermes milikmu.

Kalau kamu hanya butuh satu lapis, salin lapis itu saja. Tidak perlu semuanya.

## Catatan ukuran

Hermes memuat isi SKILL.md ke dalam konteks saat skill dipanggil. Skill terbesar di paket
ini sekitar 40 KB, jadi panggil satu per satu sesuai kebutuhan. Jangan memuat seluruh
paket tanpa alasan.

## Variabel lingkungan opsional

Beberapa skill memakai API publik dan bisa berjalan tanpa kunci:

- `OPENALEX_API_KEY` key gratis dari openalex.org. Tanpa key, query anonim tetap bisa,
  tetapi paginasi cursor halaman kedua ke atas ditolak OpenAlex.
- `UNPAYWALL_EMAIL` email kontak yang sebenarnya, untuk pengecekan full text open access.

Jangan menuliskan nilai variabel ini ke dalam berkas skill atau ke chat. Simpan di
variabel lingkungan atau berkas `.env` yang masuk `.gitignore`.

## Batas yang perlu diketahui

Skill ini alat bantu, bukan pengganti penilaian peneliti. Simulasi review, penandaan
kesalahan logika, dan penilaian sifat sitasi adalah penilaian model yang harus dipisahkan
dari fakta data. Laporan selalu menyertakan kutipan agar bisa diperiksa ulang.

Pembandingan kemiripan teks di `literature-analysis` bersifat lokal dan hanya mencakup
kandidat yang full text-nya berhasil diunduh. Itu bukan pemeriksaan plagiarisme seluruh web.

## Lisensi

MIT. Lihat `LICENSE` dan `NOTICE.md`. Tiga skill berasal dari
`xngg1021/hermes-academic-skills` commit `439ce4a` yang saat itu berlisensi MIT.
