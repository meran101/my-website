import streamlit as st
import base64

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

div[data-testid="horizontal-block"] {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 8px !important;
}

div[data-testid="column"] {
    flex: 1 1 0% !important;
    min-width: 0 !important;
}

div.stButton > button {
    background: rgba(18, 18, 18, 0.85) !important;
    color: #cccccc !important;
    border: 1px solid rgba(76, 175, 80, 0.4) !important;
    border-radius: 15px !important;
    padding: 6px 8px !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    width: 100% !important;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

div.stButton > button:hover {
    background: #4CAF50 !important;
    color: #ffffff !important;
    border-color: #4CAF50 !important;
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.8) !important;
    transform: translateY(-2px);
}

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
    width: 90px; height: 90px; border-radius: 50%;
    border: 3px solid #4CAF50; box-shadow: 0 0 30px rgba(76, 175, 80, 0.9);
    animation: epicPulse 1.2s infinite alternate; object-fit: cover; margin-bottom: 20px;
}

@keyframes epicPulse {
    0% { transform: scale(0.95); box-shadow: 0 0 15px rgba(76, 175, 80, 0.5); }
    100% { transform: scale(1.1); box-shadow: 0 0 35px rgba(76, 175, 80, 1); }
}

.splash-text {
    color: #4CAF50; font-size: 20px; font-weight: 700; letter-spacing: 3px;
}

@keyframes epicEntrance {
    0% { opacity: 0; transform: translateY(50px) scale(0.85); filter: blur(10px); }
    100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
}

.water-bg-wrapper {
    position: relative; width: 170px; height: 170px; border-radius: 50%;
    display: flex; justify-content: center; align-items: center; margin: 0 auto;
    background: radial-gradient(circle, rgba(0, 150, 255, 0.35) 0%, rgba(76, 175, 80, 0.15) 50%, transparent 75%);
    box-shadow: 0 0 30px rgba(0, 180, 216, 0.5), inset 0 0 20px rgba(0, 119, 182, 0.4);
    animation: waterPulse 3s ease-in-out infinite alternate;
}

@keyframes waterPulse {
    0% { box-shadow: 0 0 20px rgba(0, 180, 216, 0.4), inset 0 0 15px rgba(0, 119, 182, 0.3); transform: scale(0.98); }
    100% { box-shadow: 0 0 45px rgba(0, 212, 255, 0.8), inset 0 0 30px rgba(76, 175, 80, 0.6); transform: scale(1.03); }
}

.profile-container {
    display: flex; justify-content: center; align-items: center; margin-top: 25px; margin-bottom: 25px;
    position: relative; animation: epicEntrance 1.4s cubic-bezier(0.16, 1, 0.3, 1) 1.2s forwards; opacity: 0;
}

.profile-container::before {
    content: ''; position: absolute; width: 155px; height: 155px; border-radius: 50%;
    border: 2px dashed #4CAF50; box-shadow: 0 0 20px rgba(76, 175, 80, 0.6); animation: spin 12s linear infinite;
}

.profile-container::after {
    content: ''; position: absolute; width: 185px; height: 185px; border-radius: 50%;
    background: conic-gradient(from 0deg, #4CAF50, transparent, #00d4ff, transparent);
    -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff
