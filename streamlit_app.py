import streamlit as st

lab1 = st.Page("lab1.py",title="Lab 1")
lab2 = st.Page("lab2.py",title="Lab 2")
lab3 = st.Page("lab3.py",title="Lab 3")
lab4 = st.Page("lab4.py",title="Lab 4")
pg = st.navigation([lab4, lab1, lab2, lab3])
st.set_page_config(page_title="LAB Main Page")
pg.run()