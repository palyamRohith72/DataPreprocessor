import streamlit as st
import pandas as pd
import numpy as np

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
    def partial_dataset(self,col2):
      columns=col2.multiselect("Please select the columns",self.data.columns.tolist())
      rows=col2.radio("For rows how do you want to select",["Continuous Rows","Access through index values"])
      if rows=="Continuous Rows":
        start_index=int(col2.number_input("Start Index",1))
        end_index=int(col2.number_input("End Index",1))
        if columns and start_index and end_index:
          if col2.button("Access Dataframe",use_container_width=True):
            dataset=self.data[columns].iloc[start_index:end_index,:]
            return dataset
        else:
          col2.info("Please give all all inputs")
      if rows=="Access through index values":
        indices=col2.text_input("Wriet indices of rows ',' seperated")
        if indices and columns:
          indices=[int(x.strip()) for x in indices.split(',')]
          if col2.button("Access The Rows",use_container_width=True):
            return self.data[columns].take(indices,axis=0)
        else:
          col2.info("Both columns and rows are required")
    
    def process_operation(self, col1, col2, operation):
        col2.subheader("Perform Operations On", divider='blue')
        options = col2.radio("Options", ["On complete Data", "On Sub portion Of data"])
        
        dataset = self.data if options == "On complete Data" else self.partial_data(col2)
        
        if operation == "Addition":
            self.addition(col1, col2, dataset)
        elif operation == "Subtraction":
            self.subtraction(col1, col2, dataset)
        elif operation == "Multiplication":
            self.multiplication(col1, col2, dataset)
        elif operation == "Division":
            self.division(col1, col2, dataset)
        elif operation == "Floor Division":
            self.floor_division(col1, col2, dataset)
        elif operation == "Modulus":
            self.modulus(col1, col2, dataset)
        elif operation == "Power":
            self.power(col1, col2, dataset)
        elif operation == "Quantile":
            self.quantile(col1, col2, dataset)
        elif operation == "Dot":
            self.dot(col1, col2, dataset)
    def commonLayout(self,data):
      otherOption=col2.selectbox("Do you want to perform binery operation with",["A scaler value","Data Frame"])
      if otherOption=="A scaler value":
        other=col2.number_input("Please give me a scalewr value")
        axis=col2.selectbox("Select the axis",["index","columns"])
        fill_value=col2.number_input("What value do you want to fill in NAN")
        if not fill_value:
          self.fill_value=None
        else:
          self.fill_value=fill_value
        if other and axis and fill_value:
          return other,axis,self.fill_value
        else:
          col2.info("All Parameters Shoild be selected")
      if otherOption=="Data Frame":
        other=col2.file_uploader("Please upload file",type=['csv','excel'])
        if other:
          self.other=self.parserFile(other)
        axis=col2.selectbox("Select the Axis",["index","columns"])
        fill_value=col2.number_input("What value do you want to fill In NAN")
        if not fill_value:
          self.fill_value=None
        else:
          self.fill_value=fill_value
        if other and axis and fill_value:
          return self.other,axis,fill_value
        else:
          col2.info("All Parameters Shoild be selected")
    def parseFIle(file):
      # use chardet module to detect correct encoding and reset pointer read with sucess ful encoding
      raw_data = file.read(10000)
      result = chardet.detect(raw_data)
      encoding = result['encoding']
      
      # Reset file pointer to beginning
      file.seek(0)
      
      # Read file with detected encoding
      try:
          if file.name.endswith('.csv'):
              return pd.read_csv(file, encoding=encoding)
          elif file.name.endswith('.xlsx') or file.name.endswith('.xls'):
              return pd.read_excel(file, engine='openpyxl')
          else:
              st.error("Unsupported file format. Please upload a CSV or Excel file.")
              return None
      except Exception as e:
          st.error(f"Error reading file: {e}")
          return None
        
    def addition(self, col1, col2, data):
      other,axis,fill_value=self.commonLayout(data)
      dataframe=data.add(other=other,axis=axis,fill_value=fill_value)
      st.session_state["allData"][f"Stage - Mathematics - Addition"]=datafarme
      col2.datafarme(dataframe)
    def subtraction(self, col1, col2, data):
      other,axis,fill_value=self.commonLayout(data)
      dataframe=data.sub(other=other,axis=axis,fill_value=fill_value)
      st.session_state["allData"][f"Stage - Mathematics - substraction"]=datafarme
      col2.datafarme(dataframe)
    
    def multiplication(self, col1, col2, data):
      other,axis,fill_value=self.commonLayout(data)
      dataframe=data.mul(other=other,axis=axis,fill_value=fill_value)
      st.session_state["allData"][f"Stage - Mathematics - Multiplication"]=datafarme
      col2.datafarme(dataframe)
    
    def division(self, col1, col2, data):
      other,axis,fill_value=self.commonLayout(data)
      dataframe=data.true_div(other=other,axis=axis,fill_value=fill_value)
      st.session_state["allData"][f"Stage - Mathematics - True Division"]=datafarme
      col2.datafarme(dataframe)
    
    def dot(self, col1, col2, data):
      other,axis,fill_value=self.commonLayout(data)
      dataframe=data.dot(other=other,axis=axis,fill_value=fill_value)
      st.session_state["allData"][f"Stage - Mathematics - Dot Product"]=datafarme
      col2.datafarme(dataframe)
    
    def floor_division(self, col1, col2, data):
      other,axis,fill_value=self.commonLayout(data)
      dataframe=data.floor_div(other=other,axis=axis,fill_value=fill_value)
      st.session_state["allData"][f"Stage - Mathematics - Floor Div"]=datafarme
      col2.datafarme(dataframe)
    
    def modulus(self, col1, col2, data):
      other,axis,fill_value=self.commonLayout(data)
      dataframe=data.mod(other=other,axis=axis,fill_value=fill_value)
      st.session_state["allData"][f"Stage - Mathematics - Modulous"]=datafarme
      col2.datafarme(dataframe)
    
    def power(self, col1, col2, data):
      other,axis,fill_value=self.commonLayout(data)
      dataframe=data.pow(other=other,axis=axis,fill_value=fill_value)
      st.session_state["allData"][f"Stage - Mathematics - Power"]=datafarme
      col2.datafarme(dataframe)
    
    def quantile(self, col1, col2, data):
      other,axis,fill_value=self.commonLayout(data)
      dataframe=data.quantile(other=other,axis=axis,fill_value=fill_value)
      st.session_state["allData"][f"Stage - Mathematics - Quantile"]=datafarme
      col2.datafarme(dataframe)
