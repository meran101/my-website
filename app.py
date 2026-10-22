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

/* إخفاء الشعار والشريط السفلي بالكامل نهائياً */
footer, 
.viewerBadge_container__16336, 
.viewerBadge_link__1S137, 
[data-testid="stToolbar"], 
[data-testid="stStatusWidget"],
div[class*="viewerBadge"],
div[class*="stAppViewerBadge"] {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    height: 0 !important;
    width: 0 !important;
    pointer-events: none !important;
}

/* إلغاء المسافات والهوامش العلوية لرفع المحتوى للأعلى */
.stMainBlockContainer, .block-container {
    padding-top: 0.8rem !important;
    padding-bottom: 1rem !important;
}

/* خلفية الموقع الأساسية */
.stApp {
    background-color: #050505;
    color: #ffffff;
}

/* طبقة المطر المائي والعميق */
.matrix-rain {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 1;
    overflow: hidden;
    opacity: 0.6;
}

.matrix-column {
    position: absolute;
    top: -50%;
    width: 2px;
    height: 120px;
    background: linear-gradient(180deg, transparent, #00b4d8, #0077b6);
    box-shadow: 0 0 8px rgba(0, 150, 255, 0.9), 0 0 3px rgba(0, 212, 255, 0.7);
    animation: rainFall linear infinite;
}

@keyframes rainFall {
    0% { transform: translateY(-120px); }
    100% { transform: translateY(120vh); }
}

/* ضمان بقاء الأزرار في صف أفقي واحد بجانب بعضها تماماً */
div[data-testid="horizontal-block"], 
div.row-widget.stHorizontal, 
[data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 10px !important;
    align-items: center !important;
    width: 100% !important;
}

div[data-testid="column"], 
[data-testid="stColumn"] {
    flex: 1 1 0% !important;
    min-width: 0 !important;
    max-width: 100% !important;
}

/* تصميم احترافي وعصري للأزرار */
div.stButton > button {
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.6)) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(0, 180, 216, 0.3) !important;
    border-radius: 14px !important;
    padding: 8px 12px !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    width: 100% !important;
    backdrop-filter: blur(12px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0, 119, 182, 0.9), rgba(0, 180, 216, 0.7)) !important;
    color: #ffffff !important;
    border-color: rgba(0, 212, 255, 0.9) !important;
    box-shadow: 0 0 25px rgba(0, 180, 216, 0.6), inset 0 1px 2px rgba(255, 255, 255, 0.3) !important;
    transform: translateY(-2px) scale(1.02);
}

div.stButton > button:active {
    transform: translateY(0) scale(0.98) !important;
}

