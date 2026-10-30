# 🤖 Chitti AI – Personality-Based AI Chatbot

An interactive AI chatbot built using **Python, Streamlit, LangChain, and Groq API**. Chitti AI allows users to interact with an AI assistant through eight different personalities, each offering a unique conversational experience.

🔗 **Live Demo:** https://chitti-ai-chatbot-kdvqbh8mwwjanw4jkrq7a7.streamlit.app/

📂 **GitHub Repository:** https://github.com/kamal1128/chitti-ai-chatbot

---

## ✨ Features

Chitti AI offers eight different AI personalities:

| Personality | Description |
|---|---|
| 😢 Sad | A sad and emotional conversational companion |
| 😊 Happy | A cheerful and positive companion |
| 🧠 Intelligent | Provides thoughtful and informative responses |
| 👨‍🏫 Teacher | Explains concepts and helps with learning |
| 👨‍👩‍👦 Parent | Offers caring and supportive conversations |
| 😂 Funny | Responds with humor and entertainment |
| 👔 Strict Boss | Gives direct and disciplined responses |
| 🚀 Motivator | Provides encouragement and motivation |

### Additional Features

- **Personality Switching:** Switch between eight AI personalities.
- **Interactive Chat Interface:** Chat through a simple Streamlit interface.
- **Conversation History:** Maintains conversation context during the session.
- **Clear Conversation:** Reset the current chat whenever needed.
- **LLM Integration:** Generates responses using Groq API.
- **Cloud Deployment:** Accessible through Streamlit Community Cloud.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | Web application interface |
| LangChain | LLM integration and message management |
| Groq API | LLM inference |
| GPT-OSS 20B | Language model |
| Git & GitHub | Version control and source code hosting |
| Streamlit Cloud | Application deployment |

---

## ⚙️ Project Architecture

```text
              User
                |
                ▼
       Streamlit Chat Interface
                |
                ▼
       Select AI Personality
                |
                ▼
       Personality System Prompt
                |
                ▼
       Conversation History
                |
                ▼
          LangChain
                |
                ▼
             Groq API
                |
                ▼
          GPT-OSS 20B
                |
                ▼
        Generated Response
                |
                ▼
         Display in Chat UI
```

---

## 📁 Project Structure

```text
chitti-ai-chatbot/
│
├── app.py
│
├── requirements.txt
│
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
```

**Note:** `secrets.toml` is stored locally and excluded from GitHub using `.gitignore`.

---

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/kamal1128/chitti-ai-chatbot.git
```

### 2. Navigate to the project folder

```bash
cd chitti-ai-chatbot
```

### 3. Create a virtual environment

Using uv:

```bash
uv venv
```

### 4. Install dependencies

```bash
uv pip install --python .venv/Scripts/python.exe -r requirements.txt
```

### 5. Configure Groq API Key

Create a folder named `.streamlit` in the project directory.

Inside it, create `secrets.toml`:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Get your API key from:

https://console.groq.com/keys

**Important:** Never upload your API key or `secrets.toml` file to GitHub.

### 6. Run the application

```bash
.venv/Scripts/python.exe -m streamlit run app.py
```

Open your browser at:

http://localhost:8501

---

## ☁️ Deployment

Chitti AI is deployed using **Streamlit Community Cloud**.

Deployment steps:

1. Push the project to GitHub.
2. Connect the GitHub repository to Streamlit Community Cloud.
3. Configure `GROQ_API_KEY` under App Settings → Secrets.
4. Deploy the application.
5. Access Chitti AI through the public application URL.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Integrating Large Language Models into applications.
- Working with LangChain and Groq API.
- Managing conversational messages and chat history.
- Designing interactive applications using Streamlit.
- Managing API keys securely using application secrets.
- Deploying AI applications using Streamlit Community Cloud.

---

## 🔮 Future Improvements

- Add more AI personalities.
- Implement voice input and voice responses.
- Add chat history persistence.
- Support multiple language conversations.
- Improve response customization.
- Add downloadable conversation history.

---

## 👨‍💻 Author

**Sai Kamal Kandukuri**

- GitHub: https://github.com/kamal1128
- LinkedIn: https://www.linkedin.com/in/sai-kamal-kandukuri-404288305
- Portfolio: https://neon-kamal-site.lovable.app/

---

⭐ If you find this project interesting, consider giving the repository a star!
