import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if "allData" not in st.session_state:
    st.session_state["allData"]={}
class MODIFICATIONS:
    def __init__(self, data):
        self.data = data
    
    def display(self):
        st.subheader("DataFrame Operations", divider='blue')
        tab1, tab2, tab3 = st.tabs(["Perform Operations", "View Results", "Clear Memory"])
        
        with tab1:
            col1, col2 = st.columns([1, 2], border=True)
            
            with col1:
                st.subheader("Select Operation")
                self.operation = st.radio(
                    "Choose an operation:",
                    [
                        "Apply", "Apply & Map", "Aggregate", "Group By", "Sort Values", "Sort Index", "Add Suffix", "Add Prefix", 
                        "Rename", "Set Index", "Bin Numeric", "Clean Names", "Concatenate Columns", "Encode Categorical", 
                        "Expand Columns", "Factorize Columns"
                    ]
                )
            if self.operation=="Apply":
                self.apply(col1,col2)
    
    def apply(self, col1, col2):
        with col2:
            columns = st.multiselect("Select columns to apply function", self.data.columns.tolist())
            lambda_func = st.text_input("Enter lambda function", "lambda x: x")
            axis = st.selectbox("Select axis", [0, 1], index=0)
            
            if st.button("Apply Function"):
                try:
                    data=self.data
                    data[f"Apply({columns})"] = self.data[columns].apply(eval(lambda_func), axis=axis)
                    st.success("Function applied successfully!")
                    st.session_state["allData"][f"Stage - Modifications - Apply - {axis} - {columns}"]=data
                    st.dataframe(data)
                 except Exception as e:
                    st.error(f"Error applying function: {e}")
    
    def apply_map(self, col1, col2):
        pass
    
    def aggregate(self, col1, col2):
        pass
    
    def group_by(self, col1, col2):
        pass
    
    def sort_values(self, col1, col2):
        pass
    
    def sort_index(self, col1, col2):
        pass
    
    def add_suffix(self, col1, col2):
        pass
    
    def add_prefix(self, col1, col2):
        pass
    
    def rename(self, col1, col2):
        pass
    
    def set_index(self, col1, col2):
        pass
    
    def bin_numeric(self, col1, col2):
        pass
    
    def clean_names(self, col1, col2):
        pass
    
    def concatenate_columns(self, col1, col2):
        pass
    
    def encode_categorical(self, col1, col2):
        pass
    
    def expand_columns(self, col1, col2):
        pass
    
    def factorize_columns(self, col1, col2):
        pass
