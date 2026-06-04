# 🌊 OceanAI - AI Water Quality Detection Web App

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)

Aplikasi web cerdas berbasis **Deep Learning (InceptionV3)** untuk mendeteksi dan mengklasifikasikan kualitas air menjadi 3 kategori: **Polusi Rendah**, **Polusi Sedang**, atau **Polusi Tinggi**. Aplikasi ini dirancang dengan antarmuka *modern, clean*, dan *futuristik* yang menggabungkan elemen visual laut (*oceanic theme*) dengan teknologi AI termutakhir. Sangat cocok untuk monitoring lingkungan, proyek akademis, dan portofolio teknologi.

---

## ✨ Konsep Visual & UI/UX

Aplikasi ini mengusung tema **"Clean Futuristic Ocean Dashboard"**. Antarmuka dirancang untuk memberikan pengalaman pengguna yang *smooth* dan elegan layaknya aplikasi startup AI modern.

* **Vibe & Gaya:** Biru laut (*Dark Navy* `#0F172A`), putih awan, aksen *cyan glow* (`#38BDF8`), efek *modern glassmorphism* pada kartu-kartunya, dan gaya futuristik.
* **Animasi:** Transisi *smooth*, *floating bubble animation* secara dinamis lewat JavaScript, efek garis pemindaian (*scanning line*) AI saat memproses data, progress bar beranimasi untuk tingkat keyakinan (*confidence*), serta animasi *AOS (Animate On Scroll)*.
* **Responsivitas:** Mendukung penuh perangkat Mobile, Tablet, dan Desktop tanpa mengurangi kualitas estetika UI.

### 🎨 Palet Warna Utama
| Warna | Hex Code | Penggunaan |
| :--- | :--- | :--- |
| **Dark Navy** | `#0F172A` | Background utama halaman, footer, dan elemen gelap |
| **Ocean Blue** | `#0EA5E9` | Aksen sekunder, gelombang laut, tombol utama |
| **Cyan Glow** | `#38BDF8` | Efek *glow*, indikator AI, tombol aktif, teks sorotan |
| **Cloud White**| `#FFFFFF` | Teks utama, teks judul, *glassmorphism card* |
| **Light Aqua** | `#7DD3FC` | *Hover state*, elemen transisi |

---

## 🚀 Fitur Utama & Halaman Aplikasi

Aplikasi ini terdiri dari tiga halaman utama yang saling terintegrasi secara dinamis:

### 1. Beranda (Landing Page - `index.html`)
* **Hero Section Fullscreen:** Dilengkapi latar belakang gradient biru gelap ke cyan, teks ber-efek glow, serta tombol aksi cepat untuk memulai analisis.
* **Navbar Glassmorphism:** Navigasi lengket (*sticky*) transparan dengan efek blur latar belakang dan logo responsif yang berkedip lembut (*pulse*).
* **Tentang OceanAI:** Penjelasan umum mengenai sistem pengolahan citra digital berbasis kecerdasan buatan untuk mengklasifikasikan tingkat polusi air (Polusi Rendah, Polusi Sedang, Polusi Tinggi).
* **Fitur Utama Highlight:** 4 kartu spesifikasi visual (*Instan & Cepat, Akurasi Tinggi, Statistik Real-Time, Desain Responsif*) dengan ikon FontAwesome.
* **Tim Pengembang:** Bagian khusus yang menampilkan profil mahasiswa pengembang proyek (Azmi Novi Athaya, Rusydi Ardani, Fauzan Aldi) lengkap dengan NIM dan rincian tugas/tanggung jawab masing-masing.
* **Footer Dinamis:** Menampilkan informasi spesifikasi teknis model AI secara langsung (Jumlah layer model, total parameter model, resolusi input, dan status sistem).

### 2. Panel Analisis (Analysis Dashboard - `analisis.html`)
* **Smart Upload Panel:**
  * Fitur *Drag and Drop* interaktif serta klik untuk memilih gambar sampel air (Mendukung format `.jpg`, `.jpeg`, `.png`).
  * Live preview gambar sebelum dianalisis dengan tombol hapus (*clear*) instan.
  * Animasi *scanning line* (garis pemindai bergerak) dan status pemrosesan *"AI sedang menganalisis kualitas air..."* saat mendeteksi.
* **Result Card Overlay:**
  * Menampilkan hasil klasifikasi: **Polusi Rendah** (Hijau sukses), **Polusi Sedang** (Kuning/Oranye perhatian), atau **Polusi Tinggi** (Merah bahaya).
  * Menampilkan persentase tingkat keyakinan (*Confidence Score*) dengan *progress bar* beranimasi gradient warna.
