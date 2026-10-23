---
name: dsr-self-audit
description: "Use when self-auditing a DSR thesis before supervision."
version: 0.1.0
author: Mahdy, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [dsr, audit, hevner, checklist, thesis-review, qa]
    related_skills: [design-science-research-positioning, thesis-defense-positioning, research-problem-and-gap]
---

# DSR Self-Audit

Memeriksa tesis riset desain memakai tujuh pedoman Hevner sebagai daftar periksa
diagnostik sebelum bimbingan. Baris yang kosong menandai titik rawan ditembak penguji.
Skill ini memeriksa, bukan menulis.

## When to Use
- Sebelum bimbingan, sebelum sidang, atau sebelum mengirim bab ke pembimbing.
- Setelah bab hasil ditulis, ingin tahu klaim mana yang belum punya bukti.
- Penguji atau pembimbing menanya "ini riset atau laporan proyek?".
- Don't use for: memposisikan kerangka (pakai design-science-research-positioning) atau
  merumuskan gap (pakai research-problem-and-gap).

## Aturan Dasar
Hevner menolak pemakaian kaku (rote use). Ketujuh pedoman harus disapa dalam bentuk
apa pun, tetapi cara menyapanya dinilai dengan pertimbangan peneliti. Checklist ini
bukan centang mekanis, melainkan deteksi lubang.

Mnemonic tujuh pedoman: APA - KENAPA - BUKTI - BARU - KETAT - CARI - OMONG.

## Checklist Diagnostik
1. G1 Design as an Artifact: APA artefaknya? Bentuknya construct, model, method, atau
   instantiation? Bisa ditunjuk komponennya? Jebakan: "sistem cerdas" tanpa penunjuk.
2. G2 Problem Relevance: KENAPA masalahnya nyata? Ada bukti praktik, bukan asumsi peneliti?
   Jebakan: alat dibangun dulu, masalah dicari belakangan.
3. G3 Design Evaluation: BUKTI apa yang menunjukkan artefak berguna? Metrik apa, data apa,
   pembanding apa? Keluarga metode: observational, analytical, experimental, testing,
   descriptive. Jebakan: hanya demonstrasi layar tanpa metrik.
4. G4 Research Contributions: BARU di mana? Kontribusi pada artefak, fondasi desain, atau
   metodologi? Jebakan: mengklaim "teori baru" padahal hanya memindahkan aliran.
5. G5 Research Rigor: KETAT di dua sisi. Saat membangun (sumber aturan resmi) dan saat
   mengevaluasi (metrik ditetapkan sebelum menjalankan, bukan setelah lihat hasil).
6. G6 Design as a Search Process: CARI alternatif. Ada desain lain yang dipertimbangkan dan
   ditolak? Desain adalah satisficing, bukan penemuan solusi optimal.
7. G7 Communication of Research: OMONG ke dua audiens. Teknis bisa membangun ulang,
   manajerial bisa memutuskan adopsi.

## Procedure
1. Salin tujuh baris checklist ke catatan kerja, satu baris per pedoman.
2. Untuk tiap baris, tulis bukti konkret dari naskah: nomor subbab dan kalimatnya.
   Kriteria selesai: tidak ada baris yang diisi dengan rencana, hanya dengan isi yang sudah ada.
3. Tandai setiap baris yang kosong atau hanya berisi niat. Kriteria selesai: daftar lubang
   eksplisit, diurutkan dari yang paling mudah ditembak penguji.
4. Petakan tiap lubang ke bab tempat perbaikannya. Kriteria selesai: tiap lubang punya bab
   tujuan, bukan hanya label.
5. Cek pemetaan ke tiga siklus Hevner. Kriteria selesai: G1-G2 ke Relevance, G4-G5 ke Rigor,
   G3-G6 ke Design, G7 sebagai pintu keluar.

## Yang Masuk Naskah, Yang Tetap di Catatan
Masuk naskah, porsi kecil dan fungsional:
- Pernyataan bahwa ini riset desain dan menghasilkan pengetahuan preskriptif. Satu paragraf.
- Dua sisi pengetahuan: tertanam di artefak dan eksplisit di justifikasi. Satu sampai dua kalimat.
- Tingkat kontribusi, dengan justifikasi apa yang dipindahkan dari mana ke mana.
- Keluarga metode evaluasi yang dipakai beserta alasannya.
- Pernyataan keterulangan: prosedur cukup rinci agar dapat diulang pihak lain.

Tetap di catatan, jangan dimasukkan naskah:
- Ontologi critical realism dan istilah filsafat lain tanpa konsekuensi konkret.
- Istilah lambda-knowledge. Cukup pakai frasa "pengetahuan preskriptif".
- Perdebatan ontology, epistemology, axiology riset desain.
- Perbandingan tokoh satu per satu.

Aturan: setiap istilah filsafat wajib disusul kalimat "konsekuensinya dalam penelitian ini
adalah ...". Tanpa itu, jangan dimasukkan ke naskah.

## Pitfalls
- Evaluasi hanya berupa tangkapan layar antarmuka. Itu deskriptif, bukan pengujian.
- Memilih metrik setelah melihat hasil supaya terlihat baik. Itu pembenaran, bukan rigor.
- Menyebut istilah filsafat untuk terlihat mendalam, tanpa kaitan ke keputusan desain.
- Menilai artefak hanya dengan "sistem berjalan dengan baik". Itu tidak dapat diverifikasi.
- Menganggap checklist ini wajib dicentang semua. Hevner menolak rote use.

## Verification
- [ ] Tujuh baris punya bukti dari naskah, dengan nomor subbab.
- [ ] Daftar lubang tertulis dan terurut berdasarkan risiko.
- [ ] Tiap lubang punya bab tujuan perbaikan.
- [ ] Pemetaan ke tiga siklus Hevner diperiksa.
- [ ] Istilah filsafat di naskah selalu disertai kalimat konsekuensi.
