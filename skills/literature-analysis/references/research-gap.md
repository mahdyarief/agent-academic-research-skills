# Analisis Kepadatan Penelitian

Untuk alur kerja K. Memakai kepadatan sitasi dan topik untuk menemukan area persilangan yang jarang dikerjakan, sebagai bahan pertimbangan heuristik dalam memilih topik.

## Metode

1. Tentukan pasangan atau kombinasi topik kandidat, misalnya "graph neural network dengan manajemen risiko keuangan".
2. Bandingkan kepadatan. Untuk topik tunggal, verifikasi ID topik lewat `/topics?search=<kata topik>`, lalu baca `meta.count` dari `https://api.openalex.org/works?filter=topics.id:<TA>&per_page=1&corpus=core`. Untuk kombinasi, pakai `filter=topics.id:<TA>,topics.id:<TB>&corpus=core` yang bersifat AND, dengan `corpus`, jendela waktu, dan jenis terbitan yang sama. Kepadatan persilangan dihitung sebagai jumlah kombinasi dibagi jumlah minimum topik tunggalnya. Bila penyebutnya nol, nilainya tidak terdefinisi dan ditulis N/A; rasio kecil hanya berarti proporsi kemunculan bersama pada cakupan klasifikasi itu rendah.
3. Tren waktu: pakai query AND yang sama dengan tambahan `group_by=publication_year`, lalu lihat pertumbuhan tiga tahun penuh terakhir. Pertumbuhan tidak terdefinisi bila basisnya nol, dan tahun berjalan yang belum selesai tidak dibandingkan langsung. Basis kecil dengan pertumbuhan tinggi berarti sedang naik; basis kecil dengan pertumbuhan rendah berarti sepi, dan itu bisa berarti peluang atau jalan buntu.
4. Pemusatan sitasi: lihat distribusi `cited_by_count` paper di area persilangan. Perlu kendali atas usia publikasi dan bidang; bentuk distribusinya tidak cukup untuk menyimpulkan jenuh atau tidak.

## Format keluaran

Untuk setiap kombinasi topik, tulis kepadatan topik tunggal A dan B, jumlah persilangan, rasio kepadatan, tren tiga tahun, dan penilaian awal. Kata yang dipakai harus "kepadatan paper di area persilangan rendah", "pertumbuhannya cepat", atau "proporsi kemunculan bersamanya tinggi". Dilarang menulis "di sini ada celah", karena data hanya menunjukkan kepadatan publikasi dan tidak membuktikan belum ada yang mengerjakan atau layak dikerjakan.

## Batas jujur

- Ini heuristik kepadatan publikasi. Argumen celah penelitian yang sebenarnya harus disertai pembacaan literatur; data kepadatan hanya mempersempit wilayah.
- Pencarian topik sangat dipengaruhi pilihan kata kunci; konsep yang sama dengan kata lain memberi hasil berbeda, jadi rasio kepadatan hanya boleh dibandingkan dengan cakupan yang sama.
- Sepi tidak sama dengan kosong. Bisa jadi masalahnya tidak berdiri, datanya tidak tersedia, atau nilainya tidak jelas. Penilaian itu butuh pertimbangan manusia.
- Untuk menyusun argumen masalah dan celah yang lebih kuat, sambungkan dengan skill `research-problem-and-gap`.
