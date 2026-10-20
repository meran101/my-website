import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="موقعي الشخصي", page_icon="👤", layout="centered")

# --- كود إخفاء الشعار والقوائم بالكامل (نسخة مطورة وشاملة) ---
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppHeader {display: none;}
            .stAppFooter {display: none;}
            [data-testid="stHeader"] {display: none;}
            [data-testid="stStatusWidget"] {display: none;}
            #stDecoration {display: none;}
            
            /* إخفاء شعار الاستضافة والشريط السفلي نهائياً */
            footer {visibility: hidden !important; display: none !important;}
            .viewerBadge_container__1QSob {visibility: hidden !important; display: none !important;}
            div[class*="viewerBadge"] {display: none !important;}
            div[data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
            .styles_viewerBadge__1yG5_ {display: none !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)