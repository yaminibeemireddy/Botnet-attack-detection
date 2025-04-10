import streamlit as st
import pickle
import pandas as pd
from streamlit_option_menu import option_menu
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import base64
import seaborn as sns
from matplotlib import pyplot as plt
import pdfplumber
import base64

user_data = st.session_state.get('user', None)

def staff_home_page():
    def exam_monitor():
        st.markdown(
            """
            <style>
            /* Apply background image to the main content area */
            .main {
                background-image: url('https://img.freepik.com/premium-photo/creative-educational-sketch-white-backdrop-with-copybooks-education-knowledge-concept-3d-rendering_670147-66821.jpg');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }
            </style>
            """,
            unsafe_allow_html=True
            )
        video=st.file_uploader("Upload Video",type=['mp4'])
        if video:
            #play video
            st.video(video)

    with st.sidebar:
        # Extracting user data from session state after successful login
        user_data = st.session_state.get('user', None)
        if user_data:
            with st.sidebar:
                # Add custom CSS to center content
                st.markdown(
                    """
                    <style>
                    .center-content {
                        text-align: center;
                        margin: auto;
                    }
                    .center-image img {
                        display: block;
                        margin: auto;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )

                # Centered title
                
                st.markdown(
                    f"<h1 class='center-content' style='color: red; t'>{user_data[1]} Profile</h1>",
                    unsafe_allow_html=True
                )
                
                # Centered image
                st.markdown(
                    f"""
                    <div class="center-image">
                        <img src="https://cdn-icons-png.flaticon.com/512/4128/4128176.png" width="250">
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                #need gap
                st.markdown("<br>",unsafe_allow_html=True)
                # Centered user details
                st.markdown(
                    f"""
                    <div class="center-content">
                        <p ><strong>Name:</strong> {user_data[1]}</p>
                        <p ><strong>User Type:</strong> {user_data[3]}</p>
                        <p><strong>Email:</strong> {user_data[2]}</p>
                        <p><strong>Department:</strong> {user_data[4]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


        else:
            st.error("User not logged in!")


    # Navigation menu for user dashboard
    selected = option_menu(
        menu_title=None,
        options=["Exam Monitoring",'Logout'],
        icons=['camera-fill','file-lock2-fill'], menu_icon="cast", default_index=0,
        orientation="horizontal",
    styles={
            "nav-link-selected": {
                "background-color": "#ffc11c",  # Background color of the selected item
                "color": "black",
            },
            "nav-link": {
                "background-color": "#ffefc4",  # Background color of unselected items
                "color": "black",  # Text color of unselected items
            },
        },
    )
    if selected == "Exam Monitoring":
        exam_monitor()
    elif selected=='Logout':
        # setting session data to None
        st.session_state.clear()  # Clear session state to "log out"
        st.rerun()