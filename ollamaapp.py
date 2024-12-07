import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

#Langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGSMITH_TOKEN')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")

#Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ('system',"you are a helpful assistance. Please respond to the question asked"),
        ('user', "Question: {question}")
         
    ]
)

# streamlit framework
st.title("OLLAMA GENAI Application")
input_text = st.text_input("What is the query?")

#Ollama gemma2 model
llm = Ollama(model = "gemma2:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))


