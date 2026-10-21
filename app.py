import streamlit as st
import base64

# 1. إعداد حالة الصفحة واللغة في التخزين المؤقت
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

# 2. إعداد CSS والتصميم الحديث والأيقونات الأفقية المتناسقة
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none !important;}
            div[data-testid="stDecoration"] {display: none !important;}
            
            /* خلفية الموقع الداكنة الفخمة */
            .stApp {
                background-color: #050505;
                color: #ffffff;
            }
            
            /* تنسيق أزرار التنقل الأفقية الحديثة */
            div.stButton > button {
                background: rgba(18, 18, 18, 0.85) !important;
                color: #cccccc !important;
                border: 1px solid rgba(76, 175, 80, 0.4) !important;
                border-radius: 20px !important;
                padding: 6px 12px !important;
                font-size: 13px !important;
                font-weight: 600 !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
                width: 100% !important;
                backdrop-filter: blur(10px);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
            }

            div.stButton > button:hover {
                background: #4CAF50 !important;
                color: #ffffff !important;
                border-color: #4CAF50 !important;
                box-shadow: 0 0 20px rgba(76, 175, 80, 0.8) !important;
                transform: translateY(-2px);
            }

            /* شاشة البداية (Splash Screen) */
            @keyframes splashEpicOut {
                0% { opacity: 1; visibility: visible; transform: scale(1); }
                85% { opacity: 1; transform: scale(1); }
                100% { opacity: 0; visibility: hidden; transform: scale(1.1); pointer-events: none; }
            }

            .splash-screen {
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: radial-gradient(circle, #121212 0%, #000000 100%);
                display: flex; flex-direction: column; justify-content: center; align-items: center;
                z-index: 99999; animation: splashEpicOut 1.8s cubic-bezier(0.77, 0, 0.175, 1) forwards;
            }

            .splash-logo {
                width: 110px; height: 110px; border-radius: 50%;
                border: 3px solid #4CAF50; box-shadow: 0 0 40px rgba(76, 175, 80, 0.9);
                animation: epicPulse 1.2s infinite alternate; object-fit: cover; margin-bottom: 20px;
            }

            @keyframes epicPulse {
                0% { transform: scale(0.95); box-shadow: 0 0 20px rgba(76, 175, 80, 0.5); }
                100% { transform: scale(1.1); box-shadow: 0 0 50px rgba(76, 175, 80, 1); }
            }

            .splash-text {
                color: #4CAF50; font-size: 22px; font-weight: 700; letter-spacing: 3px;
            }

            /* تأثيرات الحركة السينمائية */
            @keyframes cinematicAppear {
                0% { opacity: 0; transform: translateY(40px) scale(0.9); filter: blur(8px); }
                100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
            }

            .profile-container {
                display: flex; justify-content: center; align-items: center; margin-top: 25px; margin-bottom: 25px;
                position: relative; animation: cinematicAppear 1.2s cubic-bezier(0.16, 1, 0.3, 1) 1.2s forwards; opacity: 0;
            }

            .profile-container::before {
                content: ''; position: absolute; width: 225px; height: 225px; border-radius: 50%;
                border: 3px dashed #4CAF50; box-shadow: 0 0 30px rgba(76, 175, 80, 0.6); animation: spin 12s linear infinite;
            }

            .profile-container::after {
                content: ''; position: absolute; width: 265px; height: 265px; border-radius: 50%;
                background: conic-gradient(from 0deg, #4CAF50, transparent, #4CAF50, transparent);
                -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 3px), #fff calc(100% - 3px));
                mask: radial-gradient(farthest-side, transparent calc(100% - 3px), #fff calc(100% - 3px));
                animation: spin-reverse 18s linear infinite;
            }

            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            @keyframes spin-reverse { 0% { transform: rotate(360deg); }
