# AI Knowledge-Base Document Assistant (RAG Chatbot)

An AI-powered document assistant that allows users to upload PDF and TXT documents and ask questions about their content through a conversational interface. The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate context-aware answers.

## 🚀 Project Overview

The AI Knowledge-Base Document Assistant is designed to make document searching and information retrieval easier. Instead of manually reading lengthy documents, users can upload their files and interact with them through a chatbot.

The system processes documents, splits their content into smaller chunks, generates embeddings, stores them in a FAISS vector database, and retrieves relevant information to answer user queries.

## ✨ Key Features

- Upload PDF and TXT documents.
- Extract text from uploaded documents.
- Split documents into manageable text chunks.
- Generate semantic embeddings using Sentence Transformers.
- Store and search document embeddings using FAISS.
- Retrieve relevant document sections based on user queries.
- Generate AI-powered answers using Google Gemini API.
- Interactive chatbot interface built with Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| PyMuPDF | PDF text extraction |
| LangChain Text Splitters | Document chunking |
| Sentence Transformers | Text embeddings |
| FAISS | Vector database and similarity search |
| Google Gemini API | AI answer generation |
| python-dotenv | Environment variable management |

## 🏗️ Project Architecture

The application follows a Retrieval-Augmented Generation (RAG) workflow:

1. **Document Upload:** User uploads PDF or TXT documents.
2. **Text Extraction:** Text is extracted from the uploaded files.
3. **Text Chunking:** Extracted content is divided into smaller chunks.
4. **Embedding Generation:** Sentence Transformers converts chunks into numerical vectors.
5. **Vector Storage:** FAISS stores the generated embeddings.
6. **Query Processing:** User submits a question through the chatbot.
7. **Information Retrieval:** Relevant document chunks are retrieved using similarity search.
8. **Answer Generation:** Google Gemini generates an answer using the retrieved context.

## 📂 Project Structure

```text
AI-Document-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── src/
│   ├── document_processor.py
│   ├── text_chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── answer_generator.py
│
├── Test Files/
│   ├── test_answer_generator.py
│   ├── test_chunker.py
│   ├── test_embeddings.py
│   ├── test_gemini.py
│   ├── test_processor.py
│   ├── test_retriever.py
│   └── test_vector_store.py
│
└── screenshots/
    ├── dashboard.png
    └── document-processing.png
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mudassir-amjid/AI-Document-Assistant_AlchemistDigitalSolution.git
```

### 2. Navigate to the Project Directory

```bash
cd AI-Document-Assistant_AlchemistDigitalSolution
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the root project directory.

Add your Gemini API key and model configuration:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.8-flash
```

Replace `your_gemini_api_key_here` with your own valid API key. Never upload your actual `.env` file or API key to GitHub.

### 7. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📸 Project Screenshots

### 1. Main Dashboard

![Main Dashboard](Screenshots/Dashboard.png)

### 2. Document Processing

![Document Processing](Screenshots/processing.png)

## 🧪 Testing

The project includes separate test scripts for the major components:

- `test_processor.py` — Document text extraction.
- `test_chunker.py` — Text chunking.
- `test_embeddings.py` — Embedding generation.
- `test_vector_store.py` — FAISS vector storage.
- `test_retriever.py` — Relevant document retrieval.
- `test_answer_generator.py` — AI answer generation.
- `test_gemini.py` — Gemini API connectivity.

Run an individual test using:

```bash
python "Test Files/test_processor.py"
```

Replace the filename to run another test.

## 🔐 Environment Variables and Security

- API keys are stored in environment variables.
- The `.env` file is excluded from Git tracking.
- The `.env.example` file provides a configuration template.
- Uploaded documents and generated vector database files are excluded from version control.

## 🎯 Project Objectives

- Demonstrate practical implementation of Retrieval-Augmented Generation (RAG).
- Build an intelligent document question-answering system.
- Explore semantic search and vector databases.
- Integrate Large Language Models with document retrieval.
- Develop a user-friendly AI application using Python and Streamlit.

## 👨‍💻 Developer

**Mudassir Amjid**

GitHub: [mudassir-amjid](https://github.com/mudassir-amjid)

## 📌 Repository

[AI Knowledge-Base Document Assistant — GitHub Repository](https://github.com/mudassir-amjid/AI-Document-Assistant_AlchemistDigitalSolution)

---

**Built with Python, Streamlit, FAISS, Sentence Transformers, and Google Gemini API.**