* **AI Statistics Dashboard:**
  * **Metrik Pengujian:** Menampilkan 5 kartu statistik dinamis: *Total Pengujian*, *Polusi Rendah*, *Polusi Sedang*, *Polusi Tinggi*, dan *Rerata Confidence*.
  * **Grafik Rasio Interaktif:** Visualisasi diagram lingkaran/doughnut menggunakan **Chart.js** untuk menunjukkan perbandingan sampel air berdasarkan kategori polusinya (Polusi Rendah, Polusi Sedang, Polusi Tinggi).
  * **Tabel Riwayat Analisis:** Daftar kronologis dari pengujian terbaru (Mencakup waktu uji, nama berkas gambar, hasil deteksi dengan badge warna, dan confidence score).
  * **Fitur Reset Statistik:** Tombol untuk membersihkan seluruh riwayat pengujian dari penyimpanan sistem.

### 3. Performa Model (Model Specs Page - `performa.html`)
* **Statistik Pelatihan Model:** Informasi performa model saat ditraining (*Akurasi Model*, *Validation Accuracy*, *Epoch Training*, dan *Total Dataset*).
* **Visualisasi Kurva Training:**
  * Gambar kurva perbandingan Akurasi Training vs Validasi (*Training & Validation Accuracy Curve*).
  * Gambar kurva perbandingan Loss Training vs Validasi (*Training & Validation Loss Curve*).
* **Matriks Konfusi (Confusion Matrix):** Visualisasi matriks hasil evaluasi data uji untuk menganalisis performa *True Positive*, *True Negative*, *False Positive*, dan *False Negative*.

---

## 🛠️ Arsitektur Sistem & Alur Kerja

Aplikasi ini menggunakan arsitektur MVC sederhana berbasis Flask dengan model Deep Learning yang berjalan di sisi server (Server-side Inference).

### 1. Backend & Routing (`app.py`)
Backend Flask bertugas untuk mengatur routing halaman, mengelola database riwayat, serta menangani pemrosesan model kecerdasan buatan.
* **`/` (Index):** Mengambil metadata model dan merender halaman beranda dengan menampilkan total parameter dan layer model secara dinamis.
* **`/analisis` (Analisis):**
  * **GET:** Mengambil riwayat pengujian dari berkas JSON dan merender dashboard statistik.
  * **POST:** Menerima unggahan gambar dari frontend, menyimpannya di folder `uploads/`, memproses gambar untuk model AI, melakukan prediksi, menyimpan hasil ke riwayat, lalu merender halaman kembali dengan menampilkan kartu hasil (*overlay result*).
* **`/reset`:** Menghapus berkas basis data riwayat (`predictions.json`) untuk mereset dashboard statistik.
* **`/performa`:** Merender halaman evaluasi training model.


### 2. Pengolahan Citra & Deep Learning
* **Arsitektur Model:** InceptionV3 (Convolutional Neural Network) yang dilatih secara khusus untuk ekstraksi fitur citra air.
* **Pemrosesan Gambar (Pre-processing):**
  1. Gambar sampel air dibaca menggunakan pustaka **Pillow (PIL)**.
  2. Gambar diubah ukurannya (*resized*) menjadi resolusi input model target, yaitu `299x299` piksel.
  3. Konversi gambar menjadi array numpy.
  4. Normalisasi nilai piksel ke rentang `[0.0, 1.0]` (membagi nilai array dengan `255.0`).
  5. Penambahan dimensi batch (`np.expand_dims`) sebelum dimasukkan ke model.
* **Klasifikasi:**
  * Secara default, model mendeteksi 3 kelas keluaran (Output berukuran `3` dengan probabilitas *Softmax*).
  * Kelas ditentukan berdasarkan indeks probabilitas tertinggi (`argmax`):
    - Indeks `0`: **Polusi Tinggi** (High Pollution)
    - Indeks `1`: **Polusi Rendah** (Low Pollution)
    - Indeks `2`: **Polusi Sedang** (Mid/Normal)
  * Tingkat keyakinan (*confidence*) dihitung langsung dari nilai probabilitas kelas terpilih dikali 100%.
  * (*Fallback*): Jika model yang dimuat adalah model 1-output lama (Sigmoid), sistem otomatis menyesuaikan kembali ke logika threshold biner.

### 3. Penyimpanan Data (Persistence Layer)
* **`predictions.json`:** Berkas database JSON lokal untuk menyimpan hingga 100 riwayat transaksi pengujian terakhir (Format: nama berkas, hasil prediksi, tingkat kepercayaan, dan stempel waktu).
* **`model/model_metadata.json`:** Berkas konfigurasi JSON yang menyimpan spesifikasi performa model secara dinamis (akurasi, val_accuracy, best_epoch, total_dataset, data latih, dan konfigurasi confusion matrix).

---

## 📁 Struktur Direktori

