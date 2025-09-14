import os
import time
import random
import string

def wipe_file(path, passes=3):
    """Wipe a single file by overwriting with random data."""
    if not os.path.isfile(path):
        print(f"❌ File not found: {path}")
        return False

    size = os.path.getsize(path)
    with open(path, "rb+") as f:
        for p in range(passes):
            print(f"[File] Pass {p+1}/{passes} - Overwriting {path}...")
            f.seek(0)
            f.write(os.urandom(size))
            f.flush()
    # Optional: rename file to random name before deleting
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    new_path = os.path.join(os.path.dirname(path), random_name)
    os.rename(path, new_path)
    os.remove(new_path)

    print(f"✅ File wiped: {path}")
    return True


def wipe_folder(path, passes=3):
    """Wipe all files inside a folder/USB path."""
    if not os.path.isdir(path):
        print(f"❌ Folder not found: {path}")
        return False

    success_count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if wipe_file(file_path, passes):
                success_count += 1

    print(f"✅ Wiped {success_count} files in folder: {path}")
    return True


def generate_certificate(target, passes):
    """Generate a simple wipe certificate (log file)."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_name = f"wipe_certificate_{int(time.time())}.txt"
    with open(log_name, "w") as log:
        log.write("=== Data Wipe Certificate ===\n")
        log.write(f"Target: {target}\n")
        log.write(f"Passes: {passes}\n")
        log.write(f"Date: {timestamp}\n")
        log.write("Status: SUCCESSFUL\n")
    print(f"📜 Certificate saved as {log_name}")


def main():
    print("=== Secure Data Wiper ===")
    print("1. Wipe File")
    print("2. Wipe Drive/USB (all files inside)")

    choice = input("Choose option (1/2): ")
    target = input("Enter file/folder path: ").strip('"')
    passes = int(input("How many passes (recommended: 3): "))

    if choice == "1":
        success = wipe_file(target, passes)
    elif choice == "2":
        success = wipe_folder(target, passes)
    else:
        print("Invalid choice.")
        return

    if success:
        generate_certificate(target, passes)


if __name__ == "__main__":
    main()
