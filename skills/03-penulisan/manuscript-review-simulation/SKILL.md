---
name: manuscript-review-simulation
description: Use when simulating review of a manuscript before submission.
version: 1.0.0
author: Mahdy Arief (mahdyarief)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [review, manuscript, editorial, peer-review, simulation]
    related_skills: [paper-writing, literature-analysis, claim-evidence-map, reviewer-response-coach]
---

# Simulasi Review Naskah

Menjalankan satu putaran review atas naskah sendiri, seolah dibaca reviewer yang tidak
punya kepentingan agar naskah ini lolos. Tujuannya menemukan kelemahan sebelum orang lain
menemukannya, bukan mengukur peluang diterima.

Skill ini **tidak** memberi skor, persentase peluang, atau peringkat. Penilaian reviewer
simulasi bukan prediksi keputusan jurnal, dan tidak boleh disampaikan seolah begitu.

## Kapan dipakai

- Sebelum mengirim manuskrip ke jurnal.
- Sebelum mengirim bab tesis ke pembimbing.
- Setelah revisi besar, untuk memeriksa apakah perbaikannya menyentuh akar masalah.

Jangan pakai untuk menulis naskahnya. Kalau naskah belum ada, itu pekerjaan `paper-writing`.

## Empat sudut baca

Mnemonic: **ORI-MET-BUK-ARG**, plus dua penilai tambahan di bawahnya.

1. *ORI (Orisinalitas).* Kontribusinya apa, dibanding karya yang sudah ada, dan klaim
   kebaruannya boleh sekuat apa. Replikasi dan pengujian batas bisa jadi kontribusi sah
   tanpa teori baru, jangan direndahkan hanya karena tidak baru.
2. *MET (Metodologi).* Apakah desainnya bisa menjawab pertanyaan penelitian, dan apakah
   cara pelaksanaannya mendukung kesimpulan yang diambil.
3. *BUK (Bukti).* Apakah setiap klaim penting ditopang bukti dengan jenis, mutu, dan
   cakupan yang cukup. Tidak ada batas jumlah sumber universal. Syarat angka hanya boleh
   dipakai kalau memang ditetapkan oleh jurnal atau pedoman yang kamu sebut namanya.
4. *ARG (Argumen).* Apakah rantai masalah, celah, pertanyaan, metode, temuan, dan implikasi
   nyambung tanpa lompatan logika.

Dua tambahan yang sering dilupakan:

- *Gaya penulisan.* Apakah alasannya disampaikan cukup jelas untuk diperiksa, tanpa
  mencampur kemerahan bahasa dengan mutu penelitian.
- *Integrasi literatur.* Apakah literatur yang dipakai benar-benar yang dibutuhkan untuk
  pertanyaan, alternatif, dan kontribusinya.

## Penilai kedua: Devil's Advocate

Selalu hadir, tidak boleh dilewat.

- Tulis argumen tandingan terkuat, 200 sampai 300 kata, yang bisa dijawab reviewer
  sungguhan.
- Daftar masalah dikategorikan KRITIS, MAYOR, MINOR, dengan lokasi.
- Sebut penjelasan alternatif dan pemangku kepentingan yang diabaikan.
- Sebut juga hal yang bukan cacat, supaya tidak ada kesan menyerang.

## Cara menilai per dimensi

Lima label, jangan lebih, dan jangan diubah jadi angka.

- *MELEBIHI* jika melampaui apa yang diminta kriterianya.
- *MEMENUHI* jika sesuai dan bisa ditunjuk buktinya.
- *SEBAGIAN* jika arahnya benar tapi tidak lengkap.
- *TIDAK MEMENUHI* jika kriterianya jelas gagal.
- *TAK DINILAI* jika tidak bisa dinilai dengan bahan yang ada.

Setiap label wajib disertai lokasi bukti, alasan, dan penyebutan apakah penilaian itu
mempengaruhi rekomendasi. Jangan menyusun total, bobot, atau persentase dari kelima label
ini. Itu bukan skala.

## Empat rekomendasi editorial

- *Terima*: semua kriteria inti terverifikasi positif, tidak ada kelemahan penentu yang
  belum tertutup.
- *Revisi kecil*: inti sudah layak, sisanya perbaikan terbatas. Biasanya penambahan
  rujukan, penjelasan metode, atau kejelasan argumen.
- *Revisi besar*: ada kelemahan material yang bisa diperbaiki, tapi butuh kerja nyata:
  analisis ulang, penambahan data, atau penataan model teoretis.
- *Tolak*: ada kegagalan inti yang tidak bisa diperbaiki dengan revisi.

Beban bukti untuk Terima sama beratnya dengan Tolak. Jangan melonggarkan Terima karena
kasihan pada diri sendiri, dan jangan mengeraskan Tolak supaya terlihat teliti. Nada
sopan hanya mengatur kata, bukan menurunkan tingkat keparahan temuan.

Kalau menolak, sebut subtipe yang paling dekat: di luar cakupan jurnal, cacat mendasar,
kontribusi kurang, belum matang, atau layak dikirim ulang setelah ditata.

## Aturan yang tidak boleh dilanggar

- Jangan mengarang temuan yang tidak ada di naskah. Setiap temuan harus bisa ditunjuk
  lokasinya.
- Jangan menyunting naskah. Simulasi review bersifat baca saja.
- Jangan menghaluskan temuan supaya nyaman, dan jangan menambah temuan supaya terlihat
  banyak. Ikuti bukti ke dua arah.
- Jangan menyimpulkan peluang diterima di jurnal dari hasil simulasi ini.
- Kalau naskah menyembunyikan bagian yang krusial, itu temuan, bukan alasan untuk berhenti.

## Keluaran

Lima bagian ringkas:

1. Tabel penilaian: dimensi, label, lokasi bukti, alasan, dan apakah mempengaruhi
   rekomendasi.
2. Daftar masalah dari Devil's Advocate, dikategorikan KRITIS, MAYOR, MINOR.
3. Rekomendasi editorial, beserta kriteria mana yang membuatnya cocok.
4. Peta revisi: temuan mana diselesaikan di bagian mana.
5. Satu kalimat jujur tentang batas simulasi ini.

## Hubungan dengan skill lain

- `claim-evidence-map` memeriksa klaim ke bukti satu per satu, ini memeriksa naskah utuh.
- `literature-analysis` menyediakan pembanding dan kontradiksi.
- `reviewer-response-coach` dipakai setelah komentar reviewer asli datang.
