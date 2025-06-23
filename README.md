# 🧠 Auto Form Filler (Python Project)

A Python-based automation tool that **auto-fills desktop or browser forms** using data from Excel files. Designed to simplify repetitive data entry tasks like client KYC, registrations, job applications, and more.
Includes a **subproject: Auto Excel Creator** to generate test Excel sheets for quick testing.

---

## 📁 Project Structure

```
AutoFiller_Extension/
│
├── main.py                  # Main auto form filler script
├── config/
│   └── field_mapping.json   # Field coordinates or identifiers
├── profiles/
│   └── user_data.xlsx       # Excel sheet with profile data
├── assets/
│   └── sample_screenshots/  # Screenshots of forms (if needed)
│
├── AutoExcelCreator/        # Subproject to generate test Excel data
│   ├── create_excel.py
│   └── templates/
│       └── template.xlsx
│
├── README.md
└── requirements.txt
```

---

## 🚀 Features

* 📟 Auto-fill fields in desktop/browser apps using Excel input
* 📍 Field mapping using pixel coordinates or image matching
* ⏱️ Adjustable typing speed and delay between actions
* 📄 Supports multiple user profiles from a single Excel
* 🧪 Includes Auto Excel Creator for quick testing
* 📦 Portable and lightweight (no browser extension required)

---

## 🔧 Technologies Used

* `Python 3.8+`
* `PyAutoGUI` – For keyboard/mouse automation
* `pandas` – To read Excel files
* `openpyxl` – Excel operations
* `time`, `json`, `os` – Utility modules
* `opencv-python` (optional) – For GUI image detection
* `tkinter` (optional) – If GUI interface is added

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/AutoFiller_Extension.git
   cd AutoFiller_Extension
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### 🧠 Auto Form Filler

```bash
python main.py
```

* Select profile and target window (if applicable)
* The script will auto-fill form fields using preconfigured mappings

### 📄 Auto Excel Creator

```bash
cd AutoExcelCreator
python create_excel.py
```

* Generates a sample Excel sheet with dummy data for testing autofill

---

## 🧠 Configuration

* Customize `config/field_mapping.json` with field coordinates or form structure.
* Add more test data in `profiles/user_data.xlsx`
* Set delays and typing behavior in `main.py` as per your screen speed.

---

## 🔐 Security Note

This tool runs **locally only** and doesn't store or transmit data externally.

---

## 📄 License

MIT License – use freely with credit.

---

## ✨ TODO / Future Plans

* GUI interface for field mapping
* Auto-detect window and fields using OCR
* Excel to PDF form auto-filler
* Chrome-specific version with Selenium

---

## 👤 Contribution

Pull requests, bug reports, or improvements are welcome!

```bash
# Fork → Edit → Pull Request 🚀
```

---

## 📧 Contact

For help or suggestions, open an [Issue](https://github.com/your-username/AutoFiller_Extension/issues) or reach out via email.

---

> Created with ❤️ to automate the boring stuff.
