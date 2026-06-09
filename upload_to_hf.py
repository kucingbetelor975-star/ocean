"""
Script untuk upload model ke Hugging Face Hub
Jalankan script ini sekali untuk upload model, lalu model bisa didownload dari Railway
"""
import os

MODEL_PATH = 'model/model_air.h5'

print("=" * 60)
print("INSTRUKSI UPLOAD MODEL KE HUGGING FACE")
print("=" * 60)
print()
print("Karena file model terlalu besar (145 MB), kita perlu upload ke")
print("hosting eksternal yang mendukung file besar seperti Hugging Face.")
print()
print("Langkah-langkah:")
print()
print("1. Buat akun gratis di https://huggingface.co")
print()
print("2. Install huggingface_hub:")
print("   pip install huggingface_hub")
print()
print("3. Login dengan token:")
print("   huggingface-cli login")
print()
print("4. Upload model dengan perintah:")
print("   huggingface-cli upload <username>/oceanai-model model/model_air.h5")
print()
print("5. Setelah upload, dapatkan URL download:")
print("   https://huggingface.co/<username>/oceanai-model/resolve/main/model_air.h5")
print()
print("6. Update URL di download_model.py dengan URL dari langkah 5")
print()
print("=" * 60)
print()
print("ALTERNATIF: Google Drive (Lebih Mudah)")
print("=" * 60)
print()
print("1. Upload model_air.h5 ke Google Drive")
print()
print("2. Klik kanan > Share > Anyone with the link")
print()
print("3. Copy link sharing, formatnya:")
print("   https://drive.google.com/file/d/FILE_ID/view")
print()
print("4. Ubah menjadi direct download link:")
print("   https://drive.google.com/uc?export=download&id=FILE_ID")
print()
print("5. Update URL di download_model.py")
print()
print("=" * 60)

# Cek ukuran file
if os.path.exists(MODEL_PATH):
    size_mb = os.path.getsize(MODEL_PATH) / (1024 * 1024)
    print(f"\n📦 File model: {MODEL_PATH}")
    print(f"📊 Ukuran: {size_mb:.2f} MB")
else:
    print(f"\n❌ File tidak ditemukan: {MODEL_PATH}")
