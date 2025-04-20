import os
import shutil
from pathlib import Path

# Set the directory to search — your home directory or any specific path
BASE_DIR = Path.home()

# Set size threshold (in MB)
SIZE_THRESHOLD_MB = 20

def get_size_in_mb(path):
    if path.is_file():
        return path.stat().st_size / (1024 * 1024)
    elif path.is_dir():
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.isfile(fp):
                    total += os.path.getsize(fp)
        return total / (1024 * 1024)
    return 0

def scan_for_large_files(base_path, min_size_mb):
    large_files = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".so"):
                full_path = Path(root) / file
                size_mb = get_size_in_mb(full_path)
                if size_mb > min_size_mb:
                    large_files.append((str(full_path), round(size_mb, 2)))

    return sorted(large_files, key=lambda x: x[1], reverse=True)

def scan_for_large_venvs(base_path, min_size_mb):
    large_venvs = []

    for root, dirs, files in os.walk(base_path):
        for d in dirs:
            if d == "venv":
                full_path = Path(root) / d
                size_mb = get_size_in_mb(full_path)
                if size_mb > min_size_mb:
                    large_venvs.append((str(full_path), round(size_mb, 2)))
        # Skip subdirectories if "venv" found
        dirs[:] = [d for d in dirs if d != "venv"]

    return sorted(large_venvs, key=lambda x: x[1], reverse=True)

def confirm_and_delete(paths):
    for path, size in paths:
        confirm = input(f'\n⚠️ {path} ({size} MB)\nDo you want to delete this? [y/N]: ')
        if confirm.lower() == 'y':
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                print(f"✅ Deleted: {path}")
            except Exception as e:
                print(f"❌ Failed to delete {path}: {e}")
        else:
            print("⏩ Skipped.")

if __name__ == "__main__":
    print("🔎 Scanning for large `.so` files and `venv/` directories...\n")

    so_files = scan_for_large_files(BASE_DIR, SIZE_THRESHOLD_MB)
    venvs = scan_for_large_venvs(BASE_DIR, SIZE_THRESHOLD_MB)

    if not so_files and not venvs:
        print("✅ No large files or environments found.")
    else:
        print("📦 Large .so Files Found:")
        for path, size in so_files:
            print(f"{size} MB - {path}")

        print("\n📦 Large venv Folders Found:")
        for path, size in venvs:
            print(f"{size} MB - {path}")

        if input("\nDo you want to delete any of these? [y/N]: ").lower() == 'y':
            confirm_and_delete(so_files + venvs)
        else:
            print("👋 Cleanup skipped.")