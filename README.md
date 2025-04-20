# Cleaner Script

A simple Python utility to detect and optionally delete large `.so` files and virtual environments (`venv/`) that may be taking up unnecessary disk space.

---

##  Features

- Scans your home directory (or a custom path) for:
  - Large `.so` shared object files
  - Python virtual environments (`venv/` folders)
- Displays file sizes in MB
- Interactive deletion prompt for safe cleanup

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Inconsequential-24/Cleaner_script
cd Cleaner_script
```

### 2. Run the script

```bash
python3 main.py
```

---

## ⚙ Configuration

- Default scan path: your home directory
- Size threshold: 20 MB (can be changed in the script) ('SIZE_THRESHOLD_MB')

---

##  Safety

- No files are deleted automatically 
- Every deletion is confirmed via prompt (It asks you 'Y' or 'N' before deleting)
- You can modify the script to enable auto-cleaning if needed 

---

##  Sample Output

```
 Large .so Files Found:
102.3 MB - /Users/juhi/.venv/lib/python3.11/site-packages/xla_extension.so

 Large venv Folders Found:
210.5 MB - /Users/juhi/Projects/old_project/venv

Do you want to delete any of these? [y/N]:
```

---

##  License

MIT License. Do what you want, just don't blame me for deleted files ... 

---

##  Author

Made by [Juhi Dwivedi](https://github.com/Inconsequential-24) because I can manage to run out of storage even if I have 1 TB of storage.

In case of doubts, please reach out to me on LinkedIn - [juhi-dwivedi](https://www.linkedin.com/in/juhi-dwivedi/).
