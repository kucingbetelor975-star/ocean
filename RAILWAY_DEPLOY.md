# 🚂 Panduan Deploy OceanAI ke Railway

## ⚠️ Masalah: File Model Terlalu Besar

File `model_air.h5` berukuran **145 MB**, terlalu besar untuk deployment standar. Railway tidak selalu support Git LFS dengan baik.

## ✅ Solusi yang Sudah Disiapkan

### Opsi 1: Deploy dengan Git LFS (Auto) ⭐ COBA INI DULU

Script `setup_model.sh` sudah disiapkan untuk otomatis download model dari Git LFS saat deployment.

**Langkah:**
1. Pastikan repository ini sudah terhubung ke Railway
2. Railway akan otomatis menjalankan `setup_model.sh` saat build
3. Script akan download model via Git LFS

### Opsi 2: Upload Model ke Google Drive (RECOMMENDED)

Jika Opsi 1 gagal, gunakan cara ini (PALING MUDAH & PASTI BERHASIL):

#### A. Upload ke Google Drive

1. Buka https://drive.google.com
2. Upload file `model/model_air.h5` (145 MB)
3. Klik kanan file → **Share** → **Anyone with the link**
4. Copy link (format: `https://drive.google.com/file/d/FILE_ID/view`)
5. Ubah menjadi direct download link:
   ```
   https://drive.google.com/uc?export=download&id=FILE_ID&confirm=t
   ```
   
   Contoh:
   - Link asli: `https://drive.google.com/file/d/1abc123XYZ/view`
   - Direct link: `https://drive.google.com/uc?export=download&id=1abc123XYZ&confirm=t`

#### B. Set Environment Variable di Railway

1. Buka project Railway Anda
2. Pergi ke **Variables** tab
3. Tambahkan variable baru:
   ```
   MODEL_URL = https://drive.google.com/uc?export=download&id=YOUR_FILE_ID&confirm=t
   ```
4. Redeploy aplikasi

### Opsi 3: Upload ke Hugging Face (Untuk Profesional)

1. Buat akun di https://huggingface.co
2. Install Hugging Face CLI:
   ```bash
   pip install huggingface_hub
   ```
3. Login:
   ```bash
   huggingface-cli login
   ```
4. Upload model:
   ```bash
   huggingface-cli upload YOUR_USERNAME/oceanai-model model/model_air.h5
   ```
5. URL model akan jadi:
   ```
   https://huggingface.co/YOUR_USERNAME/oceanai-model/resolve/main/model_air.h5
   ```
6. Set di Railway Variables:
   ```
   MODEL_URL = https://huggingface.co/YOUR_USERNAME/oceanai-model/resolve/main/model_air.h5
   ```

## 🔧 Troubleshooting

### Error: "Model AI belum terpasang"

**Penyebab:** File model tidak terdownload saat deployment

**Solusi:**
1. Cek Railway logs untuk lihat error detail
2. Gunakan Opsi 2 (Google Drive) - ini PASTI berhasil
3. Pastikan `setup_model.sh` dijalankan (cek build logs)

### Build Gagal

**Solusi:**
1. Pastikan `nixpacks.toml` ada di root project
2. Cek Railway build logs
3. Pastikan Git LFS sudah aktif:
   ```bash
   git lfs ls-files
   ```

## 📋 Checklist Deployment

- [x] Repository sudah di-push ke GitHub
- [x] Git LFS sudah dikonfigurasi
- [x] File model sudah di-track dengan LFS
- [x] `nixpacks.toml` sudah dikonfigurasi
- [x] `setup_model.sh` sudah ada
- [ ] Deploy ke Railway
- [ ] Cek build logs
- [ ] Jika gagal → gunakan Opsi 2 (Google Drive)
- [ ] Test aplikasi di URL Railway

## 🎯 Cara Cepat (5 Menit)

Jika mau yang PASTI dan CEPAT:

1. **Upload model_air.h5 ke Google Drive** (3 menit)
2. **Dapatkan direct download link**
3. **Set MODEL_URL di Railway Variables**
4. **Redeploy**
5. **DONE!** ✅

Tidak perlu repot dengan Git LFS, Hugging Face, dll. Google Drive adalah solusi termudah dan tercepat.
