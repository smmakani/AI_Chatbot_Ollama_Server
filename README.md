# Basic AI Chatbot using Ollama Server

This project combines LangChain, Ollama, and Flask to create an interactive chatbot interface.

## Prerequisites

1. **Ollama**: Install Ollama from [https://ollama.ai/](https://ollama.ai/)
2. **Python 3.8+**: Make sure you have Python 3.8 or newer installed

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd ollama-chatbot
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Ollama Models

Before running the application, download at least one model:

```bash
ollama pull gemma:2b
```

Optional: Pull additional models for more options:

```bash
ollama pull llama3.2:1b
ollama pull gemma3:1b
```

### 5. Create .env File

Create a `.env` file in the root directory with the following variables:

```
LANGCHAIN_API_KEY = ""
LANGCHAIN_PROJECT = ""
SECRET_KEY = "your_secret_key_here"  # For Flask session encryption
```

Note: LangChain API key is only needed if you want to use LangSmith for tracking.

## Running the Application

### Start the Flask Server

```bash
python app.py
```

Then open your browser and navigate to:
```
http://127.0.0.1:5000/
```

## Features

- **Model Selection**: Choose from different Ollama models
- **Responsive UI**: Clean interface with proper styling
- **Read-only Response Area**: Properly styled textarea that can't be edited
- **Clear Functionality**: Reset the conversation with a single click
- **Loading Indicator**: Visual feedback during response generation

## Troubleshooting

- **Ollama Connection**: Make sure Ollama is running in the background
- **Model Availability**: Check that the models you're trying to use are downloaded
- **Port Conflict**: If port 5000 is in use, modify the port in app.py

## Project Structure

- `app.py`: Flask application with LangChain integration
- `templates/index.html`: HTML template for the web interface
- `static/styles.css`: CSS styling for the application
- `requirements.txt`: Project dependencies
- `.env`: Environment variables

## License

No License required. Anyone is free to use the code.

## Acknowledgments

- LangChain: https://github.com/langchain-ai/langchain
- Ollama: https://ollama.ai/
- Flask: https://flask.palletsprojects.com/