/* تأثير الانتقال بين الصفحات */
.page-transition {
    animation: pageSlideIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes pageSlideIn {
    0% {
        opacity: 0;
        transform: translateY(20px) scale(0.97);
        filter: blur(6px);
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
    border: 3px solid #00b4d8; box-shadow: 0 0 30px rgba(0, 180, 216, 0.9);
    animation: epicPulse 1.2s infinite alternate; object-fit: cover; margin-bottom: 20px;
}

@keyframes epicPulse {
    0% { transform: scale(0.95); box-shadow: 0 0 15px rgba(0, 150, 255, 0.5); }
    100% { transform: scale(1.1); box-shadow: 0 0 35px rgba(0, 212, 255, 1); }
}

.splash-text {
    color: #00b4d8; font-size: 20px; font-weight: 700; letter-spacing: 3px;
}

.profile-container {
    display: flex; justify-content: center; align-items: center; margin-top: 15px; margin-bottom: 20px;
    position: relative; z-index: 10;
}

.profile-container::before {
    content: ''; position: absolute; width: 155px; height: 155px; border-radius: 50%;
    border: 2px dashed #00b4d8; box-shadow: 0 0 20px rgba(0, 180, 216, 0.6); animation: spin 12s linear infinite;
}

.profile-container::after {
    content: ''; position: absolute; width: 185px; height: 185px; border-radius: 50%;
    background: conic-gradient(from 0deg, #00b4d8, transparent, #0077b6, transparent);
    -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff calc(100% - 2px));
    mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff calc(100% - 2px));
    animation: spin-reverse 18s linear infinite;
}

@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
@keyframes spin-reverse { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }

.profile-img {
    width: 125px !important; height: 125px !important; border-radius: 50% !important;
    object-fit: cover !important; border: 3px solid #00b4d8 !important;
    box-shadow: 0px 0px 30px rgba(0, 180, 216, 0.8); position: relative; z-index: 2;
}

.title-animation {
    text-align: center; color: #ffffff; font-weight: 800; font-size: 26px;
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
    position: relative; z-index: 10;
}

.subtitle-animation {
    text-align: center; color: #00b4d8; font-size: 15px;
    text-shadow: 0 0 10px rgba(0, 180, 216, 0.4);
    position: relative; z-index: 10;
}

.social-container {
    display: flex; justify-content: center; align-items: center; gap: 20px; margin-top: 20px;
    position: relative; z-index: 10;
}

.social-btn {
    display: inline-flex; justify-content: center; align-items: center; width: 45px; height: 45px;
    border-radius: 50%; color: white; font-size: 22px; transition: all 0.4s ease; text-decoration: none;
}
.insta-btn { background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fd5949 45%, #d6249f 60%, #285AEB 90%); box-shadow: 0px 4px 15px rgba(214, 36, 159, 0.6); }
.snap-btn { background: #FFFC00; color: #000000; box-shadow: 0px 4px 15px rgba(255, 252, 0, 0.6); }
.threads-btn { background: #101010; color: #ffffff; border: 1px solid #333333; box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.25); }

/* بنر الماء المتحرك خلف بطاقة عني */
.water-banner-card {
    position: relative;
    background: linear-gradient(135deg, rgba(0, 119, 182, 0.3), rgba(0, 180, 216, 0.15)), rgba(15, 15, 15, 0.85);
    border: 1px solid rgba(0, 180, 216, 0.6);
    border-radius: 20px;
    padding: 25px;
    margin-top: 15px;
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
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(0, 212, 255, 0.2) 0%, transparent 70%);
    animation: waterRippleMove 8s linear infinite;
    z-index: 0;
    pointer-events: none;
}

@keyframes waterBannerGlow {
    0% { box-shadow: 0 0 25px rgba(0, 150, 255, 0.25), inset 0 0 15px rgba(0, 180, 216, 0.15); }
    100% { box-shadow: 0 0 45px rgba(0, 212, 255, 0.5), inset 0 0 30px rgba(0, 119, 182, 0.3); }
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

# توليد خطوط المطر المائي
rain_html = '<div class="matrix-rain">'
for i in range(35):
    left_pos = i * 3
    anim_duration = 0.8 + (i % 5) * 0.3
    anim_delay = (i % 7) * 0.4
    rain_html += f'<div class="matrix-column" style="left: {left_pos}%; animation-duration: {anim_duration}s; animation-delay: {anim_delay}s;"></div>'
rain_html += '</div>'

st.markdown(rain_html, unsafe_allow_html=True)
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

st.markdown("<hr style='border-color: rgba(0, 180, 216, 0.25); margin-top: 10px; margin-bottom: 15px; position: relative; z-index: 10;'>", unsafe_allow_html=True)

st.markdown('<div class="page-transition">', unsafe_allow_html=True)

if st.session_state.current_page == "home":
    img_b64 = get_image_base64(image_filename)
    if img_b64:
        st.markdown(f'<div class="splash-screen"><img src="data:image/jpeg;base64,{img_b64}" class="splash-logo" alt="Loading..."><div class="splash-text">LOADING WEBSITE...</div></div><div class="profile-container"><img src="data:image/jpeg;base64,{img_b64}" class="profile-img" alt="Profile Picture"></div>', unsafe_allow_html=True)

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
        st.markdown("<h2 style='text-align: center; color: #00b4d8; position: relative; z-index: 10;'>نبذة عني 👤</h2>", unsafe_allow_html=True)
        st.markdown('<div class="water-banner-card"><div class="water-content"><p style="font-size: 20px; font-weight: 700; color: #00b4d8; letter-spacing: 1px; margin: 0;">🤖 Owner of TIGER Bot 🐅</p></div></div>', unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align: center; color: #00b4d8; position: relative; z-index: 10;'>About Me 👤</h2>", unsafe_allow_html=True)
        st.markdown('<div class="water-banner-card"><div class="water-content"><p style="font-size: 20px; font-weight: 700; color: #00b4d8; letter-spacing: 1px; margin: 0;">🤖 Owner of TIGER Bot 🐅</p></div></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
