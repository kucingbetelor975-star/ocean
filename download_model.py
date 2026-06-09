#!/usr/bin/env python3
"""
Script untuk mengunduh model dari GitHub menggunakan Git LFS atau dari URL alternatif
Mendukung environment variable MODEL_URL untuk custom download URL
"""
import os
import subprocess
import sys
import urllib.request

MODEL_PATH = 'model/model_air.h5'

# Cek environment variable untuk custom URL
MODEL_URL = os.environ.get('MODEL_URL', None)

# URL alternatif default (akan dicoba jika MODEL_URL tidak diset)
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
            try:
                os.remove(MODEL_PATH)
            except:
                pass
            return False
    print(f"❌ Model tidak ditemukan: {MODEL_PATH}")
    return False

def download_with_git_lfs():
    """Download model menggunakan Git LFS"""
    try:
        print("📥 Mencoba mengunduh model dengan Git LFS...")
        
        # Install Git LFS jika belum ada
        subprocess.run(['git', 'lfs', 'install', '--skip-repo'], 
                      check=False, capture_output=True, timeout=30)
        
        # Pull file dari Git LFS
        result = subprocess.run(
            ['git', 'lfs', 'pull', '--include', MODEL_PATH],
            capture_output=True,
            text=True,
            timeout=180  # 3 menit timeout
        )
        
        if result.returncode == 0:
            print("✅ Git LFS pull berhasil")
            return check_model_exists()
        else:
            print(f"⚠️ Git LFS pull gagal: {result.stderr[:200]}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏱️ Git LFS timeout (file terlalu besar atau koneksi lambat)")
        return False
    except Exception as e:
        print(f"❌ Error saat menggunakan Git LFS: {str(e)[:100]}")
        return False

def download_from_url(url):
    """Download model dari URL dengan progress"""
    try:
        print(f"📥 Mengunduh model dari: {url[:80]}...")
        
        # Pastikan direktori model ada
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        
        # Download dengan progress
        downloaded_mb = [0]  # Mutable for closure
        
        def report_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            downloaded_mb[0] = downloaded / 1_000_000
            if total_size > 0:
                percent = min(downloaded * 100 / total_size, 100)
                print(f"\r📦 Progress: {percent:.1f}% ({downloaded_mb[0]:.2f} MB / {total_size/1_000_000:.2f} MB)", end='', flush=True)
            else:
                print(f"\r📦 Downloaded: {downloaded_mb[0]:.2f} MB", end='', flush=True)
        
        # Set user agent untuk bypass blocking
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')]
        urllib.request.install_opener(opener)
        
        urllib.request.urlretrieve(url, MODEL_PATH, reporthook=report_progress)
        print("\n✅ Download selesai!")
        
        return check_model_exists()
        
    except Exception as e:
        print(f"\n❌ Error saat download dari URL: {str(e)[:200]}")
        if os.path.exists(MODEL_PATH):
            try:
                os.remove(MODEL_PATH)  # Hapus file corrupted
            except:
                pass
        return False

def main():
    print("=" * 60)
    print("🌊 OceanAI Model Downloader")
    print("=" * 60)
    print()
    print("🔍 Memeriksa keberadaan model...")
    
    if check_model_exists():
        print("✅ Model siap digunakan!")
        return 0
    
    print("\n📥 Model tidak ditemukan, mencoba mengunduh...")
    print()
    
    # Prioritas 1: Jika MODEL_URL diset, gunakan itu
    if MODEL_URL:
        print(f"🌐 Environment variable MODEL_URL terdeteksi")
        print(f"   URL: {MODEL_URL[:60]}...")
        print()
        if download_from_url(MODEL_URL):
            print("✅ Model berhasil diunduh dari MODEL_URL!")
            return 0
        print("❌ Download dari MODEL_URL gagal, mencoba metode lain...")
        print()
    
    # Prioritas 2: Coba Git LFS
    if download_with_git_lfs():
        print("✅ Model berhasil diunduh via Git LFS!")
        return 0
    
    # Prioritas 3: Coba GitHub raw (kemungkinan gagal untuk LFS)
    print("\n📥 Mencoba download langsung dari GitHub...")
    if download_from_url(GITHUB_RAW_URL):
        print("✅ Model berhasil diunduh via GitHub!")
        return 0
    
    # Semua metode gagal
    print("\n" + "=" * 60)
    print("❌ GAGAL: Model tidak dapat diunduh dari sumber manapun")
    print("=" * 60)
    print()
    print("⚠️  Aplikasi akan tetap berjalan, tapi fitur prediksi tidak tersedia")
    print()
    print("💡 Solusi Manual (PALING MUDAH):")
    print()
    print("   1. Upload file model_air.h5 ke Google Drive")
    print("   2. Dapatkan shareable link dan ubah menjadi direct download:")
    print("      https://drive.google.com/uc?export=download&id=FILE_ID&confirm=t")
    print("   3. Set environment variable di Railway:")
    print("      MODEL_URL=<your_direct_download_url>")
    print("   4. Redeploy aplikasi")
    print()
    print("   Detail lengkap ada di RAILWAY_DEPLOY.md")
    print()
    print("=" * 60)
    
    # Return 0 agar aplikasi tetap berjalan
    return 0

if __name__ == '__main__':
    sys.exit(main())
