import streamlit as st
import streamviz
import pandas as pd
import numpy as np
# Dummy user credentials for login
user_db = {
    "userID": "test",
    "passWD": "1234"
}

# Function to check login credentials
def check_login(username, password):
    if username == user_db["userID"] and password == user_db["passWD"]:
        return True
    return False

# Function to display the login page
def login_page():
    st.title("Login Page")
    
    # Username input
    username = st.text_input("Username")
    
    # Password input (the password will be hidden)
    password = st.text_input("Password", type="password")
    
    # Login button
    if st.button("Login"):
        if check_login(username, password):
            st.session_state['logged_in'] = True
            st.rerun()  # Rerun to load the Home page
        else:
            st.error("Incorrect username or password. Please try again.")

# Function to display the home page after login
def home_page():
    st.header("Home Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True,height=200):
            streamviz.gauge(
                gVal=25.2, gSize="SML", 
                gTitle="Temperature", gMode="gauge+number",
                grLow=20, grMid=50, gcLow='#fefae0', 
                gcMid='#ccd5ae', gcHigh='#d4a373', arTop=80,
                cWidth=True
                )
        with st.container(border=True,height=250):
            st.text("Temperature")
            temp_vale = [25,23,19,39,49,69,49,30,11,45]
            chart_data = pd.DataFrame(temp_vale)
            st.line_chart(
                chart_data, color="#ffaa00",height=250
            )

    with col2:
        with st.container(border=True,height=200):
            streamviz.gauge(
                gVal=60, gSize="SML", 
                gTitle="Humidity", gMode="gauge+number",
                grLow=30, grMid=70, gcLow='#caf0f8', 
                gcMid='#90e0ef', gcHigh='#0096c7', arTop=100
                )
        with st.container(border=True,height=250):
            st.text("Humidity")
            temp_vale = [50,60,70,45,44,66,77,55,55,99]
            chart_data = pd.DataFrame(temp_vale)
            st.line_chart(
                chart_data, height=250
            )
    col11, col12, col13 = st.columns(3, vertical_alignment="center")
    with col11:
        with st.container(border=True, height=100):
            on1 = st.toggle("LAMP 1")
            if on1: 
                st.write("ON")
            else:
                st.write("OFF")
    with col12:
        with st.container(border=True, height=100):
            on2 = st.toggle("LAMP 2")
            if on2: 
                st.write("ON")
            else:
                st.write("OFF")
    with col13:
        with st.container(border=True, height=100):
            on3 = st.toggle("LAMP 3")
            if on3: 
                st.write("ON")
            else:
                st.write("OFF")
    
    with st.container(border=True, height=400):
        data = {'lat': [16.447885162412057], 'lon': [103.53140799906956]}
        dfm = pd.DataFrame(data)
        st.map(dfm)

# Main app logic to manage navigation between pages
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Navigation: Show the Home page if logged in, otherwise show the Login page
if st.session_state['logged_in']:
    home_page()
else:
    login_page()
#home_page()