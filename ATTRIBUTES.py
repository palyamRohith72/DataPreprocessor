import streamlit as st
import pandas as pd

class ATTRIBUTES:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def display(self):
        # Initialize session state for storing data if not already done
        if 'allData' not in st.session_state:
            st.session_state['allData'] = {}

        st.session_state['allData']['original_dataframe'] = self.dataframe

        tab1, tab2 = st.tabs(["Perform Operation here", "View Result"])

        with tab1:
            col1, col2 = st.columns([1, 2],border=True)

            # Radio buttons in column 1
            operations = [
                "DataFrame.index",
                "DataFrame.columns",
                "DataFrame.dtypes",
                "DataFrame.info",
                "DataFrame.select_dtypes",
                "DataFrame.values",
                "DataFrame.axes",
                "DataFrame.ndim",
                "DataFrame.size",
                "DataFrame.shape",
                "DataFrame.memory_usage",
                "DataFrame.empty",
                "DataFrame.set_flags",
            ]
            selected_operation = col1.radio("Select an operation:", operations)

            # Display result in column 2
            if selected_operation == "DataFrame.index":
                col2.dataframe(self.dataframe.index)
            elif selected_operation == "DataFrame.columns":
                col2.dataframe(self.dataframe.columns)
            elif selected_operation == "DataFrame.dtypes":
                col2.dataframe(self.dataframe.dtypes)
            elif selected_operation == "DataFrame.info":
                col2.dataframe(self.dataframe.info())
            elif selected_operation == "DataFrame.select_dtypes":
                # Display available datatypes in a multiselect
                available_dtypes = list(self.dataframe.dtypes.unique())
                selected_dtypes = col2.multiselect("Select datatypes to include:", available_dtypes)
                if selected_dtypes:
                    filtered_df = self.dataframe.select_dtypes(include=selected_dtypes)
                    col2.dataframe(filtered_df)
            elif selected_operation == "DataFrame.values":
                col2.write(self.dataframe.values)
            elif selected_operation == "DataFrame.axes":
                col2.write(self.dataframe.axes)
            elif selected_operation == "DataFrame.ndim":
                col2.write(self.dataframe.ndim)
            elif selected_operation == "DataFrame.size":
                col2.write(self.dataframe.size)
            elif selected_operation == "DataFrame.shape":
                col2.write(self.dataframe.shape)
            elif selected_operation == "DataFrame.memory_usage":
                col2.write(self.dataframe.memory_usage())
            elif selected_operation == "DataFrame.empty":
                col2.write(self.dataframe.empty)
            elif selected_operation == "DataFrame.set_flags":
                col2.write(self.dataframe.set_flags())

        with tab2:
            # Selectbox for displaying dataframes from session state
            all_data_keys = list(st.session_state['allData'].keys())
            selected_key = st.selectbox("Select a dataframe to view:", all_data_keys)

            if selected_key:
                st.dataframe(st.session_state['allData'][selected_key])
