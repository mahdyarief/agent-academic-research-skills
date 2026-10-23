# Matriks Tinjauan

Untuk alur kerja G. Mampatkan puluhan paper menjadi tabel yang bisa dibandingkan, untuk tinjauan literatur dan penyaringan sistematis.

## Langkah

1. Cari 20 sampai 50 kandidat dengan metode alur kerja A di SKILL.md utama: pencarian teks, ID topik, rekomendasi `related_works`, dan kumpulan sitasi. Laporkan rentang paginasi, lalu urutkan berdasarkan relevansi dan ambil N teratas.
2. Rekonstruksi abstrak dari `abstract_inverted_index` OpenAlex. Bila kosong, ambil `message.abstract` dari Crossref `works/{DOI}`. Bila masih kosong, tandai "perlu full text" dan jangan diisi dengan dugaan.
3. Isi matriks per paper dengan lima kolom: paper dan tahun, metode, sampel atau data, simpulan utama, serta keterbatasan dan batas berlaku.
4. Tambahkan satu baris putusan di akhir tiap paper: masuk, keluar, atau belum diputuskan, dengan satu kalimat alasan seperti metode berulang, sampel terlalu sempit, atau simpulan sudah usang.
5. Setelah matriks lengkap, kelompokkan berdasarkan tema, misalnya arsitektur model, augmentasi data, dan evaluasi, lalu beri ringkasan pembanding dua sampai tiga kalimat untuk setiap kelompok.

## Aturan keluaran

- Pakai markdown, dan pecah tabel panjang menjadi beberapa kelompok. Sertakan DOI setiap paper agar mudah ditelusuri.
- Kolom simpulan hanya berisi apa yang diklaim paper itu sendiri, tanpa penilaian model. Penilaian model masuk kolom keterbatasan.
- Bila abstrak dan full text berlawanan, full text yang dipakai, dan pertentangannya ditandai.
- Tutup dengan pernyataan cakupan: berapa paper yang tercakup, kata pencarian, tanggal pencarian, dan bagian mana yang tidak tercakup.

## Catatan pelaksanaan

- Untuk 50 paper ke atas, kerjakan bertahap, sekitar 10 paper per putaran, agar keluarannya tidak terlalu panjang.
- Dalam satu sesi, matriks bisa ditambah bertahap. Paper baru cukup menambah baris, tidak perlu membaca ulang semuanya.
- Ini alat penyaringan, bukan penulis tinjauan. Narasi tinjauan ditulis terpisah dan setiap kalimatnya harus bisa dipetakan ke baris matriks.
