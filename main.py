import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo1.jpg')

with col2:
    st.title('Vasanta Koli')
    content =  """
    Hi, I’m **Vasanta Koli**, an IT leader with **18+ years of experience** in managing 
    **production operations, automation, and IT infrastructure** in the **Payments domain**. 
    Currently, as a **VP – Production Assurance Lead at Axis Bank**, I drive system optimization, 
    service resilience, and automation strategies. 
    
    With expertise in **cloud technologies, DevOps, and IT service management**, I have enhanced 
    IT operations at **HSBC, JPMorgan Chase, and more**. Passionate about **technology-driven transformation**, 
    I specialize in **problem-solving, process automation, and strategic leadership** 
    to build scalable and resilient IT ecosystems.
    """
    st.info(content)

content2 = 'Below you can find some of the apps I have built in Python. Feel free to contact me!'
st.write(content2)

col3, col4 = st.columns(2)

dataFrame = pd.read_csv('data.csv', sep=';')
# title description url image
with col3:
    for index, row in dataFrame[:10].iterrows():
        st.header(row['title'])


with col4:
    for index, row in dataFrame[10:].iterrows():
        st.header(row['title'])