
# Health Chatbot

This project is a health chatbot application that leverages advanced natural language processing (NLP) techniques and the LLaMA 3.2 model via Ollama. The chatbot allows users to ask health-related questions and provides informative responses. Note that this chatbot is not a substitute for professional medical advice.
Disclaimer: This chatbot is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare professionals for your medical concerns.

## Features

- **User-Friendly Interface**: Built with [Gradio](https://gradio.app/), providing a simple and interactive web-based interface.
- **Natural Language Understanding**: Uses [spaCy](https://spacy.io/) and [NLTK](https://www.nltk.org/) for preprocessing and tokenization of user queries.
- **Advanced Language Model**: Integrates the LLaMA 3.2 model via the Ollama API for generating high-quality responses.
- **Streaming Responses**: Handles streamed responses efficiently to ensure a seamless user experience.

## Tech Stack

- **Python**: Core programming language for the project.
- **spaCy**: For NLP tasks like tokenization and stop-word removal.
- **NLTK**: For additional text preprocessing capabilities.
- **Gradio**: To build the user-friendly web interface.
- **Ollama**: To integrate the LLaMA 3.2 model via its Docker-hosted API.
- **JSON**: For handling API responses.

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/health-chatbot.git
   cd health-chatbot
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the Ollama API:
   - Ensure Docker is installed and running on your machine.
   - Pull the Ollama Docker image:
     ```bash
     docker pull ollama/ollama
     ```
   - Run the Docker container:
     ```bash
     docker run -d -p 11434:11434 ollama/ollama
     ```
   - Download and set up the LLaMA 3.2 model within Ollama.

5. Run the application:
   ```bash
   python app.py
   ```

6. Access the Gradio interface:
   Open your web browser and navigate to the provided URL (e.g., `http://127.0.0.1:7860`).

## Usage

1. Enter your health-related question in the text input field.
2. Press "Submit" to receive a response from the chatbot.
3. Review the response and repeat for additional queries.

## Example Questions

- "What are the symptoms of dehydration?"
- "How can I improve my sleep quality?"
- "What is a balanced diet?"
- "How much water should I drink daily?"

## File Structure

```
health-chatbot/
├── app.py             # Main application file
├── requirements.txt   # Dependencies for the project
├── README.md          # Project documentation
├── Dockerfile         # Docker configuration (optional)
└── ...                # Other supporting files
```

## Limitations

- The chatbot is for informational purposes only and should not replace professional medical advice.
- Responses are generated based on the LLaMA 3.2 model and may not always be accurate or up-to-date.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to reach out with questions or suggestions!
