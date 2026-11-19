# 🎥 RAG YouTube Chatbot

A Retrieval-Augmented Generation (RAG) based YouTube Chatbot that allows users to ask questions about a YouTube video and receive context-aware answers using its transcript.

The project uses **LangChain, Hugging Face Embeddings, FAISS Vector Store, and OpenRouter LLM** to retrieve relevant information from video transcripts and generate accurate responses.

## 🚀 Features

- Extracts English transcripts from YouTube videos.
- Splits transcripts into smaller text chunks.
- Generates embeddings using Hugging Face.
- Stores and searches embeddings using FAISS.
- Retrieves relevant transcript sections using similarity search.
- Generates context-aware answers using OpenRouter LLM.
- Supports customizable YouTube video IDs and questions.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Framework | LangChain |
| Transcript Extraction | YouTube Transcript API |
| Text Splitting | RecursiveCharacterTextSplitter |
| Embeddings | Hugging Face |
| Vector Database | FAISS |
| LLM Integration | OpenRouter |
| Model | openai/gpt-oss-20b:free |

## 📂 Project Structure

```text
RAG-Youtube-Chatbot/
│
├── __pycache__/
├── .venv/
├── .env
├── .gitignore
├── transcript_video.py
├── youtube_Chatbot.py
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd RAG-Youtube-Chatbot
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install youtube-transcript-api langchain-core langchain-community langchain-text-splitters langchain-openai sentence-transformers faiss-cpu
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Get your API key from:

https://openrouter.ai/keys

**Note:** Never share your API key or upload your `.env` file to GitHub.

## ▶️ YouTube Video Configuration

The transcript script currently uses the following YouTube video ID:

```python
video_id = "Gfr50f6ZBvo"
```

To use another YouTube video, update the `video_id` variable in `transcript_video.py`.

## 💻 Usage

Run the chatbot using:

```bash
python youtube_Chatbot.py
```

The script performs the following operations:

1. Downloads the configured video's English transcript.
2. Splits the transcript into 1000-character chunks with a 200-character overlap.
3. Creates Hugging Face embeddings.
4. Builds a FAISS vector store.
5. Retrieves relevant transcript sections.
6. Sends the retrieved context and user question to the language model.
7. Generates an answer using OpenRouter LLM.

### Example Questions

- Can you summarize the video?
- Who is Demis?
- Is the topic of nuclear fusion discussed in this video?
- What are the main topics discussed?

To change a question, update the `question` variable in `youtube_Chatbot.py`.

## 🔄 How It Works

```text
YouTube URL
     ↓
Video Transcript
     ↓
Text Chunking
     ↓
Hugging Face Embeddings
     ↓
FAISS Vector Store
     ↓
Similarity Search
     ↓
Retrieved Context
     ↓
OpenRouter LLM
     ↓
Generated Answer
```

## 🧩 LangChain Components

| Component | Purpose |
|---|---|
| RecursiveCharacterTextSplitter | Splits the transcript into chunks. |
| HuggingFaceEmbeddings | Converts text chunks into embeddings. |
| FAISS | Stores and searches transcript embeddings. |
| PromptTemplate | Combines retrieved context with user questions. |
| ChatOpenAI | Communicates with the OpenRouter API. |
| RunnableParallel | Retrieves context and passes the question through the chain. |
| StrOutputParser | Converts the model response into a string. |

## 🤖 Current LLM Configuration

```python
model="openai/gpt-oss-20b:free"
base_url="https://openrouter.ai/api/v1"
temperature=0
```

The temperature is set to `0` to produce more deterministic responses.

## 🔐 Environment & Security

The following files should not be uploaded to GitHub:

- `.env`
- `.venv/`
- `__pycache__/`

These files are ignored through the included `.gitignore`.

## 👨‍💻 Author

**Dev Shah**


