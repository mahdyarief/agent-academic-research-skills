# Gerbang Integritas Klaim (I-D-A-K)

Alasan berkas ini ada: kegagalan seperti ini terlihat seperti pekerjaan yang rapi. Draft yang
persentasenya dikarang terbaca sama meyakinkan dengan draft yang persentasenya benar. Sitasi
yang salah pasang terbaca sama wajar dengan sitasi yang benar. Kamu tidak bisa menangkapnya
dengan membaca lebih teliti saja, karena yang rusak bukan bahasanya, tapi hubungan antara
klaim dan buktinya. Jadi yang dibutuhkan pemeriksaan terpisah, bukan mata yang lebih awas.

## Empat gerbang

| Gerbang | Pertanyaannya | Yang dijaga |
|---|---|---|
| *I* | Apakah setiap rujukan benar-benar ada dan mengatakan apa yang kita klaim? | Integritas sitasi |
| *D* | Apakah setiap angka dan kutipan bisa dilacak ke berkas sumbernya, dengan penyebut yang benar? | Salah hitung dan hasil karangan |
| *A* | Apakah cerita kausalnya ditopang desain penelitian, bukan proksi? | Ketergantungan proksi dan artefak yang dinarasikan sebagai temuan |
| *K* | Apakah teks metode sesuai dengan yang benar-benar dikerjakan, dan kerangkanya sesuai pertanyaan? | Metode karangan dan kerangka yang terkunci |

Mnemonic: *I-D-A-K*, dibaca "tidak". Empat huruf itu urutannya, dari yang paling sering lolos
sampai yang paling sulit dilihat sendiri.

## Tujuh mode kegagalan

### I: sitasi bermasalah

*M1. Sitasi karangan.* Rujukan yang tidak ada, salah tahun atau salah venue, atau dipasangi
temuan yang tidak pernah dibuatnya.

- Setiap rujukan di draft harus resolve ke record nyata, dicek langsung, bukan dari ingatan.
- Sumber yang dikutip harus benar-benar memuat kalimat yang jadi tumpuan klaim. Buka teksnya
  dan kutip.
- Angka sampel dan temuan dikutip dengan kata-kata sumbernya sendiri, bukan parafrase yang
  menggeser makna.

### D: angka dan kutipan

*M2. Salah hitung yang lolos pemeriksaan sendiri.* Salah jumlah, salah penyebut, salah sel,
atau baris yang hilang, dan hasilnya angka yang masuk akal tapi salah.

- Untuk setiap angka di draft: berkas atau skrip mana yang menghasilkannya? Kalau tidak ada
  artefak yang tersimpan, tandai.
- Angka yang terlalu bulat atau terlalu bersih (tepat 50 persen, varians nol, jumlah identik
  di tiap subkelompok) adalah ciri khas pipeline rusak atau salah salin. Hitung ulang.
- Jumlah subkelompok dihitung terhadap basisnya sendiri, bukan terhadap seluruh sampel.

*M3. Temuan atau kutipan karangan.* Persentase atau pernyataan partisipan yang tidak pernah
ada, ditulis supaya cocok dengan cerita.

- Setiap kutipan partisipan diambil persis dari transkrip, dengan ID dan baris yang bisa
  dibuka lagi.
- Setiap persentase punya numerator dan denominator yang bisa ditemukan di data.
- "Kami mewawancarai N orang" harus cocok dengan jumlah transkrip di folder.

### A: argumen

*M4. Ketergantungan proksi.* Efek yang dilaporkan nyata, tapi digerakkan oleh pengganti, bukan
mekanisme yang diklaim.

- Apakah ada penjelasan tandingan yang ditiadakan oleh desain? Kalau tidak, klaim kausalnya
  belum ditopang penelitian ini.
- Bukti yang dipakai mengukur konstruk itu sendiri, bukan sesuatu yang hanya berkorelasi
  dengannya.
- Untuk klaim biaya: ukurannya biaya pemakaian sebenarnya, bukan kesan yang dilaporkan
  sendiri.

*M5. Artefak yang dinarasikan sebagai temuan.* Hasil tak terduga yang berasal dari kesalahan
koding, salah klasifikasi tema, atau salah entri data, lalu diceritakan sebagai temuan baru.

