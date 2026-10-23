# Daftar Periksa Kesalahan Logika

## Format penandaan

Setiap temuan ditulis dengan empat unsur:

```
Letak: bagian X paragraf Y (kutip kalimat awalnya)
Jenis: nama jenisnya
Alasan: satu kalimat jelas tentang titik mana pada rantai argumen yang putus
Saran perbaikan: bagaimana paragraf itu ditulis agar berdiri
```

Tandai hanya yang pasti. Yang dicurigai tapi belum yakin masuk bagian "belum pasti" di akhir laporan, dengan alasan kecurigaannya, dan tidak dipaksakan. Hitung frekuensi setiap jenis dan letakkan distribusinya di awal laporan.

## 1. Struktur argumen

- Argumen melingkar: simpulan sudah tersembunyi di premis, argumen berputar kembali ke titik awal.
- Orang-orangan sawah: pendapat lawan diubah menjadi versi yang lebih lemah lalu diserang.
- Dilema palsu: hanya dua pilihan disodorkan, padahal ada jalan tengah dan pilihan ketiga.
- Argumen lereng: ditarik dari A ke B lalu ke Z, tanpa bukti mandiri di setiap langkah.
- Menyandarkan pada otoritas: "didukung tokoh atau perusahaan besar" dipakai sebagai bukti kebenaran. Otoritas hanya menaikkan dugaan awal, bukan menggantikan argumen.
- Menyandarkan pada kebaruan: "kami memakai deep learning atau model besar" dianggap sebagai kontribusi.
- Menyandarkan pada tradisi: "dari dulu begitu" dipakai sebagai bukti kebenaran.

## 2. Bukti

- Generalisasi berlebihan: simpulan umum ditarik dari sampel kecil atau satu dataset.
- Bias penyintas: hanya sampel yang berhasil dihitung, misalnya hanya kasus sukses yang diwawancarai ulang.
- Memilih bukti: hanya eksperimen yang mendukung dilaporkan, hasil yang berlawanan tidak disebut.
- Bukti anekdotal: satu cerita kasus menggantikan bukti statistik.
- Kontaminasi sampel: training dan test saling tumpang tindih atau terjadi kebocoran data, tetapi performa tetap dilaporkan.

## 3. Statistik

- Korelasi dianggap kausalitas: "A berkorelasi dengan B" langsung ditulis "A menyebabkan B", tanpa bukti mekanisme, intervensi, atau urutan waktu.
- Arah kausalitas terbalik: B menyebabkan A, tetapi ditulis A menyebabkan B.
- p-hacking: uji atau pemotongan data diganti berulang sampai p di bawah 0,05, lalu berhenti.
- Banyak uji tanpa koreksi: N uji dijalankan tanpa koreksi seperti Bonferroni, tetapi signifikansi dilaporkan pada ambang 0,05.
- Effect size diabaikan: hanya nilai p dilaporkan, tanpa effect size dan interval kepercayaan.
- Bias publikasi: "di literatur semuanya signifikan" dipakai sebagai bukti, hasil negatif yang tidak terbit diabaikan.
- Salah membaca regresi ke rata-rata: penurunan wajar dari nilai ekstrem dianggap sebagai efek intervensi.

## 4. Penyajian

- Definisi kabur: konsep inti seperti "cerdas" atau "tangguh" tidak pernah diberi definisi operasional di seluruh teks.
- Pergeseran konsep: satu kata berubah makna antara bagian awal dan akhir argumen.
- Analogi tidak sah: objek pembanding tidak berbagi sifat kunci, sehingga analoginya runtuh.
- Tidak bisa dipalsukan: simpulan tetap "benar" apa pun buktinya.
- Menyandarkan pada ketidaktahuan: "belum ada yang membuktikan salah" dipakai sebagai bukti "benar".

## Cara menjalankan

1. Baca seluruh teks dulu dan tandai paragraf mana saja yang berisi argumen, baru bandingkan dengan daftar periksa. Jangan mencari-cari kesalahan agar daftar terpenuhi.
2. Satu paragraf bisa kena beberapa jenis sekaligus; tandai masing-masing.
3. Di laporan, pisahkan "penilaian model" dari "kutipan asli" agar pengguna bisa memeriksa ulang.
4. Tujuannya memperlihatkan titik lemah argumen, bukan menjatuhkan paper. Saran perbaikan sama pentingnya dengan penandaan.
