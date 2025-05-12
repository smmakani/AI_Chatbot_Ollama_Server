# Basic AI Chatbot using Ollama Server

This project combines LangChain, Ollama, streamlit to create an interactive chatbot interfaces.

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
```

Note: LangChain API key is only needed if you want to use LangSmith for tracking.

## Running the Application

### Basic Streamlit Interface

```bash
streamlit run app.py
```


### General Issues
- Make sure Ollama is running in the background
- Check that the models you're trying to use are downloaded
- If the avatar window doesn't appear, check the terminal for error messages

## Project Structure

- `app.py`: Basic Streamlit interface
- `pygame_avatar.py`: PyGame-based 2D avatar implementation
- `pygame_app.py`: Streamlit interface with PyGame avatar integration
- `panda3d_avatar.py`: Panda3D-based 3D avatar implementation
- `panda3d_app.py`: Streamlit interface with Panda3D avatar integration
- `requirements.txt`: Project dependencies
- `.env`: Environment variables

## License

No License required. Anyone is free to use the code

## Acknowledgments

- LangChain: https://github.com/langchain-ai/langchain
- Ollama: https://ollama.ai/
- Streamlit: https://streamlit.io/
- PyGame: https://www.pygame.org/
- Panda3D: https://www.panda3d.org/