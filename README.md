# 💼 Career Advisor Chatbot

> An AI-powered career guidance assistant built with **Google Gemini** and **Streamlit** — providing real-time, context-aware career advice through a conversational interface.

---

## 🚀 Live Demo

> 🟢 **Deployed & Running on AWS EC2**
> Access the app at: **[http://52.65.122.199:8501](http://52.65.122.199:8501)**

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Configuration](#-configuration)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🧠 Overview

**Career Advisor Chatbot** is a conversational AI application that acts as a personal career coach. Users can ask career-related questions — from resume tips and interview preparation to job switching strategies — and receive structured, actionable advice powered by **Google's Gemini Flash** language model.

The app maintains **conversation memory** across turns, enabling context-aware follow-up responses, just like talking to a real advisor.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 **Gemini Flash LLM** | Powered by Google's latest `gemini-flash-latest` model for fast, high-quality responses |
| 🧠 **Conversation Memory** | Retains full chat history within a session for context-aware multi-turn dialogue |
| 🎯 **Domain-Specific Prompting** | Custom system prompt constrains the model strictly to career guidance topics |
| 💬 **Chat UI** | Clean, intuitive Streamlit chat interface with message bubbles |
| 🔐 **Secure API Key Handling** | API keys loaded via `.env` file — never hardcoded |
| 🧩 **Modular Architecture** | Clean separation of concerns across `api_client`, `memory`, `prompts`, and `config` modules |

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | [Streamlit](https://streamlit.io/) |
| **LLM Backend** | [Google Gemini API](https://ai.google.dev/) (`google-genai`) |
| **Language** | Python 3.10+ |
| **Config & Secrets** | `python-dotenv` |
| **Dependency Management** | `pip` + `requirements.txt` |

---

## 📁 Project Structure

```
career-advisor-chatbot/
│
├── app.py                  # Main Streamlit application entry point
│
├── backend/
│   ├── api_client.py       # Gemini API integration & response handling
│   ├── config.py           # Environment variable loading & validation
│   ├── memory.py           # Conversation history formatting & updates
│   └── prompts.py          # System prompt + dynamic prompt builder
│
├── .env                    # Secret keys (not committed to Git)
├── requirements.txt        # All Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/career-advisor-chatbot.git
cd career-advisor-chatbot
```

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate — macOS/Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
touch .env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

> 🔑 Get your free API key at [Google AI Studio](https://aistudio.google.com/app/apikey)

### 5. Run the App

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 🔄 How It Works

```
User Input
    │
    ▼
format_history()          ← Converts session history to readable text
    │
    ▼
build_prompt()            ← Injects system prompt + history + user query
    │
    ▼
get_gemini_response()     ← Sends prompt to Gemini Flash API
    │
    ▼
update_history()          ← Appends new Q&A pair to session state
    │
    ▼
Streamlit Chat UI         ← Renders full conversation history
```

### Component Breakdown

**`app.py`** — Orchestrates the full flow. Handles Streamlit session state, renders chat messages, and connects all backend modules.

**`backend/api_client.py`** — Initializes the Gemini client using the API key and exposes a clean `get_gemini_response(prompt)` function with error handling.

**`backend/prompts.py`** — Constructs a structured prompt by combining a domain-specific system instruction with the conversation history and latest user input.

**`backend/memory.py`** — Manages conversation state. `format_history()` serializes past exchanges into plain text; `update_history()` appends each new turn.

**`backend/config.py`** — Loads environment variables with `python-dotenv` and raises a clear error if the API key is missing.

---

## 🔐 Configuration

| Variable | Required | Description |
|---|---|---|
| `GEMINI_API_KEY` | ✅ Yes | Your Google Gemini API key from AI Studio |

> ⚠️ Never commit your `.env` file. Add it to `.gitignore` immediately.

```bash
echo ".env" >> .gitignore
```

---

## ☁️ Deployment — AWS EC2

The application is **live on AWS EC2** in the Asia Pacific (Sydney) region.

### Infrastructure Details

| Property | Value |
|---|---|
| **Cloud Provider** | Amazon Web Services (AWS) |
| **Service** | EC2 (Elastic Compute Cloud) |
| **Instance Name** | `genai.inference3` |
| **Instance Type** | `t3.micro` |
| **Region** | Asia Pacific — Sydney (`ap-southeast-2c`) |
| **Instance State** | 🟢 Running |
| **Public IPv4** | `52.65.122.199` |
| **Private IPv4** | `172.31.28.171` |

### Deployment Steps

**1. Launch EC2 Instance**
- Log in to AWS Console → EC2 → Launch Instance
- Choose **Ubuntu 22.04 LTS** as the AMI
- Select instance type: `t3.micro` (free tier eligible)
- Create or select an existing key pair (`.pem` file)
- Configure Security Group — open the following inbound ports:

| Port | Protocol | Purpose |
|---|---|---|
| `22` | TCP | SSH access |
| `8501` | TCP | Streamlit application |
| `80` | TCP | HTTP (optional) |

**2. SSH Into the Instance**

```bash
chmod 400 your-key.pem
ssh -i your-key.pem ubuntu@52.65.122.199
```

**3. Set Up the Environment**

```bash
# Update packages
sudo apt update && sudo apt upgrade -y

# Install Python & pip
sudo apt install python3-pip python3-venv git -y

# Clone the repository
git clone https://github.com/your-username/career-advisor-chatbot.git
cd career-advisor-chatbot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**4. Configure Environment Variables**

```bash
nano .env
# Add: GEMINI_API_KEY=your_key_here
```

**5. Run the App (Keep Running After SSH Exit)**

```bash
# Using nohup to keep the process alive
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &

# OR using tmux (recommended)
sudo apt install tmux -y
tmux new -s chatbot
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
# Press Ctrl+B then D to detach
```

**6. Access the App**

Open your browser and navigate to:
```
http://52.65.122.199:8501
```

---

## 🔮 Future Improvements

- [x] **AWS EC2 Deployment** — Live on `t3.micro` in ap-southeast-2 ✅

- [ ] **Persistent Memory** — Store conversation history across sessions using a database (SQLite / Firebase)
- [ ] **User Authentication** — Add login support for personalized chat histories
- [ ] **Resume Upload & Analysis** — Accept PDF resumes and provide tailored feedback
- [ ] **Streaming Responses** — Real-time token streaming for a more dynamic chat experience
- [ ] **Voice Input** — Speech-to-text integration for hands-free interaction
- [ ] **Docker Support** — Containerized deployment for easy cloud hosting
- [ ] **Multi-Model Support** — Toggle between Gemini, Claude, and GPT models

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
- Email: your.email@example.com

---

<p align="center">
  Built with ❤️ using Google Gemini + Streamlit
</p>
