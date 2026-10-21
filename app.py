import streamlit as st
import base64

# 1. إعداد حالة الصفحة واللغة
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

if "lang" not in st.session_state:
    st.session_state.lang = "en"

def set_page(page_name):
    st.session_state.current_page = page_name

def toggle_language():
    if st.session_state.lang == "en":
        st.session_state.lang = "ar"
    else:
        st.session_state.lang = "en"

# 2. إعداد CSS وتصميم القائمة العلوية الثابتة
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none !important;}
            div[data-testid="stDecoration"] {display: none !important;}
            
            .stApp {
                background-color: #050505;
                color: #ffffff;
            }
            
            /* تنسيق أزرار التنقل بين الصفحات لضمان ظهورها بشكل بارز */
            div.stButton > button {
                background-color: #121212 !important;
                color: #4CAF50 !important;
                border: 2px solid #4CAF50 !important;
                border-radius: 12px !important;
                padding: 8px 12px !important;
                font-size: 14px !important;
                font-weight: 700 !important;
                transition: all 0.3s ease !important;
                width: 100% !important;
                box-shadow: 0 0 10px rgba(76, 175, 80, 0.2) !important;
            }
            div.stButton > button:hover {
                background-color: #4CAF50 !important;
                color: #ffffff !important;
                box-shadow: 0 0 20px rgba(76, 175, 80, 0.8) !important;
                transform: scale(1.05) !important;
            }

            /* شاشة البداية (Splash Screen) */
            @keyframes splashEpicOut {
                0% { opacity: 1; visibility: visible; }
                85% { opacity: 1; }
                100% { opacity: 0; visibility: hidden; pointer-events: none; }
            }

            .splash-screen {
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: radial-gradient(circle, #121212 0%, #000000 100%);
                display: flex; flex-direction: column; justify-content: center; align-items: center;
                z-index: 99999; animation: splashEpicOut 1.8s cubic-bezier(0.77, 0, 0.175, 1) forwards;
            }

            .splash-logo {
                width: 100px; height: 100px; border-radius: 50%;
                border: 3px solid #4CAF50; box-shadow: 0 0 35px rgba(76, 175, 80, 0.9);
                animation: epicPulse 1.2s infinite alternate; object-fit: cover; margin-bottom: 20px;
            }

            @keyframes epicPulse {
                0% { transform: scale(0.95); box-shadow: 0 0 20px rgba(76, 175, 80, 0.5); }
                100% { transform: scale(1.1); box-shadow: 0 0 50px rgba(76, 175, 80, 1); }
            }

            .splash-text { color: #4CAF50; font-size: 20px; font-weight: 700; letter-spacing: 2px; }

            /* تأثيرات الحركة */
            @keyframes cinematicAppear {
                0% { opacity: 0; transform: translateY(30px) scale(0.9); filter: blur(6px); }
                100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
            }

            .profile-container {
                display: flex; justify-content: center; align-items: center; margin-top: 25px; margin-bottom: 25px;
                position: relative; animation: cinematicAppear 1.2s cubic-bezier(0.16, 1, 0.3, 1) 1.2s forwards; opacity: 0;
            }

            .profile-container::before {
                content: ''; position: absolute; width: 220px; height: 220px; border-radius: 50%;
                border: 3px dashed #4CAF50; box-shadow: 0 0 30px rgba(76, 175, 80, 0.6); animation: spin 12s linear infinite;
            }

            .profile-container::after {
                content: ''; position: absolute; width: 260px; height: 260px; border-radius: 50%;
                background: conic-gradient(from 0deg, #4CAF50, transparent, #4CAF50, transparent);
                -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 3px), #fff calc(100% - 3px));
                mask: radial-gradient(farthest-side, transparent calc(100% - 3px), #fff calc(100% - 3px));
                animation: spin-reverse 18s linear infinite;
            }

            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            @keyframes spin-reverse { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }

            .profile-img {
                width: 180px !important; height: 180px !important; border-radius: 50% !important;
                object-fit: cover !important; border: 4px solid #4CAF50 !important;
                box-shadow: 0px 0px 40px rgba(76, 175, 80, 0.7); position: relative; z-index: 2;
            }

            .title-animation {
                animation: cinematicAppear 1.2s cubic-bezier(0.16, 1, 0.3, 1) 1.4s forwards; opacity: 0;
                text-align: center; color: #ffffff; font-weight: 800; font-size: 32px;
            }

            .subtitle-animation {
                animation: cinematicAppear 1.2s cubic-bezier(0.16, 1, 0.3, 1) 1.6s forwards; opacity: 0;
                text-align: center; color: #4CAF50; font-size: 18px;
            }

            .social-container {
                display: flex; justify-content: center; align-items: center; gap: 25px; margin-top: 25px;
                animation: cinematicAppear 1.2s cubic-bezier(0.16, 1, 0.3, 1) 1.8s forwards; opacity: 0;
            }

            .social-btn {
                display: inline-flex; justify-content: center; align-items: center; width: 55px; height: 55px;
                border-radius: 50%; color: white; font-size: 26px; transition: all 0.4s ease; text-decoration: none;
            }
            .insta-btn { background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fd5949 45%, #d6249f 60%, #285AEB 90%); box-shadow: 0px 5px 20
