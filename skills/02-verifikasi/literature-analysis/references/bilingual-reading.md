# Pembacaan Dwibahasa

Untuk alur kerja J. Dipakai saat perlu mencerna paper berbahasa asing dengan cepat: ringkasan per bagian plus daftar istilah, bukan terjemahan penuh. Bahasa target mengikuti pengguna; bisa Indonesia ke Inggris, atau Inggris ke Indonesia.

## Langkah

1. Ekstrak teks dengan pymupdf per halaman, lalu potong per bagian: Abstract, Introduction, Method, Results, Discussion, Conclusion.
2. Untuk tiap bagian, hasilkan tiga hal: tiga sampai lima kalimat inti dalam bahasa target yang menjawab "bagian ini menjawab apa dan menyimpulkan apa"; satu sampai tiga kalimat kunci dalam bahasa aslinya, supaya pengguna bisa memeriksa istilah langsung; dan istilah baru yang muncul.
3. Daftar istilah: pakai satu padanan istilah untuk seluruh teks. Saat istilah pertama kali muncul, catat "aslinya, padanannya", lalu pakai konsisten. Padanan yang belum yakin ditandai (sementara) beserta alternatif yang umum.
4. Gambar dan tabel tidak diterjemahkan. Jelaskan satu kalimat per gambar atau tabel tentang apa yang ditunjukkannya, dan tunjuk nomor halamannya.

## Format keluaran

```
Bagian 3 Metode
Inti: ...
Kalimat kunci: "..." (aslinya)
Istilah: self-attention menjadi attention antar token; positional encoding menjadi encoding posisi

Gambar 2 (halaman 5)
Isi: akurasi model pada dataset X berubah menurut jumlah lapisan
```

## Aturan

- Makna teknis tidak boleh bergeser. Bila satu kalimat meragukan, beri versi harfiah dan versi bebas, lalu biarkan pengguna memilih.
- Rumus tidak diterjemahkan dan tidak diubah urutannya; simpan LaTeX apa adanya.
- Daftar istilah terakumulasi dalam sesi. Saat mengerjakan beberapa paper dengan topik sama, pakai daftar yang sama agar konsisten.
- Ini alat bantu baca, bukan pengganti penilaian pengguna. Pada simpulan penting, ingatkan "periksa paragraf X di teks aslinya".
