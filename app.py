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

/* تخصيص زر عني (About) ليحتوي على تأثير وخلفية مائية فخمة ومتحركة */
div[data-testid="column"]:nth-child(2) div.stButton > button {
    background: linear-gradient(135deg, rgba(0, 119, 182, 0.6), rgba(0, 180, 216, 0.3)), rgba(18, 18, 18, 0.9) !important;
    border: 1px solid rgba(0, 212, 255, 0.8) !important;
    color: #00d4ff !important;
    box-shadow: 0 0 20px rgba(0, 150, 255, 0.5), inset 0 0 10px rgba(0, 212, 255, 0.4) !important;
    animation: waterButtonPulse 3s ease-in-out infinite alternate;
}

div[data-testid="column"]:nth-child(2) div.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0, 180, 216, 0.8), rgba(76, 175, 80, 0.6)) !important;
    color: #ffffff !important;
    border-color: #00d4ff !important;
    box-shadow: 0 0 30px rgba(0, 212, 255, 0.9) !important;
}

@keyframes waterButtonPulse {
    0% { box-shadow: 0 0 15px rgba(0, 150, 255, 0.4), inset 0 0 8px rgba(0, 212, 255, 0.3); }
    100% { box-shadow: 0 0 25px rgba(0, 212, 255, 0.8), inset 0 0 15px rgba(76, 175, 80, 0.4); }
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

.water-profile-wrapper {
    position: relative; width: 145px; height: 145px; border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    background: radial-gradient(circle, rgba(0, 180, 216, 0.5) 0%, rgba(76, 175, 80, 0.3) 60%, transparent 80%);
    box-shadow: 0 0 30px rgba(0, 150, 255, 0.6), inset 0 0 20px rgba(0, 212, 255, 0.5);
    animation: waterIconPulse 3s ease-in-out infinite alternate;
}

.water-profile-wrapper::before {
    content: ''; position: absolute; width: 155px; height: 155px; border-radius: 50%;
    border: 2px dashed rgba(0, 212, 255, 0.7); animation: spin 12s linear infinite;
}

.water-profile-wrapper::after {
    content: ''; position: absolute; width: 175px; height: 175px; border-radius: 50%;
    background: conic-gradient(from 0deg, #00d4ff, transparent, #4CAF50, transparent, #00d4ff);
    -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff calc(100% - 2px));
    mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff calc(100% - 2px));
    animation: spin-reverse 15s linear infinite;
}

@keyframes waterIconPulse {
    0% { box-shadow: 0 0 20px rgba(0, 150, 255, 0.4), inset 0 0 15px rgba(0, 212, 255, 0.3); transform: scale(0.98); }
    100% { box-shadow: 0 0 45px rgba(0, 212, 255, 0.8), inset 0 0 30px rgba(76, 175, 80, 0.5); transform: scale(1.03); }
}

@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
@keyframes spin-reverse { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }

.profile-img {
    width: 125px !important; height: 125px !important; border-radius: 50% !important;
    object-fit: cover !important; border: 3px solid #00d4ff !important;
    box-shadow: 0px 0px 25px rgba(0, 212, 255, 0.8); position: relative; z-index: 2;
}

.title-animation {
    animation: epicEntrance 1.4s cubic-bezier(0.16, 1, 0.3, 1) 1.5s forwards; opacity: 0;
    text-align: center; color: #ffffff; font-weight: 800; font-size: 30px;
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
}

.subtitle-animation {
    animation: epicEntrance 1.4s cubic-bezier(0.16, 1, 0.3, 1) 1.8s forwards; opacity: 0;
    text-align: center; color: #4CAF50; font-size: 17px;
    text-shadow: 0 0 10px rgba(76, 175, 80, 0.4);
}

.social-container {
    display: flex; justify-content: center; align-items: center; gap: 20px; margin-top: 25px;
    animation: epicEntrance 1.4s cubic-bezier(0.16, 1, 0.3, 1) 2.1s forwards; opacity: 0;
}

.social-btn {
    display: inline-flex; justify-content: center; align-items: center; width: 50px; height: 50px;
    border-radius: 50%; color: white; font-size: 24px; transition: all 0.4s ease; text-decoration: none;
}
.insta-btn { background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fd5949 45%, #d6249f 60%, #285AEB 90%); box-shadow: 0px 4px 15px rgba(214, 36, 159, 0.6); }
.snap-btn { background: #FFFC00; color: #000000; box-shadow: 0px 4px 15px rgba(255, 252, 0, 0.6); }
.threads-btn { background: #101010; color: #ffffff; border: 1px solid #333333; box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.25); }

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
}

.water-banner-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(0, 212, 255, 0.15) 0%, transparent 70%);
    animation: waterRippleMove 8s linear infinite;
    z-index: 0;
    pointer-events: none;
}

