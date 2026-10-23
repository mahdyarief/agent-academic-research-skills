# Rekomendasi Jurnal

Untuk alur kerja H. Sebelum mengirim, cari jurnal yang pernah menerbitkan paper dengan topik serupa, lalu susun daftar kandidat.

## Metode

1. Ambil `topics` dan `primary_topic` paper, dan cocokkan berdasarkan ID, bukan nama tampilan. Bila ID tidak tersedia, pakai pencarian teks dan nyatakan bahwa itu jalur cadangan.
2. Untuk setiap topik, agregasi sumber dengan `https://api.openalex.org/works?filter=topics.id:<TID>&group_by=primary_location.source.id&corpus=core`, dengan jendela tanggal dan jenis terbitan tetap. Bila memakai sampel works, `per_page` maksimal 100, pakai paginasi cursor, dan laporkan pemotongannya. Frekuensi 100 paper teratas berdasarkan relevansi bukan peringkat seluruh jurnal.
3. Untuk sumber yang kena beberapa topik, catat jumlah publikasi, jumlah topik yang kena, dan apakah topik utamanya kena. Ini heuristik pencocokan kandidat; skor klasifikasi topik bukan tingkat penerimaan, dan jangan menghitung Concepts bersamaan dengan Topics.
4. Periksa `type`, ISSN, ruang lingkup resmi, artikel terbaru, dan ketentuan pengiriman calon sumber. Bedakan jurnal, prosiding, dan repositori. `sources?search` hanya mencari berdasarkan nama dan bersifat pelengkap. Tidak adanya ISSN, ukuran kecil, atau penerbit yang tidak dikenal tidak cukup untuk menyebut jurnal predator; butuh bukti perilaku yang spesifik.

## Format keluaran

Untuk setiap kandidat, tulis satu baris berisi nama jurnal, topik yang cocok, jumlah paper relevan di jurnal itu, jenis dan penerbitnya, lalu catatan. Setiap jurnal diberi satu kalimat alasan: topik mana yang bertumpang tindih, plus satu atau dua contoh paper terdekat yang pernah diterbitkan.

## Batas jujur

- Peringkat SINTA, kuartil Scimago, impact factor JCR, dan daftar predator tidak ada di data OpenAlex. Nyatakan bahwa peringkat dan impact factor harus diperiksa terpisah lewat web atau akun pengguna sendiri, dan jangan dikarang.
- Pencocokan jurnal berdasarkan kedekatan topik, dan tidak menggantikan langkah membaca beberapa terbitan terakhir untuk menilai selera jurnal itu.
- Untuk konferensi, caranya sama: entri dengan `type=conference` di data sources adalah konferensi.
- Untuk jurnal Indonesia, lanjutkan dengan skill `indo-journal-scouting` yang membaca Garuda dan SINTA.
