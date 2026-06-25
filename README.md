# 🏛 Citizen AI Assistant

An AI-powered multilingual citizen support assistant built using **Streamlit**, **Google Gemini API**, and **PDF document analysis**.

The application allows users to:

* Chat with an AI assistant in multiple Indian languages.
* Upload government documents, policies, circulars, or PDFs.
* Ask questions about uploaded documents.
* Receive answers based on document content when available.
* Fall back to Gemini AI knowledge when information is not present in the document.

---

## 🚀 Features

### 🌐 Multilingual Support

Supports multiple languages:

* English
* Telugu (తెలుగు)
* Hindi (हिन्दी)
* Tamil (தமிழ்)
* Kannada (ಕನ್ನಡ)
* Malayalam (മലയാളം)
* Bengali (বাংলা)
* Marathi (मराठी)

The assistant responds entirely in the selected language.

---

### 📄 PDF Question Answering

Users can upload PDF documents such as:

* Government Schemes
* Public Service Guidelines
* Policy Documents
* Educational Notices
* Citizen Service Manuals

The assistant extracts text from the PDF and uses it as context for answering questions.

---

### 🤖 Gemini AI Integration

Powered by Google's Gemini 2.5 Flash model for:

* Natural language understanding
* Multilingual responses
* Context-aware document question answering
* General knowledge assistance

---

### 💬 Conversational Chat Interface

* Interactive chat experience
* Persistent conversation history using Streamlit Session State
* Clean and user-friendly interface

---

## 🛠 Tech Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Core Programming Language |
| Streamlit         | Web Application Framework |
| Google Gemini API | AI Model                  |
| PyPDF             | PDF Text Extraction       |
| Generative AI     | Question Answering        |

---

## 📂 Project Structure

```text
Citizen-AI-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Narasimha2308/Citizen-Ai-Assistant.git
cd Citizen-Ai-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will launch at:

```text
http://localhost:8501
```

---

## 📋 Requirements

```text
streamlit
google-generativeai
pypdf
```

Install manually:

```bash
pip install streamlit google-generativeai pypdf
```

---

## 🔄 Workflow

1. Select preferred language.
2. Upload a PDF document (optional).
3. Ask a question.
4. System checks uploaded PDF.
5. If answer exists in document → responds using document.
6. Otherwise → responds using Gemini AI knowledge.
7. Response is returned in selected language.

---

## 📸 Sample Use Cases

### Government Services

* What documents are required for a ration card?
* Explain PM Kisan Scheme.
* What are the eligibility criteria for a pension scheme?

### Education

* Summarize this academic notice.
* Explain the uploaded policy document.

### General Assistance

* Ask questions in regional languages.
* Get multilingual explanations.

---

## Future Enhancements

* Voice Input Support
* Speech-to-Text
* Text-to-Speech
* Government API Integration
* Chat History Export
* OCR Support for Scanned PDFs
* User Authentication
* Deployment on AWS

---

## 👨‍💻 Author

**T. Narasimha**

GitHub: https://github.com/Narasimha2308

---

## License

This project is licensed under the MIT License.