@keyframes waterBannerGlow {
    0% { box-shadow: 0 0 25px rgba(0, 150, 255, 0.25), inset 0 0 15px rgba(0, 180, 216, 0.15); }
    100% { box-shadow: 0 0 45px rgba(0, 212, 255, 0.5), inset 0 0 30px rgba(76, 175, 80, 0.3); }
}

@keyframes waterRippleMove {
    0% { transform: translate(0, 0) rotate(0deg); }
    50% { transform: translate(10px, 15px) rotate(180deg); }
    100% { transform: translate(0, 0) rotate(360deg); }
}

.water-content {
    position: relative;
    z-index: 1;
    text-align: center;
}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">', unsafe_allow_html=True)

def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except Exception:
        return ""

image_filename = "IMG_20240908_230026_233.jpg"

col1, col2, col3 = st.columns(3)

with col1:
    btn_home = "🏠 الرئيسية" if st.session_state.lang == "ar" else "🏠 Home"
    st.button(btn_home, on_click=set_page, args=("home",), key="btn_h")

with col2:
    btn_about = "👤 عني" if st.session_state.lang == "ar" else "👤 About"
    st.button(btn_about, on_click=set_page, args=("about",), key="btn_a")

with col3:
    btn_lang = "العربية 🌐" if st.session_state.lang == "en" else "English 🌐"
    st.button(btn_lang, on_click=toggle_language, key="btn_l")

st.markdown("<hr style='border-color: rgba(76,175,80,0.25); margin-top: 15px; margin-bottom: 25px;'>", unsafe_allow_html=True)

if st.session_state.current_page == "home":
    img_b64 = get_image_base64(image_filename)
    if img_b64:
        st.markdown(f'<div class="splash-screen"><img src="data:image/jpeg;base64,{img_b64}" class="splash-logo" alt="Loading..."><div class="splash-text">LOADING WEBSITE...</div></div><div class="profile-container"><div class="water-profile-wrapper"><img src="data:image/jpeg;base64,{img_b64}" class="profile-img" alt="Profile Picture"></div></div>', unsafe_allow_html=True)

    if st.session_state.lang == "en":
        title_text, sub_text = "Welcome To My Account 👋", "My social media accounts"
    else:
        title_text, sub_text = "أهلاً بك في حسابي 👋", "حساباتي على وسائل التواصل الاجتماعي"

    st.markdown(f"<h1 class='title-animation'>{title_text}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='subtitle-animation'>{sub_text}</p>", unsafe_allow_html=True)

    url_insta = "https://www.instagram.com/meran.alyas/?__pwa=1"
    url_snap = "https://www.snapchat.com/add/meran.alyas"
    url_threads = "https://www.threads.net/@meran.alyas"

    social_html = f'''
    <div class="social-container">
        <a href="{url_insta}" target="_blank" class="social-btn insta-btn" title="Instagram"><i class="fa-brands fa-instagram"></i></a>
        <a href="{url_snap}" target="_blank" class="social-btn snap-btn" title="Snapchat"><i class="fa-brands fa-snapchat"></i></a>
        <a href="{url_threads}" target="_blank" class="social-btn threads-btn" title="Threads"><i class="fa-brands fa-threads"></i></a>
    </div>
    '''
    st.markdown(social_html, unsafe_allow_html=True)

elif st.session_state.current_page == "about":
    if st.session_state.lang == "ar":
        st.markdown("<h2 style='text-align: center; color: #4CAF50;'>نبذة عني 👤</h2>", unsafe_allow_html=True)
        st.markdown('<div class="water-banner-card"><div class="water-content"><p style="font-size: 20px; font-weight: 700; color: #4CAF50; letter-spacing: 1px; margin: 0;">🤖 Owner of TIGER Bot 🐅</p></div></div>', unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align: center; color: #4CAF50;'>About Me 👤</h2>", unsafe_allow_html=True)
        st.markdown('<div class="water-banner-card"><div class="water-content"><p style="font-size: 20px; font-weight: 700; color: #4CAF50; letter-spacing: 1px; margin: 0;">🤖 Owner of TIGER Bot 🐅</p></div></div>', unsafe_allow_html=True)