- Setiap klaim "menariknya", "tak terduga", atau "di luar dugaan": apakah literatur bisa
  memprediksi sebaliknya? Kalau tidak, periksa ulang datanya.
- Kejutan pada pembacaan pertama lebih berisiko daripada kejutan yang bertahan setelah
  pengodean diulang.

### K: kerangka

*M6. Metode karangan.* Bagian metode menjelaskan prosedur, sampling, atau instrumen yang
bukan yang benar-benar dikerjakan.

- Setiap rincian metode (jumlah, kerangka sampling, instrumen, periode, langkah analisis)
  harus ada di protokol atau catatan asli, bukan direkonstruksi dari apa yang wajar dilakukan.
- Tidak boleh ada langkah prapemrosesan yang penulisnya sendiri tidak bisa menunjuk jejaknya.

*M7. Kerangka terkunci.* Komitmen awal (pertanyaan penelitian, pilihan konstruk, lensa
analisis) yang sudah tidak bisa ditarik mundur oleh penelitiannya.

- Kalau kamu tahu sejak awal apa yang kamu tahu sekarang, apakah pertanyaan atau konstruknya
  akan berubah?
- Tanda-tandanya: "setelah kami sadari", "belakangan baru terlihat" di bagian pembahasan.
- Kalau ini terdeteksi, langkah jujurnya kembali ke tahap perumusan, bukan mendorong naskahnya
  terus.

## Tiga status per mode

Supaya bisa diaudit, setiap mode dicatat dengan satu status:

- *BERSIH*: bukti menyingkirkan mode ini. Catat buktinya secara singkat.
- *DICURIGAI*: pertanyaan deteksinya menghasilkan jawaban yang mengkhawatirkan. Tampilkan.
- *BUKTI KURANG*: tidak bisa dinyatakan bersih atau dicurigai tanpa masukan yang belum ada.
  Tampilkan dan tahan draft sampai terpecahkan.

Tiga mode adalah penahan keras: sitasi, salah hitung, hasil karangan, dan metode karangan.
Kalau salah satunya tidak bersih, hasilnya tidak keluar. Sisanya boleh keluar dengan catatan,
asal catatannya terlihat.

## Asal usul sumber, bukan jumlahnya

Tiga artikel yang mengutip satu siaran pers adalah *satu* bukti, bukan tiga.

- Kesesuaian membutuhkan sumber yang asal-usulnya independen. Cetak ulang siaran pers, cermin
  situs, dan kiriman agregator dihitung sebagai satu garis keturunan.
- Kalau semua sumber berasal dari satu asal, katakan itu dan turunkan keyakinan, jangan biarkan
  pengulangan terbaca sebagai replikasi.
- Sama untuk angka: kalau dua sumber menyebut angka yang sama, periksa apakah yang kedua
  mengutip yang pertama.

## Gerbang penjelasan tandingan

Sebelum klaim yang menentukan keputusan dikirim, cari bukti yang *melawannya*. Kalau tidak
ditemukan, catat itu secara eksplisit, misalnya "pada penelusuran ini tidak ditemukan sumber
yang bertentangan". Penelusuran satu arah adalah celah cakupan, bukan konfirmasi.

## Memilih kedalaman

Tentukan kedalamannya sebelum mengumpulkan, supaya tenaga sepadan dengan taruhannya.

- *Fakta cepat*: satu pencarian, satu sumber, tanpa keluaran.
- *Riset mendalam*: sintesis lintas sumber dengan keluaran yang harus tertopang; catat semua
  sumber di buku kerja.
- *Pemeriksaan repo atau tool*: metadata GitHub, README, dan riwayat rilis. Jangan menilai repo
  dari jumlah bintang saja.
- *Keluhan komunitas*: apa yang dilaporkan praktisi di forum dan issue. Beri label sebagai
  sentimen, bukan pengukuran.
- *Perbandingan atau naskah keputusan*: akhiri dengan rekomendasi beserta pertukaran yang
  diterima dan celah cakupannya, bukan tumpukan tautan.
