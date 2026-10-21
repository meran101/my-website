import streamlit as st

# إعداد الصفحة وإخفاء العلامة المائية والشعار
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none !important;}
            div[data-testid="stDecoration"] {display: none !important;}
            
            /* جعل الصورة دائرية وفي المنتصف */
            [data-testid="stImage"] {
                display: flex;
                justify-content: center;
            }
            [data-testid="stImage"] > img {
                border-radius: 50%;
                width: 180px !important;
                height: 180px !important;
                object-fit: cover;
                border: 4px solid #4CAF50;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# عرض الصورة المحلية مباشرة عبر دالة Streamlit الرسمية
st.image("IMG_20240908_230026_233.jpg")

# عنوان الموقع والنصوص
st.markdown("<h1 style='text-align: center;'>أهلاً بك في موقعي الشخصي 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>هذا هو موقعي المصمم بكل حب!</p>", unsafe_allow_html=True)
