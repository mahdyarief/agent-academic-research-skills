---
name: claim-evidence-map
description: Use when mapping each claim in a draft to its own evidence.
version: 1.0.0
author: Mahdy Arief (mahdyarief)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [claims, evidence, audit, writing, verification]
    related_skills: [grounded-citations, academic-source-verification, literature-analysis, research-problem-and-gap]
---

# Peta Klaim dan Bukti

Memetakan setiap klaim di sebuah naskah ke buktinya masing-masing, lalu memberi status.
Hasilnya satu tabel yang bisa dibaca dalam satu menit, bukan esai.

Dipakai saat draf sudah ada dan perlu diperiksa sebelum dikirim ke pembimbing atau
jurnal. Bukan untuk menulis, bukan untuk mencari literatur.

## Urutan kerja

Mnemonic: WAJIB-SARING-UJI-TOLAK.

- *WAJIB*: kumpulkan dulu semua kalimat yang berbentuk klaim. Kalimat deskriptif biasa
  bukan klaim, jangan dimasukkan.
- *SARING*: buang klaim yang isinya cuma alasan atau definisi umum. Sisakan yang
  mengikat pada satu bukti tertentu.
- *UJI*: untuk setiap klaim yang tersisa, cari buktinya di naskah dan di data.
- *TOLAK*: klaim yang tidak punya bukti tidak ditambal dengan kalimat baru. Ditolak atau
  diturunkan jadi pernyataan hipotetis.

## Apa yang dihitung sebagai klaim

Ya:

- Pernyataan hasil: ada pengaruh, ada peningkatan, ada perbedaan, ada hubungan.
- Pernyataan kausal: karena X, maka Y.
- Pernyataan kebaruan: belum ditemukan pada literatur, berbeda dari studi sebelumnya.
- Pernyataan generalisasi: sebagian besar, selalu, semua, kebanyakan.
- Angka apa pun yang punya penyebut tersirat.

Bukan klaim:

- Definisi istilah dari sumber yang sudah dikutip dan dikutip dengan benar.
- Kalimat latar belakang yang tidak menyatakan apa pun soal temuan.
- Rencana kerja: penelitian ini akan melakukan, bagian ini membahas.

## Tiga status

Jangan pakai status lain, dan jangan menilai dengan perasaan.

- *SIAP*: bukti ada, terukur, dan penyebutnya jelas. Kalau angka, ada numerator dan
  denominator, dan keduanya bisa dilacak ke berkas atau tabel.
- *KURANG*: ada arah bukti tapi tidak cukup untuk menopang kekuatan kalimatnya. Contoh:
  klaim generalisasi ditopang satu studi kasus, atau angka tanpa penyebut, atau klaim
  kausal ditopang korelasi.
- *TAK DINILAI*: buktinya ada di luar naskah dan belum diperiksa saat pemetaan ini
  dijalankan. Bukan status aman, ini utang yang harus ditutup.

Status TAK DINILAI tidak boleh dipakai untuk menghindari pekerjaan. Pakai hanya kalau
memang butuh akses ke berkas atau data yang belum dibuka.

## Format keluaran

Satu tabel dengan lima kolom:

- Lokasi: bab dan paragraf, atau nomor baris.
- Klaim: dipotong sampai satu kalimat, jangan diubah katanya.
- Bukti yang diklaim naskah: apa yang naskah tunjuk, sitasi atau tabel.
- Bukti yang benar-benar diperiksa: hasil pemeriksaan mandiri.
- Status: SIAP, KURANG, atau TAK DINILAI.

Setelah tabel, tiga baris ringkasan: jumlah per status, satu klaim paling berisiko, dan
satu langkah perbaikan terkecil.

## Aturan yang tidak boleh dilanggar

- Jangan melunakkan klaim di tabel. Tulis apa adanya, walaupun hasilnya buruk.
- Jangan menilai klaim dari memori. Kalau bukti belum dibuka, statusnya TAK DINILAI.
- Jangan menyebutkan angka tanpa penyebut. Kalau naskah menyebut persen tanpa penyebut,
  itu sudah cukup untuk memberi status KURANG.
- Klaim kebaruan wajib diberi status KURANG kalau dasarnya hanya "belum ada yang meneliti".
  Dasarnya harus penelusuran literatur yang bisa ditunjuk hasilnya.
- Jangan mengusulkan kalimat pengganti saat memetakan. Pemetaan dan penulisan dua
  pekerjaan berbeda, dan mencampurnya membuat hasil audit bias.

## Hubungan dengan skill lain

- `grounded-citations` untuk memeriksa apakah sumber yang dikutip benar-benar ada dan
  mendukung klaim yang dipasangkan padanya.
- `academic-source-verification` untuk identitas sitasi, retraksi, dan metadata.
- `literature-analysis` untuk memeriksa klaim kebaruan terhadap literatur yang terkumpul.
- `research-problem-and-gap` kalau hasil pemetaan menunjukkan celahnya sendiri belum kuat.

## Verifikasi

Tidak ada API yang diuji karena isinya prosedur pemeriksaan naskah. Yang diperiksa saat
pemakaian: setiap baris tabel bisa dilacak ke lokasi naskah yang disebut, dan tidak ada
status SIAP yang diberikan tanpa bukti yang benar-benar dibuka.
