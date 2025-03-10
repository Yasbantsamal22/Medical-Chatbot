# 🩺 Medical Chatbot using Gemini API, Pinecone, and Flask

## 💡 Overview

This **Medical Chatbot** is an AI-driven application designed to provide users with instant and accurate medical information. It leverages **Google's Gemini API** for advanced conversational AI, **Pinecone** for efficient vector search, and **Flask** for the backend. The chatbot extracts and processes data from **"The Gale Encyclopedia of Medicine"** to offer informed responses to user queries.

---

## 🚀 Features

- ✅ AI-powered conversational medical chatbot
- ✅ Data extracted from **The Gale Encyclopedia of Medicine (PDF)**
- ✅ Vector embeddings and similarity search using **Pinecone**
- ✅ Backend API developed with **Flask**
- ✅ User-friendly web interface built with **HTML/CSS**
- ✅ Accurate and fast responses to medical queries

---

## 📂 Project Structure

```
medical-chatbot/
│
├── app.py                # Flask backend application
├── static/               # Static files (CSS, JS)
│   └── style.css         # Frontend styling
├── templates/            # HTML templates
│   └── index.html        # Main chatbot interface
├── utils/
│   ├── data_loader.py    # Script to extract and preprocess data from PDF
│   └── vector_store.py   # Pinecone vector operations (upsert, query)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Yasbantsamal22/Medical-Chatbot.git
cd medical-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add your API keys:

```env
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Prepare and Upload Data

Run the data extraction and vector upload scripts:

```bash
python utils/data_loader.py
python utils/vector_store.py
```

### 5. Run the Flask App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` to interact with the chatbot.

---

## 💻 Technologies Used

| Technology      | Purpose                                   |
|-----------------|-------------------------------------------|
| Flask           | Backend server and API                    |
| HTML/CSS        | Frontend user interface                   |
| Gemini API      | Conversational AI model                   |
| Pinecone        | Vector storage and similarity search      |
| PyPDF2 / pdfplumber | PDF data extraction                   |
| Langchain (Optional) | Integration for embeddings & chat logic |

---

## 📖 How It Works

1. **Data Extraction**: Medical content is extracted from **The Gale Encyclopedia of Medicine (PDF)** and preprocessed.
2. **Embedding & Storage**: Text data is converted into vector embeddings and stored in **Pinecone** for similarity search.
3. **User Interaction**: Users input queries through a web interface.
4. **Query Processing**: The app fetches relevant information from Pinecone and crafts a context-aware response using **Gemini API**.
5. **Response Delivery**: The chatbot responds with concise and accurate medical information.

---

## 🛡️ Disclaimer

> **Note:** This chatbot is for **educational and informational purposes only**. It should **not** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a healthcare provider for medical concerns.

---

## 📬 Contact

For questions, suggestions, or collaborations:

- **Name**: Yasbant Samal  
- **Email**: yasbantsamal@gmail.com
- **GitHub**: https://github.com/Yasbantsamal22

---

## ⭐ Acknowledgements

- **Google Gemini API** for conversational AI
- **Pinecone** for powerful vector search
- **The Gale Encyclopedia of Medicine** for providing rich medical content
