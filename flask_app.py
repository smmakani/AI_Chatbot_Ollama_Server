import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, session
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # For session management

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked"),
        ("user", "Question:{question}")
    ]
)

# Available models
MODEL_OPTIONS = ["gemma:2b", "llama3.2:1b", "gemma3:1b"]
DEFAULT_MODEL = "gemma:2b"

@app.route('/')
def index():
    # Initialize session variables if they don't exist
    if 'response' not in session:
        session['response'] = ""
    if 'previous_question' not in session:
        session['previous_question'] = ""
    if 'selected_model' not in session:
        session['selected_model'] = DEFAULT_MODEL
    
    return render_template('index.html', 
                          response=session['response'],
                          model_options=MODEL_OPTIONS,
                          selected_model=session['selected_model'])

@app.route('/ask', methods=['POST'])
def ask():
    # Get form data
    question = request.form.get('question', '')
    selected_model = request.form.get('model', DEFAULT_MODEL)
    
    # Check if model changed
    if selected_model != session.get('selected_model', ''):
        session['response'] = ""
        session['previous_question'] = ""
    
    # Update selected model
    session['selected_model'] = selected_model
    
    # Process only if there's a question and it's different from the previous one
    if question and question != session.get('previous_question', ''):
        try:
            # Set up Ollama model
            llm = Ollama(model=selected_model)
            output_parser = StrOutputParser()
            chain = prompt | llm | output_parser
            
            # Generate response
            response = chain.invoke({"question": question})
            
            # Update session
            session['response'] = response
            session['previous_question'] = question
            
            return jsonify({
                'status': 'success',
                'response': response
            })
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500
    else:
        return jsonify({
            'status': 'no_change',
            'response': session.get('response', '')
        })

@app.route('/clear', methods=['POST'])
def clear():
    # Clear the session data
    session['response'] = ""
    session['previous_question'] = ""
    
    return jsonify({
        'status': 'success',
        'message': 'Cleared successfully'
    })

@app.route('/change_model', methods=['POST'])
def change_model():
    # Get the selected model
    selected_model = request.form.get('model', DEFAULT_MODEL)
    
    # Check if model changed
    if selected_model != session.get('selected_model', ''):
        session['response'] = ""
        session['previous_question'] = ""
        session['selected_model'] = selected_model
    
    return jsonify({
        'status': 'success',
        'message': f'Model changed to {selected_model}'
    })

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Create static directory if it doesn't exist
    os.makedirs('static', exist_ok=True)
    
    # Run the Flask app
    app.run(debug=True)