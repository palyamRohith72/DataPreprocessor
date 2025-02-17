import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from ATTRIBUTES import ATTRIBUTES
from COMPARE import COMPARE
from accessModify import *
from AddDelete import AddDelete

# Initialize session state for storing dataframes
if "allData" not in st.session_state:
    st.session_state["allData"] = {}

# File uploader for CSV files
st.header("Data Preprocessor",divider='blue')
dataframe = st.sidebar.file_uploader("Upload file", type=['csv'])
if dataframe:
    if "readed_csv" not in st.session_state["allData"]:
        st.session_state["allData"]["readed_csv"] = pd.read_csv(dataframe)

# Selectbox to choose the dataframe for operations
selected_data = st.selectbox("Please select the dataframe to perform operation", st.session_state["allData"].keys())

# Sidebar menu for selecting operations
with st.sidebar:
    options = option_menu(
        "Select the operation to perform",
        ["Attributes", "Compare DataFrames","Modifications","Filterations","Mathematical & Statistical", "Merge & Join", "Update DataFrames", "Add & Delete", "Access & Modify Data", "Plot Data"],
        icons=["info-circle", "columns","columns","search","columns", "pen", "pencil-square", "trash", "tools", "book"],
        menu_icon='gear',
        default_index=0
    )

# Perform operation based on selected option
if options == "Attributes":
    if selected_data:
        df = st.session_state["allData"][selected_data]
        attributes = ATTRIBUTES(df)
        attributes.display()

elif options == "Compare DataFrames":
    if selected_data:
        df = st.session_state["allData"][selected_data]
        compare = COMPARE(df)
        compare.display()
elif options == "Merge & Join":
    st.write("Feature coming soon: Merge & Join DataFrames")

elif options == "Update DataFrames":
    st.write("Feature coming soon: Update DataFrames")

elif options == "Add & Delete":
    if selected_data:
        df = st.session_state["allData"][selected_data]
        compare = AddDelete(df)
        compare.display()

elif options == "Access & Modify Data":
    if selected_data:
        df = st.session_state["allData"][selected_data]
        compare = AccessModify(df)
        compare.display()
    

elif options == "Plot Data":
    st.write("Feature coming soon: Plot Data")