```text
Projek citra/
│
├── app.py                  # Server Backend Flask (Controller & Core Logic)
├── Procfile                # Konfigurasi deployment server (Gunicorn)
├── requirements.txt        # Daftar pustaka & dependensi Python
├── predictions.json        # Database riwayat prediksi (Auto-generated)
│
├── model/
│   ├── model_air.h5        # Berkas fisik model Deep Learning InceptionV3
│   └── model_metadata.json # Berkas metadata spesifikasi model AI (JSON)
│
├── templates/              # Halaman Tampilan Frontend (Jinja2 Templates)
│   ├── index.html          # Halaman Beranda (Landing Page)
│   ├── analisis.html       # Halaman Dashboard Uji Sampel & Statistik
│   └── performa.html       # Halaman Evaluasi Training & Performa Model
│
├── static/                 # Aset Statis Website
│   ├── css/
│   │   └── style.css       # Custom styling CSS, efek Glassmorphism & animasi
│   ├── js/
│   │   └── main.js         # Logika interaksi UI, bubble generator, preview, & Chart.js
│   └── img/                # Aset Gambar Grafik Evaluasi & Confusion Matrix
│       ├── accuracy.png    # Gambar kurva grafik akurasi training
│       ├── loss.png        # Gambar kurva grafik loss training
│       └── confusion_matrix.png # Gambar visualisasi confusion matrix
│
└── uploads/                # Direktori penyimpanan sementara file gambar terunggah
```

---

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.8+ & JavaScript (ES6)
* **Framework Backend:** Flask (Web Server & API Gateway)
* **Engine Kecerdasan Buatan:** TensorFlow & Keras (Model InceptionV3)
* **Pemrosesan Citra:** Pillow (PIL) & NumPy
* **Desain Frontend & Styling:** Tailwind CSS (via CDN) & Custom Vanilla CSS (Glassmorphism & animations)
* **Animasi & Ikon:** AOS (Animate On Scroll) & FontAwesome v6
* **Visualisasi Grafik:** Chart.js (Responsive Canvas charts)
* **Production Server:** Gunicorn (WSGI HTTP Server)

---

## 📋 Prasyarat Sistem

Sebelum menjalankan aplikasi, pastikan komputer Anda telah memenuhi prasyarat berikut:
* **Python 3.8** atau versi di atasnya.
* **Browser Modern** (Brave, Google Chrome, Mozilla Firefox, Microsoft Edge, Safari).
* **Koneksi Internet** (Dibutuhkan untuk memuat library Tailwind CSS, Google Fonts, FontAwesome, dan AOS melalui CDN pada browser).

---

## ⚙️ Cara Instalasi & Menjalankan Aplikasi

1. **Clone atau Unduh Proyek**
   Masukkan proyek ke dalam direktori komputer Anda.
   ```bash
   cd "d:/Semester 6/Pengolahan citra/Projek citra"
   ```

2. **Buat & Aktifkan Virtual Environment (Disarankan)**
   * **Windows (PowerShell/CMD):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * **Linux / MacOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instal Dependensi**
   Instal seluruh pustaka Python yang tertera di berkas `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Server Lokal**
   Mulai jalankan server Flask:
   ```bash
   python app.py
   ```

5. **Akses Aplikasi**
   Buka peramban (browser) Anda dan akses alamat lokal:
   ```text
   http://localhost:5000
   ```

---

## 📖 Panduan Penggunaan Fitur

### 1. Melakukan Uji Kualitas Sampel Air
1. Buka tab menu **Analisis** dari Navbar.
2. Seret (*Drag & Drop*) berkas foto sampel air ke area **Smart Upload Panel**, atau cukup klik area tersebut untuk memilih file secara manual dari komputer Anda.
3. Setelah gambar terpilih, *preview* gambar akan muncul di dalam panel.
4. Klik tombol **"Proses Analisis"**.
5. Sistem akan menampilkan layar pemuatan (*loading scanner*) selama kurang lebih 1 detik.
6. Hasil prediksi (Polusi Rendah / Polusi Sedang / Polusi Tinggi) beserta persentase kecocokan (*confidence level*) akan tampil pada kartu overlay di atas panel upload.
7. Statistik pengujian, tabel riwayat, dan diagram doughnut rasio hasil pengujian di bagian bawah akan ter-update secara otomatis secara real-time.

### 2. Mengatur/Reset Riwayat Pengujian
1. Pada halaman **Analisis**, gulir ke bawah ke bagian **Statistik Pengujian**.
2. Klik tombol **"Reset Statistik"** di pojok kanan atas bagian statistik.
3. Klik tombol *OK* pada dialog konfirmasi konfirmasi peramban. Riwayat pengujian akan dikosongkan dan grafik rasio akan kembali ke keadaan kosong.
