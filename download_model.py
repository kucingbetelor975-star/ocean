"""
Script untuk mengunduh model dari GitHub menggunakan Git LFS atau dari URL alternatif
"""
import os
import subprocess
import sys

MODEL_PATH = 'model/model_air.h5'

def check_model_exists():
    """Cek apakah model sudah ada dan valid"""
    if os.path.exists(MODEL_PATH):
        file_size = os.path.getsize(MODEL_PATH)
        # Cek jika file lebih dari 1MB (bukan pointer LFS)
        if file_size > 1_000_000:
            print(f"✅ Model sudah ada: {MODEL_PATH} ({file_size / 1_000_000:.2f} MB)")
            return True
        else:
            print(f"⚠️ File model terlalu kecil ({file_size} bytes), kemungkinan pointer LFS")
            return False
    print(f"❌ Model tidak ditemukan: {MODEL_PATH}")
    return False

def download_with_git_lfs():
    """Download model menggunakan Git LFS"""
    try:
        print("📥 Mencoba mengunduh model dengan Git LFS...")
        
        # Install Git LFS jika belum ada
        subprocess.run(['git', 'lfs', 'install'], check=False)
        
        # Pull file dari Git LFS
        result = subprocess.run(
            ['git', 'lfs', 'pull', '--include', MODEL_PATH],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ Git LFS pull berhasil")
            return check_model_exists()
        else:
            print(f"⚠️ Git LFS pull gagal: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error saat menggunakan Git LFS: {e}")
        return False

def main():
    print("🔍 Memeriksa keberadaan model...")
    
    if check_model_exists():
        print("✅ Model siap digunakan!")
        sys.exit(0)
    
    print("\n📥 Model tidak ditemukan, mencoba mengunduh...")
    
    # Coba download dengan Git LFS
    if download_with_git_lfs():
        print("✅ Model berhasil diunduh!")
        sys.exit(0)
    
    print("\n❌ GAGAL: Model tidak dapat diunduh")
    print("⚠️ Aplikasi akan tetap berjalan, tapi fitur prediksi tidak tersedia")
    sys.exit(1)

if __name__ == '__main__':
    main()
