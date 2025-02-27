import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
from PIL import Image

def connectDB():
    conn = sqlite3.connect("data.db")
    return conn

def displayData():
    with connectDB() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        return data

def createTable():
    with connectDB() as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (name text, password text, roll integer primary key, branch text)")
        conn.commit()

def addRecord(data):
    with connectDB() as conn:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users(name, password, roll, branch) VALUES (?, ?, ?, ?)", data)
            conn.commit()
        except  sqlite3.integrityError:
            st.error("Roll already exists")

def UISignup():
    name = st.text_input("Name")
    password = st.text_input("Password", type='password')
    repass = st.text_input("Re-enter Password", type='password')
    roll = st.number_input("Roll Number", format='%0.0f')
    branch = st.selectbox("Branch", ["CSE", "IT", "ECE", "EE", "ME", "CE"])

    if st.button("SignIn"):
        if password != repass:
            st.warning("Password does not match")
        else:
            addRecord((name, password, roll, branch))
            st.success("Registered Successfully")

createTable()

with st.sidebar:
    # st.image("https://www.gstatic.com/webp/gallery/1.jpg")
    selected = option_menu("My APP", ['SignUp', 'Display All Record'], icons=['house', 'apple'], menu_icon="cast", default_index=1)

if selected == 'SignUp':
    UISignup()
else:
    data = displayData()
    st.table(data)

# roll no as input to reset password
# create a filter to filter student record on basis of branch
# delete student record
# menu for reset password
# Container
# Table