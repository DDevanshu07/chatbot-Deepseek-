# chatbot-Deepseek-
AI chatbot using LangChain with the Ollama LLM model and a graphical user interface (GUI) built with Tkinter. The chatbot maintains a conversation history and generates responses dynamically.
Key Components:
Language Model Setup:

The script uses LangChain's OllamaLLM (deepseek-r1:1.5b) for AI-based responses.
A ChatPromptTemplate is defined to structure the chatbot's responses with a conversation history.
Chatbot Functionality:

The handle_conversation() function:
Retrieves user input from the Tkinter entry field.
Updates the chat history in the UI.
Invokes the language model to generate a response.
Displays the bot's response and maintains conversation history.
GUI Interface:

Tkinter is used to create the chatbot's graphical interface.
A ScrolledText widget displays the conversation history.
An Entry widget allows user input.
A Button triggers the chatbot response generation.
Conversation Management:

The chatbot maintains a context variable to keep track of previous exchanges.
The conversation is dynamically updated to provide more coherent responses.
How It Works:
The user enters a message in the input field and clicks the "Send" button.
The chatbot generates a response using the deepseek-r1:1.5b model.
The conversation is displayed in the chat window.
The chat history is maintained for context-aware responses.
Features:
✅ Simple AI chatbot using LangChain and Ollama
✅ GUI interface with Tkinter for easy interaction
✅ Scrollable chat history for better visibility
✅ Dynamic conversation handling
