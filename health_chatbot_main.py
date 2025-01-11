import spacy
import nltk
import requests
import gradio as gr
import time
import json

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define the OllamaLLM class
class OllamaLLM:
    def __init__(self, base_url, model):
        self.base_url = base_url
        self.model = model

    def generate(self, prompt):
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt
        }
        try:
            # Send the request to Ollama API
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Check for request errors
            
            # Log the raw response text to diagnose the issue
            print("Raw Response Text:", response.text)
            
            # Attempt to parse the response as JSON
            try:
                response_data = response.json()
            except ValueError as ve:
                print(f"Error parsing JSON: {ve}")
                return f"Error parsing JSON: {ve}"

            # Handle incomplete responses
            while not response_data.get("done", True):
                time.sleep(0.5)  # Wait for completion
                response = requests.post(url, json=payload)
                response_data = response.json()

            return response_data.get("response", "No response generated.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error communicating with Ollama: {e}")
        except ValueError as ve:
            raise Exception(f"JSON Parsing Error: {ve}")

# Initialize OllamaLLM with the base URL and model
ollama_llm = OllamaLLM(
    base_url='http://localhost:11434',  # URL of Ollama API in Docker
    model='llama3.2'  # LLaMA model in use
)

def chatbot_response(user_query):
    """
    Function to handle user queries, preprocess them, send to OllamaLLM, and return the response.
    """
    if not user_query:
        return "Error: No query provided."

    # Preprocess user input with spaCy
    doc = nlp(user_query)
    tokens = [token.text for token in doc if not token.is_stop]
    processed_query = " ".join(tokens)

    # Generate response using OllamaLLM
    try:
        generated_text = ollama_llm.generate(prompt=processed_query)
    except Exception as e:
        return f"Error communicating with OllamaLLM: {e}"

    return generated_text or "No response generated."

# Create a Gradio interface
interface = gr.Interface(
    fn=chatbot_response,         # Function to process the input
    inputs="text",               # Input field type (text box)
    outputs="text",              # Output field type (text box)
    title="Health Chatbot",      # Title of the app
    description="Ask health-related questions (not a substitute for medical advice)."
)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch()
