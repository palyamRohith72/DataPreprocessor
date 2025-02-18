import streamlit as st
import pandas as pd
import numpy as np
import chardet

class Maths:
    def __init__(self, df):
        self.data = df
    
    def display(self):
        col1, col2 = st.columns([1, 2], gap="medium")
        col1.subheader("Please select the operations", divider='blue')
        
        options = col1.radio("Operations",
            ["Addition", "Subtraction", "Multiplication", "Division", "Floor Division", "Modulus", "Power",
             "Absolute Values", "Clip", "Correlation", "Count", "Covariance", "Cummax", "Cummin", "Cumprod", "Cumsum", 
             "Describe", "Mean", "Median", "Mode", "Variance", "Standard Deviation", "Kurtosis", "Quantile", "Rank", "Skew", "Dot"]
        )
        
        self.process_operation(col1, col2, options)
    
    def partial_dataset(self, col2):
        columns = col2.multiselect("Please select the columns", self.data.columns.tolist())
        rows = col2.radio("For rows how do you want to select", ["Continuous Rows", "Access through index values"])
        
        if rows == "Continuous Rows":
            start_index = int(col2.number_input("Start Index", 0))
            end_index = int(col2.number_input("End Index", 1))
            if columns and start_index is not None and end_index is not None:
                if col2.checkbox("Access Dataframe"):
                    return self.data.loc[start_index:end_index, columns]
            else:
                col2.info("Please provide all inputs")
        
        if rows == "Access through index values":
            indices = col2.text_input("Write indices of rows ',' separated")
            if indices and columns:
                indices = [int(x.strip()) for x in indices.split(',')]
                if col2.button("Access The Rows", use_container_width=True):
                    return self.data.loc[indices, columns]
            else:
                col2.info("Both columns and rows are required")
    
    def process_operation(self, col1, col2, operation):
        col2.subheader("Perform Operations On", divider='blue')
        options = col2.radio("Options", ["On complete Data", "On Sub portion Of data"])
        
        dataset = self.data if options == "On complete Data" else self.partial_dataset(col2)
        
        if dataset is None:
            return
        
        operation_mapping = {
            "Addition": self.addition,
            "Subtraction": self.subtraction,
            "Multiplication": self.multiplication,
            "Division": self.division,
            "Floor Division": self.floor_division,
            "Modulus": self.modulus,
            "Power": self.power,
            "Quantile": self.quantile,
            "Dot": self.dot
        }
        
        if operation in operation_mapping:
            operation_mapping[operation](col1, col2, dataset)
    
    def commonLayout(self, col2):
        otherOption = col2.selectbox("Do you want to perform binary operation with", ["A scalar value", "Data Frame"])
        
        if otherOption == "A scalar value":
            other = col2.number_input("Please enter a scalar value")
            axis = col2.selectbox("Select the axis", ["index", "columns"])
            fill_value = col2.number_input("Fill value for NaN", value=None, placeholder="Leave empty for None")
            
            if col2.button("Confirm Parameters"):
                return other, axis, fill_value if fill_value else None
        
        if otherOption == "Data Frame":
            uploaded_file = col2.file_uploader("Please upload file", type=['csv', 'xlsx'])
            if uploaded_file:
                other = self.parseFile(uploaded_file)
                axis = col2.selectbox("Select the Axis", ["index", "columns"])
                fill_value = col2.number_input("Fill value for NaN", value=None, placeholder="Leave empty for None")
                
                if col2.button("Confirm Parameters"):
                    return other, axis, fill_value if fill_value else None
        
    def parseFile(self, file):
        raw_data = file.read(10000)
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        file.seek(0)
        
        try:
            if file.name.endswith('.csv'):
                return pd.read_csv(file, encoding=encoding)
            elif file.name.endswith('.xlsx'):
                return pd.read_excel(file, engine='openpyxl')
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return None
    
    def perform_operation(self, col2, data, operation):
        other, axis, fill_value = self.commonLayout(col2)
        if other is not None and axis is not None:
            result = getattr(data, operation)(other=other, axis=axis, fill_value=fill_value)
            st.session_state.setdefault("allData", {})[f"Stage - Mathematics - {operation}"] = result
            col2.dataframe(result)
    
    def addition(self, col1, col2, data):
        self.perform_operation(col2, data, "add")
    
    def subtraction(self, col1, col2, data):
        self.perform_operation(col2, data, "sub")
    
    def multiplication(self, col1, col2, data):
        self.perform_operation(col2, data, "mul")
    
    def division(self, col1, col2, data):
        self.perform_operation(col2, data, "truediv")
    
    def dot(self, col1, col2, data):
        self.perform_operation(col2, data, "dot")
    
    def floor_division(self, col1, col2, data):
        self.perform_operation(col2, data, "floordiv")
    
    def modulus(self, col1, col2, data):
        self.perform_operation(col2, data, "mod")
    
    def power(self, col1, col2, data):
        self.perform_operation(col2, data, "pow")
    
    def quantile(self, col1, col2, data):
        self.perform_operation(col2, data, "quantile")
