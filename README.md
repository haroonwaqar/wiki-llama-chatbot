🧠 Wiki-LLaMA Chatbot

Wiki-LLaMA Chatbot GUI is a simple desktop chatbot that lets users ask questions and receive answers either from:

🌐 Wikipedia for factual, real-time information
🦙 LLaMA model (via Together API) for conversational, AI-generated responses
You can manually switch between Wikipedia and LLaMA inside the code. The chatbot features a Tkinter-based graphical user interface (GUI).

💡 Features

Chatbot-style interface built with Tkinter
Dual-mode support: Wikipedia API and Together API (LLaMA models)
Simple toggle by editing a flag in the code
Neatly formatted answer display with scrollable output

🔧 Technologies Used

🐍 Python 3
🧠 Together API
🌐 wikipedia
🪟 Tkinter (Python’s built-in GUI library)

🚀 Getting Started

1. Clone the Repository
git clone https://github.com/your-username/wiki-llama-chatbot-gui.git
cd wiki-llama-chatbot-gui

2. Install Dependencies
pip install wikipedia together requests

3.🔐 API Setup
Sign up on Together AI.
Get your API key.
Open the script and set your key:
os.environ ["TOGETHER_API_KEY"] = "your_api_key_here"

🔁 Switching Between Wikipedia and LLaMA
In the code file:
  Function "send_message" uses Wikipedia to answer the question
  Function "t_send_message" uses LLaMa to answer the question

▶️ Running the App
python ChatBot_Project.py
A window will appear where you can enter your question and view the chatbot's response.
