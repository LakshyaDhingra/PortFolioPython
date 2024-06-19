import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png", width=400)
with col2:
    st.title("Lakshya Dhingra")
    content = """
    Hi, I am Lakshya! I am a student, majoring in Computer Science, learning Python. 
    I am studying at Barrett the Honors College, at Arizona State University.
    """
    st.info(content)
