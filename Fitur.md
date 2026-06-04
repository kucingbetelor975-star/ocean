# 🌊 OceanAI - Penjelasan Fitur Fungsional Setiap Halaman

Berikut adalah penjelasan fitur fungsional (logika dan kapabilitas sistem) pada aplikasi web **OceanAI** yang dipisah secara lengkap untuk setiap halaman utama:

---

## 1. 🏠 Halaman Beranda (Landing Page - `index.html`)

Halaman utama yang berfungsi sebagai pintu gerbang aplikasi untuk memperkenalkan sistem, menampilkan pengembang, serta menyajikan spesifikasi umum model.

### Fitur Fungsional:
* **Navigasi Halaman (Routing)**: Link navigasi aktif untuk berpindah antar halaman (Beranda, Analisis, dan Performa Model) melalui server Flask.
* **Informasi Sistem & Cara Kerja**: Deskripsi fungsional mengenai bagaimana model Deep Learning menganalisis karakteristik visual (warna, kejernihan, dan partikel) citra air.
* **Profil Pengembang & Peran Teknis**: Informasi detail pengembang proyek beserta spesialisasi teknis masing-masing (Desain UI/UX & Statistik, Arsitektur Server Backend, Pelatihan Model ML).
* **Daftar Teknologi Stack**: Informasi pustaka dan framework utama yang menjalankan sistem (*Flask, TensorFlow, Tailwind CSS, Chart.js*).
* **Statistik Dinamis Model (Footer Monitor)**: Menampilkan spesifikasi teknis model yang diekstrak langsung dari backend:
  * Nama Model (InceptionV3 Custom).
  * Jumlah Layer Model (dihitung dinamis dari berkas `.h5`).
  * Total Parameter Model (dihitung dinamis dari berkas `.h5`).
  * Resolusi Input Citra target (`299x299` px).
  * Status Koneksi Sistem (*Online & Ready*).

---

## 2. 📊 Halaman Panel Analisis (Analysis Dashboard - `analisis.html`)

Halaman pemrosesan utama untuk pengujian gambar sampel air, kalkulasi hasil prediksi, penyimpanan log, dan visualisasi statistik.

### Fitur Fungsional:
* **Sistem Unggah Berkas**: Menerima input berkas gambar sampel air (format `.jpg`, `.jpeg`, `.png`) melalui drag-and-drop maupun jendela pencarian file lokal.
* **Pratinjau & Pembatalan Gambar**: Menampilkan gambar terpilih di halaman sebelum proses analisis, serta opsi pembatalan/penghapusan gambar untuk menguji ulang dari awal.
* **Klasifikasi Kualitas Air (Inference AI)**: Mengirimkan gambar ke server backend, memprosesnya melalui model InceptionV3, dan menghasilkan klasifikasi kualitas air: **Polusi Rendah**, **Polusi Sedang**, atau **Polusi Tinggi**.
* **Perhitungan Skor Keyakinan (Confidence Score)**: Menghitung persentase tingkat keyakinan prediksi model AI (berkisar antara 0% hingga 100%).
* **Penyimpanan Transaksi Prediksi**: Menyimpan data pengujian (nama file gambar, hasil prediksi, tingkat keyakinan, dan waktu/timestamp pengujian) ke berkas basis data lokal JSON (`predictions.json`).
* **Akumulasi Metrik Dashboard**: Menghitung secara real-time data dari riwayat pengujian untuk disajikan pada halaman:
  * *Total Pengujian*: Jumlah kumulatif sampel air yang dianalisis.
  * *Polusi Rendah*: Jumlah sampel air berkategori polusi rendah.
  * *Polusi Sedang*: Jumlah sampel air berkategori polusi sedang.
  * *Polusi Tinggi*: Jumlah sampel air berkategori polusi tinggi.
  * *Rerata Confidence*: Rata-rata persentase tingkat keyakinan dari total pengujian.
* **Diagram Rasio Pengujian (Chart.js)**: Memetakan perbandingan persentase antara jumlah kategori polusi (Polusi Rendah, Polusi Sedang, Polusi Tinggi) dari seluruh data riwayat secara dinamis.
* **Tabel Log Riwayat**: Menyajikan daftar kronologis seluruh pengujian terbaru yang diurutkan berdasarkan waktu analisis terbaru.
* **Reset Database Riwayat**: Fitur untuk menghapus berkas penyimpanan riwayat (`predictions.json`) melalui metode POST Flask, mengembalikan seluruh statistik dan diagram ke kondisi nol.

---

## 3. ⚙️ Halaman Performa Model (Model Specs Page - `performa.html`)

Halaman evaluasi performa model training.

### Fitur Fungsional:
* **Informasi Metrik Training**: Menyajikan performa hasil training model dari berkas metadata JSON (`model_metadata.json`): *Akurasi Model*, *Validation Accuracy*, *Epoch Terbaik*, dan *Total Dataset*.
* **Visualisasi Evaluasi Training**: Menampilkan gambar grafik kurva akurasi training, kurva loss training, serta confusion matrix untuk evaluasi model.

