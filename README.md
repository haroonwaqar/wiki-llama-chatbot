# **Wiki-LLaMA Chatbot**

Wiki-LLaMA Chatbot GUI is a simple desktop chatbot that lets users ask questions and receive answers either from Wikipedia for factual, real-time information or LLaMA model (via Together API) for conversational, AI-generated responses. You can manually switch between Wikipedia and LLaMA inside the code. The chatbot features a Tkinter-based graphical user interface (GUI).

## Features

Chatbot-style interface built with Tkinter
Dual-mode support: Wikipedia API and Together API (LLaMA models)
Simple toggle by editing a flag in the code
Neatly formatted answer display with scrollable output

## Technologies Used

- Python  
- Together API    
- wikipedia API  
- Tkinter (Python’s built-in GUI library)  

## Switching

- Switching Between Wikipedia and LLaMA
In the code file, Function "send_message" uses Wikipedia and Function "t_send_message" uses LLaMa to answer the questions
