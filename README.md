# Health-Chatbot
This project is a health-focused chatbot designed to provide general information and respond to user queries. It leverages advanced natural language processing (NLP) techniques and an AI language model to process inputs and generate responses in real time.
Health Chatbot: AI-Powered Conversational Assistant
This project is a health-focused chatbot designed to provide general information and respond to user queries. It leverages advanced natural language processing (NLP) techniques and an AI language model to process inputs and generate responses in real time.

Disclaimer: This chatbot is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare professionals for your medical concerns.

Key Features
Interactive Chat Interface: A simple Gradio-based web UI for users to interact with the chatbot.
NLP Preprocessing: Uses spaCy and NLTK to preprocess and tokenize user inputs, ensuring high-quality query processing.
AI-Powered Responses: Powered by LLaMA 3.2 via Ollama for intelligent, context-aware responses.
Streamed Output Handling: Handles streamed JSON responses efficiently to ensure smooth interactions.
Customizable Model Integration: Easily adaptable to use different LLaMA models via the Ollama API.
Technologies Used
Python: Primary programming language for the project.
spaCy: For tokenization and stopword filtering during query preprocessing.
NLTK: For additional text processing capabilities.
Gradio: To create a user-friendly interface for real-time chatbot interactions.
LLaMA 3.2: Large language model used for generating responses.
Ollama: API-based framework for hosting and querying LLaMA models.
JSON: For handling API responses and processing streamed data.
Installation
Follow these steps to set up and run the project on your local machine.

Prerequisites
Python 3.7+ must be installed on your system.

Docker must be installed to run the Ollama API.

Install the required Python packages:

bash
Copy code
pip install spacy gradio requests nltk
Download and install the en_core_web_sm model for spaCy:

bash
Copy code
python -m spacy download en_core_web_sm
Ensure you have the Ollama API running with the LLaMA 3.2 model downloaded and available:

bash
Copy code
docker pull ollama/llama3.2
docker run -d -p 11434:11434 ollama/llama3.2
How to Run the Project
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/health-chatbot.git
cd health-chatbot
Run the Chatbot:

bash
Copy code
python chatbot.py
Access the Interface:
The chatbot UI will be available at http://127.0.0.1:7860 in your web browser.

Code Overview
chatbot.py
The main script that initializes the chatbot. Key components:

OllamaLLM Class: Handles API requests to the Ollama server hosting the LLaMA model.
Preprocessing Pipeline: Uses spaCy and NLTK for input tokenization and filtering.
Chatbot Functionality: Processes user queries, sends them to the LLaMA model, and streams the responses back to the user.
Gradio Interface: Provides a simple text input/output interface for users to interact with the
