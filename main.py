import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo1.jpg', width=300)

with col2:
    st.title('Vasanta Koli')
    content = """Hi, I’m Vasanta Koli, an IT leader with 18+ years of experience in managing production operations, 
    automation, and IT infrastructure in the Payments domain. Currently, as a VP – Production Assurance Lead at Axis 
    Bank, I drive system optimization, service resilience, and automation strategies, leading a team of 40+ 
    engineers. With expertise in cloud (Azure & AWS), DevOps, Python, and IT service management, I have successfully 
    enhanced IT operations at HSBC, JPMorgan Chase, Tech Mahindra, and more. Passionate about technology-driven 
    transformation, I specialize in problem-solving, process automation, and strategic leadership to create scalable 
    and resilient IT ecosystems."""
    st.info(content)
