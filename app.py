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

/* خلفية الموقع الأساسية */
.stApp {
    background-color: #050505;
    color: #ffffff;
}

/* طبقة مطر الحروف الإنجليزية المتقطعة */
.matrix-rain {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 1;
    overflow: hidden;
    opacity: 0.4;
}

.matrix-column {
    position: absolute;
    top: -50%;
    color: #4CAF50;
    font-family: monospace;
    font-size: 16px;
    font-weight: bold;
    line-height: 20px;
    letter-spacing: 2px;
    text-align: center;
    text-shadow: 0 0 8px rgba(76, 175, 80, 0.9), 0 0 4px rgba(0, 212, 255, 0.7);
    animation: matrixFall linear infinite;
}

@keyframes matrixFall {
    0% { transform: translateY(-100%); }
    100% { transform: translateY(200vh); }
}

/* ضمان ظهور محتوى ستريملت فوق طبقة المطر والخلفية */
section.main > div {
    position: relative;
    z-index: 10;
}

div[data-testid="horizontal-block"] {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 8px !important;
    position: relative;
    z-index: 10;
}

div[data-testid="column"] {
    flex: 1 1 0% !important;
    min-width: 0 !important;
}

/* الأزرار العادية (الرئيسية واللغة) */
div.stButton > button {
    background: rgba(18, 18, 18, 0.9) !important;
    color: #cccccc !important;
    border: 1px solid rgba(76, 175, 80, 0.4) !important;
    border-radius: 15px !important;
    padding: 8px 10px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
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
    border-color: #00d4ff !important;
    box-shadow: 0 0 25px rgba(76, 175, 80, 0.9), 0 0 10px rgba(0, 212, 255, 0.6) !important;
    transform: translateY(-3px) scale(1.02);
}

/* زر عني (About) الاحترافي بتأثير مائي متحرك */
div[data-testid="column"]:nth-child(2) div.stButton > button {
    background: linear-gradient(135deg, rgba(0, 119, 182, 0.7), rgba(0, 212, 255, 0.4)), rgba(18, 18, 18, 0.95) !important;
    border: 1px solid rgba(0, 212, 255, 0.9) !important;
    color: #ffffff !important;
    box-shadow: 0 0 25px rgba(0, 150, 255, 0.6), inset 0 0 15px rgba(0, 212, 255, 0.5) !important;
    animation: proWaterButtonPulse 3s ease-in-out infinite alternate;
}

div[data-testid="column"]:nth-child(2) div.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.9), rgba(76, 175, 80, 0.8)) !important;
    border-color: #ffffff !important;
    box-shadow: 0 0 35px rgba(0, 212, 255, 0.9), 0 0 15px rgba(76, 175, 80, 0.7) !important;
    transform: translateY(-3px) scale(1.03);
}

@keyframes proWaterButtonPulse {
    0% {
        box-shadow: 0 0 15px rgba(0, 150, 255, 0.4), inset 0 0 10px rgba(0, 212, 255, 0.3);
        border-color: rgba(0, 212, 255, 0.6);
    }
    100% {
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.8), inset 0 0 20px rgba(76, 175, 80, 0.6);
        border-color: rgba(76, 175, 80, 0.9);
    }
}

/* تأثير الانتقال بين الصفحات */
.page-transition {
    animation: pageSlideIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes pageSlideIn {
    0% {
        opacity: 0;
        transform: translateY(30px) scale(0.96);
        filter: blur(8px);
    }
    100% {
        opacity: 1;
        transform: translateY(0) scale(1);
        filter: blur(0);
    }
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

.profile-container {
    display: flex; justify-content: center; align-items: center; margin-top: 25px; margin-bottom: 25px;
    position: relative; z-index: 10;
}

.profile-container::before {
    content: ''; position: absolute; width: 155px; height: 155px; border-radius: 50%;
    border: 2px dashed #4CAF50; box-shadow: 0 0 20px rgba(76, 175, 80, 0.6); animation: spin 12s linear infinite;
}

.profile-container::after {
    content: ''; position: absolute; width: 185px; height: 185px; border-radius: 50%;
    background: conic-gradient(from 0deg, #4CAF50, transparent, #4CAF50, transparent);
    -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff calc(100% - 2px));
    mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff calc(100% - 2px));
    animation: spin-reverse 18s linear infinite;
}

@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
@keyframes spin-reverse { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }

.profile-img {
    width: 125px !important; height: 125px !important; border-radius: 50% !important;
    object-fit: cover !important; border: 3px solid #4CAF50 !important;
    box-shadow: 0px 0px 30px rgba(76, 175, 80, 0.8); position: relative; z-index: 2;
}

.title-animation {
    text-align: center; color: #ffffff; font-weight: 800; font-size: 30px;
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
    position: relative; z-index: 10;
}

.subtitle-animation {
    text-align: center; color: #4CAF50; font-size: 17px;
    text-shadow: 0 0 10px rgba(76, 175, 80, 0.4);
    position: relative; z-index: 10;
}

.social-container {
    display: flex; justify-content: center; align-items: center; gap: 20px; margin-top: 25px;
    position: relative; z-index: 10;
}

.social-btn {
    display: inline-flex; justify-content: center; align-items: center; width: 50px; height: 50px;
    border-radius: 50%; color: white; font-size: 24px; transition: all 0.4s ease; text-decoration: none;
}
.insta-btn { background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fd5949 45%, #d6249f 60%, #285AEB 90%); box-shadow: 0px 4px 15px rgba(214, 36, 159, 0.6); }
.snap-btn { background: #FFFC00; color: #000000; box-shadow: 0px 4px 15px rgba(255, 252, 0, 0.6); }
.threads-btn { background: #101010; color: #ffffff; border: 1px solid #333333; box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.25); }

/* بنر الماء المتحرك خلف بطاقة عني */
.water-banner-card {
    position: relative;
    background: linear-gradient(135deg, rgba(0, 119, 182, 0.25), rgba(76, 175, 80, 0.25)), rgba(15, 15, 15, 0.85);
    border: 1px solid rgba(0, 180, 216, 0.6);
    border-radius: 20px;
    padding: 30px;
    margin-top: 20px;
    box-shadow: 0 0 35px rgba(0, 150, 255, 0.3), inset 0 0 20px rgba(0, 180, 216, 0.2);
    overflow: hidden;
    backdrop-filter: blur(12px);
    animation: waterBannerGlow 4s ease-in-out infinite alternate;
    z-index: 10;
}

.water-banner-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
