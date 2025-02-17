import streamlit as st
import pandas as pd
from streamlit_extras.metric_cards import *
import seaborn as sns

class AccessModify:
    def __init__(self, df):
        self.df = df
        if "allData" not in st.session_state:
            st.session_state["allData"] = {}

    def display(self):
        tab1, tab2 = st.tabs(['Perform Operations', 'View Your Results'])
        
        with tab1:
            col1, col2 = st.columns([1, 2])
            
            options = col1.radio("Please select the operation that you want to perform", 
                                ['Access Data', 'Access Data (Advanced)', 'Modify Values', 'Modify Values (Advanced)'])
            
            if options == 'Access Data':
                self.access_data(col1, col2)
            elif options == 'Access Data (Advanced)':
                st.warning("Feature not implemented yet.")
            elif options == 'Modify Values':
                st.warning("Feature not implemented yet.")
            elif options == 'Modify Values (Advanced)':
                st.warning("Feature not implemented yet.")
        
        with tab2:
            st.subheader("Stored Results", divider='green')
            if st.session_state["allData"]:
                for key, value in st.session_state["allData"].items():
                    st.write(f"**{key}**")
                    st.dataframe(value)
            else:
                st.info("No stored results yet.")

    def access_data(self, col1, col2):
        col2.subheader("Please select an option", divider='green')
        options = col2.radio("Options", 
                            ['Access first n rows', 'Access last n rows', 'Access Sample Data', 'Access Filtered Data'])
        
        if options == 'Access first n rows':
            self.access_first_n_rows(col2)
        elif options == 'Access last n rows':
            self.access_last_n_rows(col2)
        elif options == 'Access Sample Data':
            self.access_sample_data(col2)
        elif options == 'Access Filtered Data':
            st.warning("Feature not implemented yet.")

    def access_first_n_rows(self, col2):
        col2.subheader("Provide input for selected option", divider='green')
        slider = col2.slider("Drag to select number of rows", 1, self.df.shape[0])
        columns = col2.multiselect("Select the columns", ['All Columns'] + list(self.df.columns))
        
        if col2.button("Fix My Settings", use_container_width=True, type='primary'):
            if not columns:
                col2.warning("You must select at least one column.")
                return
            
            if "All Columns" in columns:
                selected_data = self.df.head(slider)
            else:
                selected_data = self.df.head(slider)[columns]
            
            key = f"Stage - Access & Modify - First {slider} Rows with columns - {columns}"
            st.session_state["allData"][key] = selected_data
            
            col2.subheader("Your Results", divider='grey')
            col2.dataframe(selected_data)

    def access_last_n_rows(self, col2):
        col2.subheader("Provide input for selected option", divider='green')
        slider = col2.slider("Drag to select number of rows", 1, self.df.shape[0])
        columns = col2.multiselect("Select the columns", ['All Columns'] + list(self.df.columns))
        
        if col2.button("Fix My Settings", use_container_width=True, type='primary'):
            if not columns:
                col2.warning("You must select at least one column.")
                return
            
            if "All Columns" in columns:
                selected_data = self.df.tail(slider)
            else:
                selected_data = self.df.tail(slider)[columns]
            
            key = f"Stage - Access & Modify - Last {slider} Rows with columns - {columns}"
            st.session_state["allData"][key] = selected_data
            
            col2.subheader("Your Results", divider='grey')
            col2.dataframe(selected_data)

    def access_sample_data(self, col2):
        col2.subheader("Provide input for selected option", divider='green')
        sample_size = col2.slider("Select number of random samples", 1, self.df.shape[0])
        columns = col2.multiselect("Select the columns", ['All Columns'] + list(self.df.columns))
        
        if col2.button("Fix My Settings", use_container_width=True, type='primary'):
            if not columns:
                col2.warning("You must select at least one column.")
                return
            
            if "All Columns" in columns:
                selected_data = self.df.sample(sample_size)
            else:
                selected_data = self.df.sample(sample_size)[columns]
            
            key = f"Stage - Access & Modify - Sample {sample_size} Rows with columns - {columns}"
            st.session_state["allData"][key] = selected_data
            
            col2.subheader("Your Results", divider='grey')
            col2.dataframe(selected_data)
