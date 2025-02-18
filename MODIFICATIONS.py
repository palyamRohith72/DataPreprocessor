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
            if self.operation=="Sort Values":
                self.sort_values(col1,col2)
            if self.operation=="Sort Index":
                self.sort_index(col1,col2)
            if self.operation=="Add Prefix":
                self.add_prefix(col1,col2)
            if self.operation=="Add Suffix":
                self.add_suffix(col1,col2)
            if self.operation=="Rename":
                self.rename(col1,col2)
                
    
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
        with col2:
            columns = st.multiselect("Select columns to sort by", self.data.columns.tolist())
            axis = st.selectbox("Select axis", [0, 1], index=0)
            ascending = st.checkbox("Sort in ascending order", value=True)
            kind = st.selectbox("Select sorting algorithm", ["quicksort", "mergesort", "heapsort", "stable"], index=0)
            na_position = st.selectbox("Select NaN position", ["last", "first"], index=0)
            ignore_index = st.checkbox("Ignore index", value=False)
            
            if st.button("Apply Sort Values", use_container_width=True):
                try:
                    sorted_data = self.data.sort_values(
                        by=columns if columns else None,
                        axis=axis,
                        ascending=ascending,
                        kind=kind,
                        na_position=na_position,
                        ignore_index=ignore_index
                    )
                    st.success("Sort applied successfully!")
                    st.dataframe(sorted_data)
                    key=f"Stage - Modifications - sort_values - Columns : {columns} - axis : {axis} - ascending : {ascending} - kind : {kind} - na_position : {na_position} - ignore_index : {ignore_index}"
                    st.sesion_state["allData"][key]=sorted_data
                except Exception as e:
                    st.error(f"Error applying Sort Values: {e}")
    
    def sort_index(self, col1, col2):
        with col2:
            columns = st.multiselect("Select columns to sort by", self.data.columns.tolist())
            axis = st.selectbox("select axis", [0, 1], index=0)
            ascending = st.checkbox("sort in ascending order", value=True)
            kind = st.selectbox("select sorting algorithm", ["quicksort", "mergesort", "heapsort", "stable"], index=0)
            na_position = st.selectbox("select NaN position", ["last", "first"], index=0)
            sort_remaining = st.checkbox("sort remaining", value=False)
            
            if st.button("Apply Sort Values", use_container_width=True):
                try:
                    sorted_data = self.data[columns].sort_index(
                        axis=axis,
                        ascending=ascending,
                        kind=kind,
                        na_position=na_position,
                        sort_remaining=sort_remaining
                    )
                    st.success("Sort applied successfully!")
                    st.dataframe(sorted_data)
                    key=f"Stage - Modifications - sort_index - Columns : {columns} - axis : {axis} - ascending : {ascending} - kind : {kind} - na_position : {na_position} - ignore_index : {sort_remaining}"
                    st.session_state["allData"][key]=sorted_data
                except Exception as e:
                    st.error(f"Error applying Sort Values: {e}")
    
    def add_suffix(self, col1, col2):
        with col2:
            columns = st.multiselect("Select columns for suffix", self.data.columns.tolist())
            suffix = st.text_input("Enter suffix to add")
            
            if st.button("Apply Add Suffix", use_container_width=True):
                try:
                    updated_data=self.data
                    updated_data = updated_data[columns].add_suffix(suffix)
                    st.success("Suffix added successfully!")
                    st.dataframe(updated_data)
                except Exception as e:
                    st.error(f"Error applying Add Suffix: {e}")
    
    def add_prefix(self, col1, col2):
        with col2:
            prefix = st.text_input("Enter prefix to add")
            
            if st.button("Apply Add Prefix", use_container_width=True):
                try:
                    updated_data = self.data.add_prefix(prefix)
                    st.success("Prefix added successfully!")
                    st.dataframe(updated_data)
                except Exception as e:
                    st.error(f"Error applying Add Prefix: {e}")
    
    def rename(self, col1, col2):
        with col2:
            # Select columns or index to rename
            rename_type = st.radio("Select Type to Rename", ("Index", "Columns"))
    
            # Input for renaming index or columns
            if rename_type == "Index":
                selected_index = st.multiselect("Select Indexes to Rename", options=self.data.index.tolist(), default=self.data.index.tolist())
                index_map = st.text_area("Enter Index Mapping comma separetd")
                if index_map:
                    index_map=index_map.split(',')
                    index_mapping={i:j for i,j in zip(selected_index,index_map)}
    
            elif rename_type == "Columns":
                selected_columns = st.multiselect("Select Columns to Rename", options=self.data.columns.tolist(), default=self.data.columns.tolist())
                column_map = st.text_area("Enter Column Mapping comma seperated")
                if column_map:
                    column_map=column_map.split(',')
                    column_map={i:j for i,j in zip(selected_columns,column_map)}
    
            # Error handling parameter
            errors = st.selectbox("Choose Error Behavior", ["ignore", "raise"], index=0)
    
            # Button to perform renaming operation
            if st.button("Apply Rename", use_container_width=True):
                try:
                    # Perform renaming based on selection
                    if rename_type == "Index":
                        renamed_data = self.data.rename(index=index_mapping, errors=errors)
                    elif rename_type == "Columns":
                        renamed_data = self.data.rename(columns=column_mapping, errors=errors)
    
                    # Show success message and renamed DataFrame
                    st.success("Rename applied successfully!")
                    st.dataframe(renamed_data)
    
                    # Save to session state
                    key = f"Stage - Modifications - rename - {rename_type} : {selected_index if rename_type == 'Index' else selected_columns} - errors : {errors}"
                    st.session_state["allData"][key] = renamed_data
    
                except Exception as e:
                    st.error(f"Error applying Rename: {e}")

    
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
