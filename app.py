import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="موقعي الشخصي", layout="wide")

# كود إخفاء الشعار والقائمة والعلامة المائية بطريقة أمنة
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none !important;}
            div[data-testid="stDecoration"] {display: none !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# محتوى موقعك هنا
st.title("أهلاً بك في موقعي الشخصي 👋")
st.write("هذا الموقع مستضاف بنجاح وبدون أي علامة مائية!")
