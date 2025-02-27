import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
# from PIL import Image

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

def signUp():
    name = st.text_input("Name")
    password = st.text_input("Password", type='password')
    repass = st.text_input("Re-enter Password", type='password')
    roll = st.number_input("Roll Number", format='%0.0f')
    branch = st.selectbox("Branch", ["CSE", "IT", "ECE", "EE", "ME", "CE"])

    if st.button("SignUp"):
        with connectDB() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE roll=?", (roll,))
            data = cur.fetchone()
            if data:
                st.error("Roll number already exists")
            elif password != repass:
                st.warning("Password does not match")
            else:
                addRecord((name, password, roll, branch))
                st.success("Registered Successfully")

    # if st.button("SignUp"):
    #     if password != repass:
    #         st.warning("Password does not match")
    #     else:
    #         addRecord((name, password, roll, branch))
    #         st.success("Registered Successfully")

def signIn():
    col1, col2 = st.columns(2)
    with col1:
        roll = st.number_input("Roll Number", format='%0.0f')
    with col2:
        password = st.text_input("Password", type='password')
        
    with connectDB() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE roll=? AND password=?", (roll, password))
        data = cur.fetchone()
        if st.button("SignIn"):
            if data:
                return data
            else:
                st.error("Invalid Credential")

def searchRecord(roll):
    with connectDB() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE roll=?", (roll,))
        data = cur.fetchone()
        if st.button("Search"):
            if data:
                return data
            else:
                st.warning("Record not found")

def resetPass(roll, password):
    with connectDB() as conn:
        cur = conn.cursor()
        cur.execute("UPDATE users SET password=? WHERE roll=?", (password, roll))
        conn.commit()

def deleteRecord(roll):
    with connectDB() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE roll=?", (roll,))
        result = cur.fetchone()

        if st.button("Delete"):
            if result == True:
                st.success("Record Deleted Successfully")
                conn.commit()
            else:
                st.warning("Record not found")

def home():  
    st.title("Home Page")
    st.write("Welcome to my App")
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.write("This is a simple app to manage student records")
    st.write("You can add, delete, search and reset password of student record")

createTable()
with st.sidebar:
    selected = option_menu("My APP", ['Home', 'SignUp', 'SignIn', 'Display All Record', 'Reset password', 'Search', 'delete record'], icons=['house', 'person-bounding-box', 'person-check-fill', 'database', 'arrow-clockwise', 'search', 'trash'], menu_icon="app", default_index=0)


if selected == 'Home':
    home()
elif selected == 'SignUp':
    signUp()
elif selected == 'SignIn':
    data = signIn()
    if data:
        st.success("Login Successfully")
        st.table([data])
elif selected == 'Display All Record':
    data = displayData()
    st.table(data)
elif selected == 'Search':
    roll = st.number_input("Roll Number", format='%0.0f')
    data = searchRecord(roll)
    if data:
        st.table([data])
elif selected == 'Reset password':
    roll = st.number_input("Roll Number", format='%0.0f')
    password = st.text_input("New Password", type='password')
    if st.button("Reset"):
        resetPass(roll, password)
        st.success("Password Reset Successfully")
elif selected == 'delete record':
    roll = st.number_input("Roll Number", format='%0.0f')
    if st.button("Delete"):
        deleteRecord(roll)