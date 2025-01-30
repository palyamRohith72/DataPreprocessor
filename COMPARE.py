import streamlit as st
import pandas as pd

class COMPARE:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def display(self):
        tab1, tab2 = st.tabs(["Perform Operation here", "View Result"])

        with tab1:
            col1, col2, col3 = st.columns([1, 2, 1])

            with col1:
                operation = st.radio(
                    "Select Comparison Operation",
                    ["DataFrame.eq", "DataFrame.ne", "DataFrame.le", "DataFrame.ge", "DataFrame.lt", "DataFrame.gt", "DataFrame.compare"]
                )

            if operation in ["DataFrame.eq", "DataFrame.ne"]:
                with col3:
                    comparison_type = st.radio("Select Comparison Type", ["Upload Other Dataset", "Enter Values to Compare"])
                    axis = st.selectbox("Select Axis", ["index", "columns"])

                if comparison_type == "Upload Other Dataset":
                    with col2:
                        file = st.file_uploader("Upload another dataset", type=['csv'])
                        if file:
                            other_df = pd.read_csv(file)
                            # Allow user to input columns from uploaded dataset
                            uploaded_columns = st.text_input("Enter columns for the uploaded dataset (comma-separated):")
                            uploaded_columns_list = [col.strip() for col in uploaded_columns.split(',')] if uploaded_columns else []

                            # Allow user to input columns from the already loaded dataset
                            columns = st.text_input("Enter columns from the already loaded dataset (comma-separated):")
                            columns_list = [col.strip() for col in columns.split(',')] if columns else []

                            if uploaded_columns_list and columns_list:
                                # Extract subdatasets based on selected columns
                                sub_df = self.dataframe[columns_list]
                                sub_other_df = other_df[uploaded_columns_list]

                                if st.button("Confirm", use_container_width=True, type='primary'):
                                    result = getattr(sub_df, operation.split('.')[-1])(sub_other_df)
                                    key = f"{operation.split('.')[-1]}_with_uploaded_dataset_on_selected_columns"
                                    st.session_state["allData"][key] = result
                                    st.write(result)
                            else:
                                st.warning("Please enter columns for both the datasets for comparison.")

                elif comparison_type == "Enter Values to Compare":
                    with col2:
                        input_values = st.text_input("Enter comma-separated values (equal to column length or only one value):")
                        if input_values and st.button("Confirm", use_container_width=True, type='primary'):
                            try:
                                # Split and evaluate the input values
                                values = []
                                for value in input_values.split(','):
                                    if value.isalnum():
                                        values.append(value.strip())
                                    elif value.isdigit():
                                        values.append(int(value.strip()))
                                    elif value.isnumeric():
                                        values.append(float(value.strip()))
                                    else:
                                        values.append(value.strip())         
                                # Handle single value broadcasting
                                if len(values) == 1:
                                    values = values[0]
                                # Handle multiple values comparison
                                elif len(values) == len(self.dataframe.columns):
                                    values = pd.Series(values, index=self.dataframe.columns)
                                elif len(values) == len(self.dataframe.index):
                                    values = pd.Series(values, index=self.dataframe.index)
                                else:
                                    raise ValueError("Invalid number of values provided. Ensure the values match the column or index length.")
                                
                                # Perform the comparison
                                result = getattr(self.dataframe, operation.split('.')[-1])(values)
                                key = f"{operation.split('.')[-1]}_with_values_on_selected_columns"
                                
                                # Save and display the result
                                st.session_state["allData"][key] = result
                                st.write(result)
                            except Exception as e:
                                st.error(f"Error: {e}")


            elif operation in ["DataFrame.le", "DataFrame.ge", "DataFrame.lt", "DataFrame.gt"]:
                with col3:
                    comparison_type = st.radio("Select Comparison Type", ["Upload Other Dataset", "Enter Values to Compare"])
                    axis = st.selectbox("Select Axis", ["index", "columns"])

                if comparison_type == "Upload Other Dataset":
                    with col2:
                        file = st.file_uploader("Upload another dataset", type=['csv'])
                        if file:
                            other_df = pd.read_csv(file)
                            # Allow user to select columns from uploaded dataset using multi-select
                            uploaded_columns = st.multiselect("Select columns from the uploaded dataset", options=other_df.columns)
                            
                            # Allow user to input columns from the already loaded dataset
                            columns = st.text_input("Enter columns from the already loaded dataset (comma-separated):")
                            columns_list = [col.strip() for col in columns.split(',')] if columns else []

                            if uploaded_columns and columns_list:
                                # Extract subdatasets based on selected columns
                                sub_df = self.dataframe[columns_list]
                                sub_other_df = other_df[uploaded_columns]

                                if st.button("Confirm", use_container_width=True, type='primary'):
                                    result = getattr(sub_df, operation.split('.')[-1])(sub_other_df, axis=axis)
                                    key = f"{operation.split('.')[-1]}_with_uploaded_dataset_on_selected_columns"
                                    st.session_state["allData"][key] = result
                                    st.write(result)
                            else:
                                st.warning("Please select columns for both the datasets for comparison.")

                elif comparison_type == "Enter Values to Compare":
                    with col2:
                        input_values = st.text_input("Enter comma-separated values (equal to column length or only one value):")
                        if input_values and st.button("Confirm", use_container_width=True, type='primary'):
                            try:
                                # Split and evaluate the input values
                                values = []
                                for value in input_values.split(','):
                                    if value.isalnum():
                                        values.append(value.strip())
                                    elif value.isdigit():
                                        values.append(int(value.strip()))
                                    elif value.isnumeric():
                                        values.append(float(value.strip()))
                                    else:
                                        values.append(value.strip())         
                                # Handle single value broadcasting
                                if len(values) == 1:
                                    values = values[0]
                                # Handle multiple values comparison
                                elif len(values) == len(self.dataframe.columns) and axis == "columns":
                                    values = pd.Series(values, index=self.dataframe.columns)
                                elif len(values) == len(self.dataframe.index) and axis == "index":
                                    values = pd.Series(values, index=self.dataframe.index)
                                else:
                                    raise ValueError("Invalid number of values provided. Ensure the values match the column or index length.")
                                
                                # Perform the comparison
                                result = getattr(self.dataframe, operation.split('.')[-1])(values, axis=axis)
                                key = f"{operation.split('.')[-1]}_with_values_on_selected_columns"
                                
                                # Save and display the result
                                st.session_state["allData"][key] = result
                                st.write(result)
                            except Exception as e:
                                st.error(f"Error: {e}")


            elif operation == "DataFrame.compare":
                with col3:
                    file = st.file_uploader("Upload another dataset", type=['csv'])
                    align_axis = st.selectbox("Select Align Axis", [1, 0])
                    keep_shape = st.checkbox("Keep Shape", value=False)
                    keep_equal = st.checkbox("Keep Equal", value=False)
                    result_names = st.text_input("Enter Result Names (e.g., ('self', 'other'))")

                with col2:
                    # Allow user to input columns from the uploaded dataset
                    uploaded_columns = st.text_input("Enter columns for the uploaded dataset (comma-separated):")
                    uploaded_columns_list = [col.strip() for col in uploaded_columns.split(',')] if uploaded_columns else []

                    if file:
                        other_df = pd.read_csv(file)

                    # Allow user to input columns from the already loaded dataset
                    columns = st.text_input("Enter columns from the already loaded dataset (comma-separated):")
                    columns_list = [col.strip() for col in columns.split(',')] if columns else []

                    if file and result_names and st.button("Confirm", use_container_width=True, type='primary'):
                        if uploaded_columns_list and columns_list:
                            sub_df = self.dataframe[columns_list]
                            sub_other_df = other_df[uploaded_columns_list]

                            try:
                                result_names_tuple = eval(result_names)
                                result = sub_df.compare(
                                    sub_other_df,
                                    align_axis=align_axis,
                                    keep_shape=keep_shape,
                                    keep_equal=keep_equal,
                                    result_names=result_names_tuple
                                )
                                key = f"compare_with_uploaded_dataframe_on_selected_columns"
                                st.session_state["allData"][key] = result
                                st.write(result)
                            except Exception as e:
                                st.error(f"Error: {e}")
                        else:
                            st.warning("Please enter columns for both datasets for comparison.")

        with tab2:
            if "allData" in st.session_state and st.session_state["allData"]:
                selected_key = st.selectbox("Select a result to view", st.session_state["allData"].keys())
                if selected_key:
                    st.dataframe(st.session_state["allData"][selected_key])
            else:
                st.write("No results available.")
