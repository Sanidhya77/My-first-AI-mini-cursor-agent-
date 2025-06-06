# My-first-AI-mini-cursor-agent-
This is an Min cursor which can build website based on react.

# 🤖 AI Development Assistant

An interactive terminal-based AI assistant that helps you **create and manage full-stack projects** from natural language prompts. Powered by OpenAI and built for automation, it handles tasks like generating project structure, writing code, installing dependencies, running commands, and even opening the browser for preview — all with minimal human input.

---

## ✨ Features

- ✅ Generate full project structure from a single prompt
- ✅ Automatically install npm and pip dependencies
- ✅ Create frontend (HTML/CSS/JS/React) and backend (Node.js/Python) code
- ✅ Auto-launch browser preview
- ✅ Iterative chat-based workflow with follow-up handling
- ✅ Tools for reading/writing files and running shell commands
- ✅ Uses modern UI libraries like Tailwind CSS or Bootstrap
- ✅ Integrates free, contextually-relevant web images to beautify websites

---

## 📦 Project Structure

├── Tools/
│ ├── command_runner.py # For running shell/npm/pip commands
│ ├── file_open.py # File read/write logic
│ └── project_tools.py # Project scaffolding logic
├── System_Prompts.txt # System prompt for OpenAI assistant
├── main.py # Main assistant interface
├── .env # API key (OpenAI)
├── requirements.txt
└── README.md

How to make it work 
after cloning the repo create a virtual environment 
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
#Demo 
Here you can watch teh demo video https://youtu.be/3Qc8C_WyFss
source venv/bin/activate

Add your openAi key 
OPENAI_API_KEY=your_openai_key_here
in the .env file(you need to install this on the venv so do pip install dotenv 
and then run the assistant 
