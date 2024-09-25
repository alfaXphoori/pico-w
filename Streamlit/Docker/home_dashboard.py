import streamlit as st
import pandas as pd
import streamviz

# Predefined credentials for demonstration purposes
USERNAME = "test"
PASSWORD = "test"

# Check if the user is logged in, and set the appropriate page icon
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Function to verify login credentials
def login(username, password):
    if username == USERNAME and password == PASSWORD:
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        return True
    return False

# Function to display the login page
def login_page():
    # Set the page configuration with a key icon for the login page
    st.set_page_config(page_title="Login Page", page_icon="🔑", layout="centered")
    
    st.title("Login Page")

    # Create a form for user login
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        # Check credentials
        if submit:
            if login(username, password):
                st.success(f"Welcome, {username}! 🎉 Redirecting to the main page...")
                st.rerun()  # Reload the page to show main page after login
            else:
                st.error("Invalid username or password. Please try again.")

# Function to display the main page
def main_page():
    # Set the page configuration with a home icon for the main page
    st.set_page_config(page_title="Main Page", page_icon="🏠", layout="centered")
    
    st.title("🏠 Home Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Temperature")
        with st.container(height=200):
            streamviz.gauge(
                gVal=34, gSize="SML", 
                gTitle="Temeperature", gMode="gauge+number",
                grLow=20, grMid=50, gcLow="#e2e6bd", 
                gcMid="#e8c33c", gcHigh="#e1704c", arTop=70
)
        with st.container(height=200):
            time = [1,2,3,4,5,6,7,8,9,10]
            chart_data = pd.DataFrame(time)
            st.line_chart(chart_data,height=200, color="#ffaa00")
    with col2:
        st.write("Huminity")
        with st.container(height=200):
            streamviz.gauge(
                gVal=70, gSize="SML", 
                gTitle="Huminity", gMode="gauge+number",
                grLow=20, grMid=50, gcLow="#e2e6bd", 
                gcMid="#e8c33c", gcHigh="#e1704c", arTop=100
)
        with st.container(height=200):
            temp_value = [40,25,30,77,44,50,99,33,66,34]
            chart_data = pd.DataFrame(temp_value)
            st.line_chart(chart_data, height=200, color="#1f2200")
            
    col21, col22, col23, = st.columns(3)

    with col21:
        with st.container(height = 120):
            on1 = st.toggle("LAMP 1")
            if on1:
                st.write("ON")
            else:
                st.write("OFF")
    with col22:
        with st.container(height = 120):
            on2 = st.toggle("LAMP 2")
            if on2:
                st.write("ON")
            else:
                st.write("OFF")
    with col23:
        with st.container(height = 120):
            on3 = st.toggle("LAMP 3")
            if on3:
                st.write("ON")
            else:
                st.write("OFF")
    
    with st.container(height=400):
        #st.write("map")
        location = {'lat':[16.44828426030011,16.454618931231167], 'lon':[103.53131004831428,103.53143712501553]}
        loc_df = pd.DataFrame(location)
        st.map(loc_df)

    # Log out button
    if st.button("Log out"):
        st.session_state["logged_in"] = False
        st.rerun()

# Main application logic: Show login page if not logged in, else show main page
if st.session_state["logged_in"]:
    main_page()  # Show main page if logged in
else:
    login_page()  # Show login page if not logged in
#main_page()