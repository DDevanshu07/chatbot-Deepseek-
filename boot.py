from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import tkinter as tk
from tkinter import scrolledtext

# Define the chatbot components
templates = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="deepseek-R1:1.5b")
prompt = ChatPromptTemplate.from_template(templates)
chain = prompt | model

# Function to handle conversation
def handle_conversation():
    global context
    user_input = user_entry.get().strip()

    if not user_input:  # Ignore empty input
        return

    # Display user's message in the chat window
    chat_display.insert(tk.END, f"You: {user_input}\n")
    user_entry.delete(0, tk.END)

    # Generate the chatbot's response
    result = chain.invoke({"context": context, "question": user_input})
    bot_response = str(result)

    # Update context and display bot's response
    chat_display.insert(tk.END, f"Bot: {bot_response}\n")
    chat_display.see(tk.END)  # Auto-scroll to the latest message
    context += f"\nUser: {user_input}\nAI: {bot_response}"

# Initialize context for conversation history
context = ""

# Create the tkinter UI
root = tk.Tk()
root.title("AI Chatbot")

# Chat display (scrolled text area)
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=30, width=50, state="normal")
chat_display.pack(pady=10,side=tk.LEFT)
chat_display.insert(tk.END, "Welcome to the AI Chatbot! Type 'exit' to quit.\n")

# Input entry field
user_entry = tk.Entry(root, width=40, font=("Arial", 14))
user_entry.pack(side=tk.LEFT, padx=10, pady=40)

# Send button
send_button = tk.Button(root, text="Send", font=("Arial", 12, "bold"), command=handle_conversation)
send_button.pack(side=tk.LEFT, padx=10, pady=40)

# Run the tkinter event loop
root.mainloop()