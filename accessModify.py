import streamlit
from streamlit_extras.metric_cards import *
import pandas
import seaborn

class AccessModify:
  def __init__(self,df):
    self.df=df
  def display(self):
    tab1,tab2=st.tabs(['Perform Operations','View Your Results'])
    with tab1:
      col1,col2=st.columns([1,2],border=True)
      options=col1.radio("Please select the operation that you want to perform",['Access Data','Access Data (Advanced)','Modify Values','Modify Values (Advanced)'])
      if options=='Access Data':
        self.access_data(col1,col2)
      if options=='Access Data (Advanced)':
        pass
      if options=='Modify Values':
        pass
      if options=='Modify Values (Advanced)':
        pass
  def access_data(self,col1,col2):
    col2.subheader("Please select an option",divider='green')
    options=col2.radio("Options were",['Access first n rows','Access last n rows','Access Sample Data',"Access Filetr Data"])
    if options=='Access first n rows':
      col2.subheader("Provide input for selected Option",divider='green')
      slider=col2.slider("Drag To Select Number Of Rows",1,self.df.shape[0]
      columns=col2.multiselect("Select the columns",["All Columns"]+self.df.columns)
      if col2.button("Fix My Settings",use_container_width=True,type='primery'):
        if slider and columns:
          if len(columns)==1 and "All Columns" in columns:
            selectedData=self.df.head(slider)
          elif len(columns)>1 and "All Columns" in columns:
            col2.info("You Can select all colummns or some columns")
          elif len(columns)>=1 and "All Columns" not in columns:
            selectedData=self.df.head(slider)[columns]
          st.session_state["allData"][f"Stage - Access & Modify - First {slider} Rows with columnns - {columns}"]=selectedData
          col2.subheader("Your Results",divider='grey')
          col2.dataframe(selectedData)
      else:
        col2.info("You have to select both rows and columns")
    
