# duPy

🔁 **duPy** is a simple Python command-line tool for finding and managing duplicate files in a directory.

---

## 🚀 Features

* Detects duplicate files by comparing size and SHA-256 hash
* Simple to use CLI interface
* Optionally deletes or archives duplicates
* Minimal, fast, and dependency-free (uses standard library)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/dupy.git
cd dupy

# (Optional) create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🛠 Usage

```bash
# Scan and list duplicates
python main.py scan /path/to/folder
python main.py list /path/to/folder

# Delete duplicates (with confirmation)
python main.py delete /path/to/folder

# Delete duplicates (without confirmation)
python main.py delete /path/to/folder --yes

# Zip duplicates into archive
python main.py zip /path/to/folder
```

### 🧪 Example

```bash
$ python main.py scan ~/Downloads
Duplicate files:
----
/home/user/Downloads/photo1.jpg
/home/user/Downloads/photo1 (copy).jpg
```

---

## 📁 Project Structure

```
duPy/
├── main.py            # Entry point
├── cli.py             # CLI handler
├── duPy/
│   ├── __init__.py
│   ├── scanner.py     # Scanning and logic
│   └── file_utils.py  # File hashing utilities
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📌 Roadmap

* [ ] Add file extension filter
* [ ] Logging and verbose mode
* [ ] Export report to text or CSV
* [ ] GUI version using Tkinter or PyQt

---

## 🤝 Contributing

Contributions are welcome! Fork this repository and submit a pull request with your improvements.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.