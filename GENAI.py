import pandas as pd
import streamlit as st
from pandasai import *
from pandasai.llm.openai import OpenAI
from pandasai.llm.azure_openai import AzureOpenAI
from pandasai.llm.open_assistant import OpenAssistant
from pandasai.llm.starcoder import Starcoder
from pandasai.llm.google_palm import GooglePalm
from pandasai.llm.fake import FakeLLM

# Dictionary mapping LLM names to classes
LLM_CLASSES = {
    "OpenAI": OpenAI,
    "AzureOpenAI": AzureOpenAI,
    "HuggingFaceLLM": HuggingFaceLLM,
    "OpenAssistant": OpenAssistant,
    "Starcoder": Starcoder,
    "GooglePalm": GooglePalm,
    "FakeLLM": FakeLLM
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
                        llm_instance = LLM_CLASSES[llm_choice](api_token=api_key)
                        pandas_ai = PandasAI(llm_instance, conversational=False)
                        response = pandas_ai.run(self.data, prompt=prompt)
        
        with col2:
            if response:
                st.subheader("LLM Response")
                st.write(response)

# Initialize and display the app
gen_ai = GenerativeAI(df)
gen_ai.display()
