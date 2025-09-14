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
