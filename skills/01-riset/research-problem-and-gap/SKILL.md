---
name: research-problem-and-gap
description: "Use when formulating a research problem and literature gap."
version: 0.1.0
author: Mahdy, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [problem-statement, research-gap, novelty, proposal, thesis]
    related_skills: [thesis-proposal, literature-mapping, design-science-research-positioning]
---

# Research Problem and Gap

Memisahkan tiga hal yang sering dicampur di Bab 1: ISSUE (persoalan jangka panjang),
PROBLEM (masalah yang akan dipecahkan), dan GAP (celah pada literatur yang ditinjau).
Skill ini soal perumusan, bukan pencarian pustaka.

## When to Use
- Menyusun latar belakang atau rumusan masalah di Bab 1.
- Menyusun pernyataan gap untuk proposal atau tesis.
- Penguji menanya "gap-nya apa, bedanya dengan yang sudah ada apa?".
- Don't use for: memetakan literatur secara sistematis (pakai literature-mapping), atau
  menulis naskah akademik jadi (pakai thesis-proposal).

## Tiga Lapis yang Harus Dipisah
- ISSUE = persoalan jangka panjang dan sistemik. Satu tesis tidak menyelesaikannya.
- PROBLEM = masalah spesifik yang akan dipecahkan penelitian ini.
- GAP = celah pada literatur yang ditinjau, bukan celah pada praktik.

Hubungan: Issue menimbulkan Problem. Problem punya justifikasi akademik karena ada Gap.
Penelitian mengisi Gap untuk menjawab Problem, sebagai respons terhadap Issue.

Mnemonic: I-P-G, "Isu Panjang, Gap" - isu panjang, problem yang dipilih, gap yang diisi.

## Rumus Gap

> Sedang banyak penelitian membahas [temuan yang sudah ada], belum ditemukan pada literatur
> yang ditinjau [dimensi yang hilang], khususnya dalam konteks [konteks]. Akibatnya, belum
> jelas bagaimana [mekanisme yang akan diuji]. Studi ini mengisi gap ini dengan [pendekatan].

Frasa kebaruan yang wajib dipakai: "belum ditemukan pada literatur yang ditinjau".
Frasa yang dilarang: "belum pernah ada", "belum ada yang meneliti", "teori baru".

## Tipe Gap yang Layak Disebut
Urut dari yang paling sering dipakai di tesis terapan:
- Konseptual: aliran teori belum dipindahkan ke konteks baru.
- Empiris: belum ada uji pada konteks atau populasi tersebut.
- Metodologis: pendekatan yang ada belum berbasis aturan eksplisit atau belum dapat diaudit.
- Praktis: kebijakan atau standar sudah ada, belum menjadi alat yang dapat dieksekusi.
Sebuah tesis yang kuat biasanya menyebut dua tipe, bukan lima sekaligus.

## Procedure
1. Tulis ISSUE satu kalimat. Kriteria selesai: kalimat itu masih akan benar lima tahun lagi,
   dan tidak bisa diselesaikan oleh satu tesis.
2. Tulis PROBLEM satu kalimat. Kriteria selesai: ada subjek, predikat, dan batas konteks;
   menjawab pertanyaan "kenapa ini harus dipecahkan sekarang".
3. Tentukan tipe gap yang dipakai, maksimal dua. Kriteria selesai: tiap tipe punya alasan
   mengapa tipe itu yang dipilih.
4. Tulis pernyataan gap dengan rumus di atas. Kriteria selesai: memuat dimensi yang hilang,
   konteks, akibat, dan pendekatan yang ditawarkan.
5. Verifikasi gap belum diisi. Kriteria selesai: ada penelusuran live (OpenAlex atau Scopus),
   bukan penilaian dari ingatan.
6. Cek frasa. Kriteria selesai: nol kemunculan "belum pernah ada" dan "teori baru".

## Pitfalls
- GAP bukan masalah praktik. Kalau ditulis "di rumah sakit belum ada alat", itu problem,
  bukan gap. Gap harus menyebut literatur yang ditinjau.
- Gap lemah: "masih sedikit penelitian". Itu quantity gap, jenis paling lemah. Ganti dengan
  dimensi yang spesifik: konteks, mekanisme, atau metode yang belum dipakai.
- Jangan mengarang angka di bagian kondisi nyata. Setiap angka wajib punya sumber atau
  penyebut dari data penelitian sendiri.
- Jangan menyebut nama file data atau nama tabel internal di naskah. Cukup deskripsi isi:
  jumlah baris, jumlah kolom, periode, sumber.
- Gap yang terlalu lebar membuat tesis tidak selesai. Gap yang terlalu sempit bikin penguji
  bertanya "kenapa ini penting".

## Verification
- [ ] Issue, problem, dan gap tertulis sebagai tiga kalimat berbeda.
- [ ] Gap menyebut literatur, bukan hanya praktik lapangan.
- [ ] Maksimal dua tipe gap yang diklaim.
- [ ] Frasa "belum ditemukan pada literatur yang ditinjau" dipakai, "belum pernah ada" tidak.
- [ ] Setiap angka punya sumber atau penyebut.
- [ ] Ada jejak penelusuran live untuk menguji gap belum terisi.
