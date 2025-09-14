# Zero-Trace
A lightweight Python tool to securely delete files and folders by overwriting them with random data and generating proof-of-erasure certificates.


## ✨ Features
- Wipe **single files** or all files inside a **folder/USB**.
- Overwrite with **random data** (configurable number of passes).
- **Random renaming** before deletion to hide original file names.
- Generates a **wipe certificate** with:
  - Date & time
  - Target path
  - Passes used
  - Files wiped & bytes overwritten
- Works on **Windows, Linux, MacOS** (Python 3).

---

## ⚠️ Limitations
- ❌ No raw drive/partition wiping.
- ❌ Not optimized for SSDs (TRIM/Secure Erase required).
- ❌ Cannot wipe locked/system files while they are in use.
- ❌ Slower for very large data (multiple passes).
- ❌ Basic certificate (not compliance-ready for GDPR/HIPAA).

---

## 🚀 Future Scope
- Add **GUI interface** (Tkinter or PyQt).
- Add **free-space wipe** (cover deleted files in empty space).
- Support **DoD/NIST/Gutmann wipe algorithms**.
- Better **certificate reporting** (serial numbers, user info, compliance tags).
- Add **automation/scheduling** (wipe at fixed intervals).

---

## ▶️ Installation & Usage

### Requirements
- Python 3.x
- Standard libraries (`os`, `time`, `random`, `string`)

### Run
```bash
python main.py



#### Example Output #####
=== Secure Data Wiper ===
1. Wipe File
2. Wipe Folder

Enter choice (1/2): 1
Enter target file or folder path: examples/demo_folder/secret.txt
How many passes (recommended: 3): 3
WARNING: This will permanently destroy data. Type YES to continue: YES

[File] Pass 1/3 - Overwriting secret.txt...
Progress: 57%
[File] Pass 2/3 - Overwriting secret.txt...
Progress: 100%
[File] Pass 3/3 - Overwriting secret.txt...
Progress: 100%

✅ File wiped: secret.txt
📜 Certificate saved as wipe_certificate_1694523456.txt



### Example Certificate ###
=== Secure Wipe Certificate ===
Date: 2025-09-12 14:33:21
Target: examples/demo_folder/secret.txt
Passes: 3
Files wiped: 1
Bytes overwritten: 2.45 MB
Status: SUCCESS

