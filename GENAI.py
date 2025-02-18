import pandas as pd
import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from langchain.llms import AzureOpenAI

# Dictionary mapping LLM names to classes
LLM_CLASSES = {
    "OpenAI": OpenAI,
    "AzureOpenAI": AzureOpenAI,
    "HuggingFaceHub": HuggingFaceHub,
}

class GenerativeAI:
    def __init__(self, data):
        self.data = data

    def display(self):
        col1, col2 = st.columns([1, 2], gap="medium")

        with col1:
            llm_choice = st.selectbox("Select an LLM", ["Select..."] + list(LLM_CLASSES.keys()))
            api_key = None
            prompt = None
            response = None

            if llm_choice != "Select...":
                api_key = st.text_input("Enter API Key", type="password")
                if api_key:
                    prompt = st.text_area("Enter Prompt")
                    if st.button("Submit", use_container_width=True):
                        llm_instance = LLM_CLASSES[llm_choice](openai_api_key=api_key)  # Initialize LLM
                        response = llm_instance(prompt)  # Query LLM using LangChain

        with col2:
            if response:
                st.subheader("LLM Response")
                st.write(response)

