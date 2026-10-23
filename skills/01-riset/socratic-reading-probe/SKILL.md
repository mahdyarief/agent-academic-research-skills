---
name: socratic-reading-probe
description: Use when probing whether a paper was actually read closely.
version: 1.0.0
author: Mahdy Arief (mahdyarief)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [reading, paper, probing, socratic, verification]
    related_skills: [socratic-research-dialogue, claim-evidence-map, academic-source-verification, literature-analysis]
---

# Probe Bacaan Socratic

Menanyai teks, bukan menanyai penulisnya. Dipakai setelah satu paper dibaca, untuk
mengetahui apakah isinya benar-benar masuk atau hanya terasa sudah dibaca.

Pembeda dengan skill lain:

- `socratic-research-dialogue` menanyai pikiran sendiri, lapisnya T-A-B-K-A.
- `literature-analysis` membantu mencari paper yang layak dibaca lebih dulu.
- Skill ini menanyai hasil bacaan. Enam pertanyaan, satu paper, setelah dibaca.

## Enam pertanyaan

Ajukan satu per satu, tunggu jawaban, baru lanjut. Jangan memberi jawaban lebih dulu.

1. *Klaim.* Apa satu klaim utama paper ini, dalam satu kalimatmu sendiri?
2. *Bukti.* Bukti apa yang dipakai menopang klaim itu, dan bukti jenis apa: angka,
   wawancara, simulasi, atau argumen konseptual?
3. *Sampel.* Berapa ukuran sampel atau data yang dipakai, dan dari mana asalnya?
4. *Pembanding.* Apa pembanding atau baseline-nya, dan kenapa pembanding itu yang dipilih?
5. *Keterbatasan.* Keterbatasan apa yang diakui penulis sendiri, dan mana yang tidak
   diakui tapi terlihat dari metode?
6. *Dicurigai.* Bagian mana yang paling tidak kamu percaya, dan apa alasan
   ketidakpercayaan itu?

Mnemonic: K-B-S-P-K-D (Klaim, Bukti, Sampel, Pembanding, Keterbatasan, Dicurigai).

## Cara menilai jawaban

Tiga status, jangan lebih.

- *DAPAT* jika jawaban bisa ditunjuk kembali ke bagian tertentu paper.
- *RAPUH* jika jawabannya benar arah tapi tidak bisa ditunjuk letaknya. Itu tanda
  bagian itu belum dibaca teliti.
- *TIDAK* jika tidak ada jawaban atau jawabannya menyimpang dari isi paper.

Jangan menilai berdasarkan panjang jawaban. Jawaban tiga kata yang tepat lebih bernilai
daripada paragraf yang mengambang.

## Aturan saat menjalankan

- Satu pertanyaan per balasan. Kalau perlu, minta jawaban di satu kalimat.
- Kalau jawaban RAPUH atau TIDAK, tunjuk bagian paper yang perlu dibaca ulang, dengan
  kutipan pendek atau nomor halaman. Jangan mengarang lokasi.
- Jangan menjawab pertanyaan dengan jawabanmu sendiri. Kalau kamu memberi isi paper,
  probe berubah jadi rangkuman dan tidak ada yang terukur.
- Maksimal enam pertanyaan. Setelah itu tutup, jangan menambah pertanyaan tambahan.
- Kalau paper-nya tidak ada di tangan dan kamu tidak bisa memeriksa isinya, katakan
  terus terang bahwa probe ini hanya mengandalkan ingatan pembaca, dan tandai hasilnya
  sebagai tidak terverifikasi.

## Keluaran

Tutup dengan tiga baris:

1. Skor: berapa DAPAT, RAPUH, dan TIDAK dari enam pertanyaan.
2. Bagian paper yang perlu dibaca ulang, sebut bagian atau halamannya.
3. Satu pertanyaan lanjutan yang paling layak dipikirkan setelah membaca ulang.

## Satu catatan penting

Probe ini tidak mengukur pemahaman konsep, hanya kedekatan dengan isi teks. Paper yang
dipahami jauh bisa tetap gagal di pertanyaan sampel karena penulis tidak menyebutnya.
Bedakan dua hal itu saat menulis kesimpulan.
