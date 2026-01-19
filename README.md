# NLP Sentence Analysis Web App

A simple **NLP-based web application** built using **Python, Flask, and NLTK** that performs sentence-level analysis such as tokenization, POS tagging, named entity recognition, and basic text statistics.

---

## 🚀 Features

* Sentence input through a web interface
* Tokenization (word-level)
* Part-of-Speech (POS) tagging
* Named Entity Recognition (NER)
* Sentence length and word count analysis
* Clean and beginner-friendly UI

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **NLP Library:** NLTK
* **Frontend:** HTML, CSS (Jinja templates)
* **Environment:** Virtualenv (optional)

---

## 📂 Project Structure

```
nlp_flask_project/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── templates/
│   └── index.html         # Frontend HTML file
└── static/                # CSS / JS files (if any)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd nlp_flask_project
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download Required NLTK Data

```python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🧠 NLP Steps Performed

1. Sentence Tokenization
2. Word Tokenization
3. POS Tagging
4. Named Entity Recognition
5. Text Statistics

---

## 📌 Use Cases

* Learning NLP fundamentals
* Academic mini-project
* Flask + NLP integration demo
* Beginner AI / Data Science project

---

## 📄 Future Enhancements

* Sentiment analysis
* Text summarization
* Word cloud visualization
* Database integration

---

## 👨‍💻 Author

**Pranjal Upadhyay**

---

## 📜 License

This project is for educational purposes only.
