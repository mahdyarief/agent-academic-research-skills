# Template Simulasi Review

## Pernyataan yang wajib ada di awal keluaran

Ini simulasi review yang dibuat model berdasarkan kerangka review standar. Ia tidak menggantikan peer review sebenarnya dan bukan pendapat resmi tentang penerimaan atau penolakan. Review sungguhan terikat kewajiban kerahasiaan dan pemeriksaan konflik kepentingan, sehingga template ini tidak berlaku untuk pengiriman naskah nyata.

## Kerangka penilaian

Nilai per bagian dengan tiga kolom: kelebihan, masalah, dan saran. Setiap kritik wajib menunjuk paragraf tertentu di paper, dengan kutipan kalimat atau nomor paragraf. Kritik umum tanpa letak tidak diterima.

1. Kontribusi dan kebaruan. Apa kontribusi intinya? Apakah perbedaannya dengan karya sebelumnya bersifat substantif atau hanya kemasan? Apakah kekuatan klaim sepadan dengan buktinya?
2. Metode dan desain eksperimen. Apakah metode dijelaskan cukup untuk direproduksi, termasuk data, hiperparameter, lingkungan, dan seed? Apakah baseline-nya adil? Apakah uji ablasi menjawab komponen mana yang berperan? Apakah metriknya sesuai masalah?
3. Validitas hasil. Apakah uji statistiknya tepat, mencakup signifikansi, effect size, dan interval kepercayaan? Apakah ada koreksi untuk banyak perbandingan? Apakah hasilnya hanya ditopang sedikit sampel atau satu seed tertentu? Apakah error bar dan varians dilaporkan?
4. Kesesuaian simpulan dengan bukti. Apakah setiap kalimat simpulan punya bukti langsung di eksperimen? Adakah lompatan dari hasil A ke simpulan B? Apakah abstrak dan simpulan membesar-besarkan bagian eksperimen?
5. Keterbatasan. Keterbatasan apa yang diakui penulis? Keterbatasan jelas apa yang terlewat, misalnya bias data, batas generalisasi, dan biaya komputasi?
6. Etika dan reproduksibilitas. Apakah pengumpulan data sesuai ketentuan? Apakah kode dan data dibuka? Adakah pernyataan reproduksibilitas?

## Penilaian akhir

- Skor 5 berarti terima, 4 revisi kecil, 3 revisi besar, 2 tolak tetapi boleh kirim ulang, 1 tolak keras.
- Tiga alasan penentu, masing-masing satu kalimat, dan tunjuk bagian mana.
- Daftar perbaikan yang bisa dikerjakan penulis, diurutkan menurut prioritas.

## Format keluaran

```
Pernyataan simulasi: ...

Paper: judul, tahun, jumlah penulis

1. Kontribusi dan kebaruan
Kelebihan: ...
Masalah: ... (lihat bagian X paragraf Y: "kutipan")
Saran: ...

(butir 2 sampai 6 sama polanya)

7. Penilaian akhir
Skor: 3 dari 5 (revisi besar)
Alasan penentu:
1. ...
2. ...
3. ...
Daftar perbaikan menurut prioritas:
- Tinggi: ...
- Sedang: ...
- Rendah: ...
```

## Aturan nada

Pakai bahasa netral, spesifik, dan membangun. Kritik pada karyanya, bukan pada orangnya. Hindari kata bernada menghakimi seperti "mengecewakan" atau "berkualitas rendah"; tulis saja "bukti belum cukup menopang simpulan itu" atau "uji ablasi ini belum memisahkan kontribusi A dan B". Sertakan minimal satu kelebihan di setiap bagian agar keluarannya tidak hanya berisi kritik.
