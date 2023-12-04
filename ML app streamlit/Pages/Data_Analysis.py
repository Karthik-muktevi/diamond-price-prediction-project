import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport

df = pd.read_csv('diamonds.csv')
st.title('Data Info & Data Analysis of Diamonds price prediction dataset')
st.selectbox('Select dataset',['diamonds'])
option = st.selectbox('Data Analysis',['Data Info','Data Analysis'])

if True:
    if option =='Data Analysis':
        submit = st.button('Generate Report')
    elif option=='Data Info':
        submit = st.button('Submit')

if submit:
    if option=='Data Analysis':
        profile = ProfileReport(df, title="Pandas Profiling Report")
        with st.spinner("Generating Report....\nplease wait...."):
            st.write("## Report")
            st.components.v1.html(profile.to_html(), width=1000, height=1200, scrolling=True)

    elif option =='Data Info':
        st.write('Data Description')
        des ='description.txt'
        with open('description.txt') as input:
            st.text(input.read())