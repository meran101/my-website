import streamlit as st

# كود إخفاء العلامة المائية والشعار والقائمة
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display:none !important;}
            [data-testid="stDecoration"] {display:none !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
