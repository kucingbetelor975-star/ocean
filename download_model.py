"""
Script untuk mengunduh model dari GitHub menggunakan Git LFS atau dari URL alternatif
"""
import os
import subprocess
import sys
import urllib.request

MODEL_PATH = 'model/model_air.h5'
# URL alternatif - bisa dari GitHub Release, Google Drive, atau Hugging Face
GITHUB_RAW_URL = 'https://github.com/kucingbetelor975-star/ocean/raw/main/model/model_air.h5'

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
            # Hapus file pointer
            os.remove(MODEL_PATH)
            return False
    print(f"❌ Model tidak ditemukan: {MODEL_PATH}")
    return False

def download_with_git_lfs():
    """Download model menggunakan Git LFS"""
    try:
        print("📥 Mencoba mengunduh model dengan Git LFS...")
        
        # Install Git LFS jika belum ada
        subprocess.run(['git', 'lfs', 'install'], check=False, capture_output=True)
        
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

def download_from_url(url):
    """Download model dari URL dengan progress"""
    try:
        print(f"📥 Mengunduh model dari: {url}")
        
        # Pastikan direktori model ada
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        
        # Download dengan progress
        def report_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            percent = min(downloaded * 100 / total_size, 100)
            print(f"\rProgress: {percent:.1f}% ({downloaded / 1_000_000:.2f} MB)", end='')
        
        urllib.request.urlretrieve(url, MODEL_PATH, reporthook=report_progress)
        print("\n✅ Download selesai!")
        
        return check_model_exists()
        
    except Exception as e:
        print(f"\n❌ Error saat download dari URL: {e}")
        return False

def main():
    print("🔍 Memeriksa keberadaan model...")
    
    if check_model_exists():
        print("✅ Model siap digunakan!")
        sys.exit(0)
    
    print("\n📥 Model tidak ditemukan, mencoba mengunduh...")
    
    # Coba download dengan Git LFS terlebih dahulu
    if download_with_git_lfs():
        print("✅ Model berhasil diunduh via Git LFS!")
        sys.exit(0)
    
    # Jika Git LFS gagal, coba download langsung dari URL
    print("\n📥 Git LFS gagal, mencoba download langsung dari GitHub...")
    if download_from_url(GITHUB_RAW_URL):
        print("✅ Model berhasil diunduh via URL!")
        sys.exit(0)
    
    print("\n❌ GAGAL: Model tidak dapat diunduh dari sumber manapun")
    print("⚠️ Aplikasi akan tetap berjalan, tapi fitur prediksi tidak tersedia")
    print("\n💡 Solusi manual:")
    print("   1. Upload file model_air.h5 ke Google Drive atau Dropbox")
    print("   2. Dapatkan direct download link")
    print(f"   3. Update GITHUB_RAW_URL di {os.path.basename(__file__)}")
    sys.exit(1)

if __name__ == '__main__':
    main()
