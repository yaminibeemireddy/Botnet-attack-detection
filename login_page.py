import streamlit as st
from db_manager import validate_user

def login_page():
    # Center the login form using Streamlit form layout
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: rgba(255, 255, 255, 0.4);
            background-blend-mode: overlay;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col1,col2,col3=st.columns([9,10,5])
    # Title
    col2.title("Login Here!!")
    # Email and Password inputs
    col1, col2, col3 = st.columns([1, 3, 1])
    email = col2.text_input("Enter Email")
    password = col2.text_input("Enter Password", type="password")
    col1, col2, col3 = st.columns([12, 10, 5])
    # Submit button inside the form
    login_button = col2.button("Login")
    col1, col2, col3 = st.columns([1, 3, 1])
    #clear session state
    # Handling form submission
    if login_button:
        user = validate_user(email, password)
        if user:
            # Set session state to user_home and store user details
            st.session_state["page"] = "user_home"
            st.session_state["user"] = user  # Store user info (e.g., name, email)
            st.experimental_rerun()
        else:
            col2.error("Invalid Email or Password!")
