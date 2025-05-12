import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Load custom CSS
with open('custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Chatbot With Open Source Models")


# Track the previously selected model
if "previous_model" not in st.session_state:
    st.session_state.previous_model = ""

# 1. Dropdown to select model (with gemma:2b as default)
model_options = ["gemma:2b", "llama3.2:1b", "gemma3:1b"]
selected_model = st.selectbox("Select Model:", model_options, index=0)

# Clear response and input when model changes
if st.session_state.previous_model != "" and st.session_state.previous_model != selected_model:
    st.session_state.response = ""
    st.session_state.previous_question = ""
    # We can't directly clear the input text, but we'll handle this with a rerun

# Update the previous model
st.session_state.previous_model = selected_model

# 2. Text area to display response with scrollbar
if "response" not in st.session_state:
    st.session_state.response = ""

# Create a container for the response
response_container = st.container()
with response_container:
    response_area = st.text_area("Response:", value=st.session_state.response, height=300, disabled=True)

# 3. Input text for asking questions
input_text = st.text_input("Ask Question:")

## Ollama model setup
llm = Ollama(model=selected_model)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Store the previous question to avoid repeated processing
if "previous_question" not in st.session_state:
    st.session_state.previous_question = ""

# Add a clear button
col1, col2 = st.columns([4, 1])
with col2:
    if st.button("Clear"):
        st.session_state.response = ""
        st.session_state.previous_question = ""
        st.rerun()

if input_text and input_text != st.session_state.previous_question:
    with st.spinner(f"Generating response using {selected_model}..."):
        response = chain.invoke({"question": input_text})
        st.session_state.response = response
        st.session_state.previous_question = input_text
        st.rerun()  # Force a rerun to update the UI immediately