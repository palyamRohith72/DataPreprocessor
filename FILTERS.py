import streamlit as st
import pandas as pd
import seaborn as sns
import janitor
if "allData" not in st.session_state:
  st.session_state["allData"]={}
class Filters:
    def __init__(self, data):
        self.data = data

    def display(self):
        tab1, tab2, tab3 = st.tabs(["Perform Operations", "View Data", "Clear Memory"])
        
        with tab1:
            col1, col2 = st.columns([1, 2], gap="medium")
            col1.subheader("Please select the operation", divider='blue')
            
            options = col1.radio("Options", [
                "Is IN", "Where", "Mask", "Query", "Is NA", "Filter Columns Is In",
                "Filter On", "Filter Date", "Filter String", "Find & Replace"
            ])
            
            if options == "Is IN":
                self.is_in(col1, col2)
            elif options == "Where":
                self.where(col1, col2)
            elif options == "Mask":
                self.mask(col1, col2)
            elif options == "Query":
                self.query(col1, col2)
            elif options == "Is NA":
                self.is_na(col1, col2)
            elif options == "Filter Columns Is In":
                self.filter_columns(col1, col2)
            elif options == "Filter On":
                self.filter_on(col1, col2)
            elif options == "Filter Date":
                self.filter_date(col1, col2)
            elif options == "Filter String":
                self.filter_string(col1, col2)
            elif options == "Find & Replace":
                self.find_replace(col1, col2)
    
   def is_in(self, col1, col2):
      choice = col2.radio("Select Scope", ["Check values in entire data", "Check values in sub data"])
     
      if choice == "Check values in entire data":
          values = col2.text_input("Enter comma-separated values")
          if values:
              values_list = [eval(val.strip()) for val in values.split(",")]
              result = self.data.isin(values_list)
              col2.dataframe(result)
      
      elif choice == "Check values in sub data":
          col_selection = col2.multiselect("Select columns", ["All"] + list(self.data.columns))
          row_selection = col2.multiselect("Select rows", ["All"] + list(self.data.index.astype(str)))
          values = col2.text_input("Enter comma-separated values")
          
          if values:
              values_list = [eval(val.strip()) for val in values.split(",")]
              selected_data = self.data.copy()
              
              if "All" not in col_selection:
                  selected_data = selected_data[col_selection]
              if "All" not in row_selection:
                  selected_data = selected_data.loc[row_selection]
              
              result = selected_data.isin(values_list)
              col2.dataframe(result)
    
    def where(self, col1, col2):
        pass
    
    def mask(self, col1, col2):
        pass
    
    def query(self, col1, col2):
        pass
    
    def is_na(self, col1, col2):
        pass
    
    def filter_columns(self, col1, col2):
        pass
    
    def filter_on(self, col1, col2):
        pass
    
    def filter_date(self, col1, col2):
        pass
    
    def filter_string(self, col1, col2):
        pass
    
    def find_replace(self, col1, col2):
        pass
