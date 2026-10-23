# Bantuan Reproduksi

Untuk alur kerja L. Mencari kode dan dataset resmi sebuah paper, lalu menjalankan contoh minimalnya.

## Memilih saluran

API lama Papers with Code tidak dijadikan sandaran tetap; satu respons HTML tidak cukup untuk membuktikan layanannya mati permanen. Utamakan halaman resmi paper untuk memastikan alamat kode dan datanya, lalu pakai tiga jalur cadangan:

1. Pencarian GitHub, jalur utama: `gh search repos "<judul paper>" --limit 10` atau `gh search repos "<nama metode> <penulis pertama>"`. Prioritaskan implementasi resmi dari akun penulis, lalu repositori reproduksi dengan bintang banyak, dengan tiga penanda: jumlah bintang, tanggal commit terakhir, dan keaktifan issue.
2. Dataset di Hugging Face: pakai skill `huggingface-hub` untuk memeriksa apakah dataset yang dipakai benchmark paper tersedia publik.
3. Pencarian web: `web_search "<judul paper> official code github"`. Halaman proyek paper biasanya mencantumkan tautan repositori langsung.

## Langkah

1. Ambil arXiv ID atau DOI paper, lalu cek halaman proyek dan repositori GitHub-nya.
2. Unduh repositori, baca README, dan pastikan kebutuhan lingkungan: versi python, daftar dependensi, dan memori GPU.
3. Cari dataset dari tautan unduhan di README atau ID dataset Hugging Face. Dataset yang perlu permohonan dijelaskan apa adanya kepada pengguna.
4. Jalankan contoh minimal seperti demo atau quickstart, bukan pelatihan penuh.
5. Laporkan hasilnya. Bila berhasil, sebutkan contoh minimal lulus, lingkungan yang dipakai, dan lama waktunya. Bila gagal, sebutkan pesan galat spesifik dan langkah yang sudah dicoba, dan jangan pura-pura berhasil.

## Jebakan

- Bedakan implementasi resmi dan reproduksi pihak ketiga. Kualitas repositori pihak ketiga beragam, jadi sebutkan sumber repositori dan jumlah bintangnya saat melaporkan hasil.
- Konflik lingkungan: dependensi repositori reproduksi bisa bentrok dengan venv Hermes. Bangun virtual environment terpisah dengan uv agar lingkungan utama Hermes tidak tercemar.
- Jangan menjalankan skrip pelatihan penuh di mesin lokal dalam waktu lama karena memakan GPU. Bila pengguna ingin pelatihan penuh, jelaskan kebutuhan sumber daya dan perkiraan waktunya, lalu biarkan pengguna memutuskan.
- Lisensi data: dataset bisa dibatasi untuk nonkomersial atau perlu permohonan. Baca ketentuannya sebelum mengunduh.
