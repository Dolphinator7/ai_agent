# 🧠 AI-Powered Assistant using LangChain + OpenAI

This project demonstrates a functional AI agent built with **LangChain**, **OpenAI's Function Calling API**, and **Python**. The agent interprets user questions and autonomously executes backend tools — such as fetching weather — using ReAct-style reasoning.

It’s built to be modular, production-minded, and extensible, showcasing skills relevant to backend engineering, API integration, and modern AI applications.

---

## 🚀 Features

- ⚙️ **LangChain Agent** with `ReAct` decision-making
- 🧠 **OpenAI Function Calling** (supports GPT-4/GPT-3.5)
- 🌤️ Custom **Weather Tool** (mocked for demo)
- 📂 Modular architecture (scales with more tools)
- 🔐 Secure `.env` handling (no API keys exposed)
- 📦 Lightweight, CLI-based interface
- 🧪 Easily testable and extendable

---

## 🏗️ Project Structure
AI_Agent/
├── main.py # CLI interface to run the agent
├── .env.example # API key format (safe for sharing)
├── requirements.txt # Project dependencies
│
├── agents/
│ └── base_agent.py # Core LangChain agent logic
│
├── tools/
│ └── weather_tool.py # Custom callable function
│
├── utils/
│ └── init.py # (reserved for future utilities)
└── README.md # You're here

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Dolphinator7/ai_agent.git
cd ai_agent

## How to Use
python main.py

Then type a natural language prompt:
Ask your agent: "What's the weather in Lagos?  e.g"

## 👨‍💻 Author
Peterside Rudolph
Backend Engineer | Python Developer | AI Agent Builder
