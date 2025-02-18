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
            if self.operation == "Apply & Map":
                self.apply_map(col1,col2)
            if self.operation == "Aggregate":
                self.aggregate(col1,col2)
            if self.operation=="Group By":
                self.group_by(col1,col2)
                
    
    def apply(self, col1, col2):
        with col2:
            columns = st.multiselect("Select columns to apply function", self.data.columns.tolist())
            lambda_func = st.text_input("Enter lambda function", "lambda x: x")
            
            if st.button("Apply Function"):
                data=self.data
                data[f"Apply({columns})"] = data[columns].apply(eval(lambda_func))
                st.success("Function applied successfully!")
                st.session_state["allData"][f"Stage - Modifications - Apply - {axis} - {columns}"]=data
                st.dataframe(data)
    
    def apply_map(self, col1, col2):
        with col2:
            column = st.selectbox("Select a column", self.data.columns.tolist())
            unique_values = self.data[column].unique().tolist()
            selected_values = st.multiselect("Select values to map", unique_values)
            mapping_values = st.text_input("Enter mapping values (comma-separated)")
            
            if st.button("Apply Map",use_container_width=True):
                try:
                    mapping_dict = dict(zip(selected_values, mapping_values.split(',')))
                    data=self.data
                    data[column] = data[column].map(mapping_dict)
                    st.success("Mapping applied successfully!")
                    st.dataframe(data)
                    key=f"Stage - Modifications - Map - {column}"
                    st.session_state["allData"][key]=data
                except Exception as e:
                    st.error(f"Error applying map: {e}")
    
    def aggregate(self, col1, col2):
        with col2:
            columns = st.multiselect("Select columns to aggregate", self.data.columns.tolist())
            agg_funcs = st.multiselect("Select aggregation functions", ["sum", "mean", "median", "min", "max", "std", "var", "count"])
            
            if st.button("Apply Aggregation", use_container_width=True):
                try:
                    aggregated_data = self.data[columns].agg(agg_funcs)
                    st.success("Aggregation applied successfully!")
                    st.dataframe(aggregated_data)
                    key=f"Stage - Modifications - Aggregate - {columns} - {agg_funcs}"
                    st.session_state["allData"][key]=aggregated_data
                except Exception as e:
                    st.error(f"Error applying aggregation: {e}")
    
    def group_by(self, col1, col2):
        with col2:
            group_column = st.selectbox("Select column to group by", self.data.columns.tolist())
            agg_columns = st.multiselect("Select columns to aggregate", self.data.columns.tolist())
            agg_funcs = st.multiselect("Select aggregation functions", ["sum", "mean", "median", "min", "max", "std", "var", "count"])
            
            if st.button("Apply Group By", use_container_width=True):
                try:
                    grouped_data = self.data.groupby(group_column)[agg_columns].agg(agg_funcs)
                    st.success("Group By applied successfully!")
                    st.dataframe(grouped_data)
                    key=f"Stage - Modifications - Group By - {group_column} - {agg_columns} - {agg_funcs}"
                    st.session_state["allData"][key]=grouped_data
                except Exception as e:
                    st.error(f"Error applying Group By: {e}")
    
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
