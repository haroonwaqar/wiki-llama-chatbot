import requests
import together
import os
import tkinter as tk
from tkinter import scrolledtext

# Function to get answer from Wikipedia API
def get_wikipedia_answer(query):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "Sorry, I couldn't find an answer.")
    else: 
        return "Error fetching data. Please try again."
    
# Getting user input and sending to API and displaying results
def send_message():
    user_text = user_entry.get()
    if not user_text.strip():
        return
    
    chat_window.insert(tk.END, "You: " + user_text + "\n", "user")
    response = get_wikipedia_answer(user_text)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n", "bot")

    user_entry.delete(0, tk.END)  # Clear input field


# Set your Together AI API key
os.environ["TOGETHER_API_KEY"] = "7e12937663807444b2516081f0d8369fa58f6cb93fa3c636d6c88e28ef14e14d"

# Function to get answer from llama API
def get_llama_response(prompt):
    try:
        response = together.Complete.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  # Use a valid available model
            prompt=prompt,
            max_tokens=200
        )

        # Check the response structure before accessing keys
        if "choices" in response and response["choices"]:
            return response["choices"][0]["text"].strip()
        else:
            return "Error: Unexpected response format"

    except Exception as e:
        return f"Error: {str(e)}"

# Getting user input and sending to API and displaying results
def t_send_message():
    user_text = user_entry.get().strip()
    if not user_text:
        return

    chat_window.insert(tk.END, "You: " + user_text + "\n", "user")
    
    # Get AI-generated response
    response = get_llama_response(user_text)
    
    chat_window.insert(tk.END, "Bot: " + response + "\n\n", "bot")
    user_entry.delete(0, tk.END)  # Clear input field


# Create the main GUI window
root = tk.Tk()
root.title("ChatBot Helper")

# Chat window
chat_window = scrolledtext.ScrolledText(root, width=60, height=30, wrap=tk.WORD)
chat_window.pack(pady=20)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

# User input field
user_entry = tk.Entry(root, width=40)
user_entry.pack(pady=10)

# Send button
send_button = tk.Button(root, text="Ask", command=t_send_message)
send_button.pack()

# Run the application
root.mainloop()

