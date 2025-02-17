import streamlit
from streamlit_extras.metric_cards import *
import pandas
import seaborn

class AccessModify:
  def __init__(self,df):
    self.data=df
  def display(self):
    tab1,tab2=st.tabs(['Perform Operations','View Your Results'])
    with tab1:
      col1,col2=st.columns([1,2],border=True)
      options=col1.radio("Please select the operation that you want to perform",['Access Data','Access Data (Advanced)','Modify Values','Modify Values (Advanced)'])
      if options=='Access Data':
        pass
      if options=='Access Data (Advanced)':
        pass
      if options=='Modify Values':
        pass
      if options=='Modify Values (Advanced)':
        pass
