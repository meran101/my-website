import streamlit as st
import base64

# إعداد حالة اللغة
if "lang" not in st.session_state:
    st.session_state.lang = "en"

def toggle_language():
    if st.session_state.lang == "en":
        st.session_state.lang = "ar"
    else:
        st.session_state.lang = "en"

# دالة تحويل الصورة
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except Exception:
        return ""

image_filename = "IMG_20240908_230026_233.jpg"

# ==================== الصفحة الأولى: الرئيسية ====================
def home_page():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display: none !important;}
    div[data-testid="stDecoration"] {display: none !important;}
    
    .stApp { background-color: #050505; color: #ffffff; }

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
        width: 110px; height: 110px; border-radius: 50%; border: 3px solid #4CAF50;
        box-shadow: 0 0 40px rgba(76, 175, 80, 0.9); animation: epicPulse 1.2s infinite alternate; object-fit: cover;
    }
    @keyframes epicPulse {
        0% { transform: scale(0.95); box-shadow: 0 0 20px rgba(76, 175, 80, 0.5); }
        100% { transform: scale(1.1); box-shadow: 0 0 50px rgba(76, 175, 80, 1); }
    }
    .splash-text { color: #4CAF50; font-size: 22px; font-weight: 700; letter-spacing: 3px; }

    @keyframes cinematicAppear {
        0% { opacity: 0; transform: translateY(50px) scale(0.85); filter: blur(10px); }
        100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
    }
    .profile-container {
        display: flex; justify-content: center; align-items: center; margin-top: 45px; margin-bottom: 30px;
        position: relative; animation: cinematicAppear 1.4s cubic-bezier(0.16, 1, 0.3, 1) 1.5s forwards; opacity: 0;
    }
    .profile-container::before {
        content: ''; position: absolute; width: 235px; height: 235px; border-radius: 50%;
        border: 3px dashed #4CAF50; box-shadow: 0 0 30px rgba(76, 175, 80, 0.6); animation: spin 12s linear infinite;
    }
    .profile-container::after {
        content: ''; position: absolute; width: 275px; height: 275px; border-radius: 50%;
        background: conic-gradient(from 0deg, #4CAF50, transparent, #4CAF50, transparent);
        -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 3px), #fff calc(100% - 3px));
        mask: radial-gradient(farthest-side, transparent calc(100% - 3px), #fff calc(100% - 3px));
        animation: spin-reverse 18s linear infinite;
    }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    @keyframes spin-reverse { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }

    .profile-img {
        width: 195px !important; height: 195px !important; border-radius: 50% !important;
        object-fit: cover !important; border: 4px solid #4CAF50 !important;
        box-shadow: 0px 0px 40px rgba(76, 175, 80, 0.7); position: relative; z-index: 2;
    }
    .title-animation {
        animation: cinematicAppear 1.4s cubic-bezier(0.16, 1, 0.3, 1) 1.8s forwards; opacity: 0;
        text-align: center; color: #ffffff; font-weight: 800; font-size: 36px;
    }
    .subtitle-animation {
        animation: cinematicAppear 1.4s cubic-bezier(0.16, 1, 0.3, 1) 2.1s forwards; opacity: 0;
        text-align: center; color: #4CAF50; font-size: 19px;
    }
    .social-container {
        display: flex; justify-content: center; align-items: center; gap: 25px; margin-top: 30px;
        animation: cinematicAppear 1.4s cubic-bezier(0.16, 1, 0.3, 1) 2.4s forwards; opacity: 0;
    }
    .social-btn {
        display: inline-flex; justify-content: center; align-items: center; width: 55px; height: 55px;
        border-radius: 50%; color: white; font-size: 26px; transition: all 0.4s ease; text-decoration: none;
    }
    .insta-btn { background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fd5949 45%, #d6249f 60%, #285AEB 90%); }
    .snap-btn { background: #FFFC00; color: #000000; }
    
    div.stButton > button {
        background-color: #121212 !important; color: #4CAF50 !important;
        border: 2px solid #4CAF50 !important; border-radius: 25px !important;
    }
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)

    col1, col2 = st.columns([5, 1])
    with col2:
        button_label = "العربية 🌐" if st.session_state.lang == "en" else "English 🌐"
        st.button(button_label, on_click=toggle_language)

    img_base64 = get_image_base64(image_filename)
    if img_base64:
        st.markdown(
            f'''
            <div class="splash-screen">
                <img src="data:image/jpeg;base64,{img_base64}" class="splash-logo" alt="Loading...">
                <div class="splash-text">LOADING...</div>
            </div>
            <div class="profile-container">
                <img src="data:image/jpeg;base64,{img_base64}" class="profile-img" alt="Profile Picture">
            </div>
            ''',
            unsafe_allow_html=True
        )

    if st.session_state.lang == "en":
        title_text, subtitle_text = "Welcome To My Account 👋", "My social media accounts"
    else:
        title_text, subtitle_text = "أهلاً بك في حسابي 👋", "حساباتي على وسائل التواصل الاجتماعي"

    st.markdown(f"<h1 class='title-animation'>{title_text}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='subtitle-animation'>{subtitle_text}</p>", unsafe_allow_html=True)

    instagram_url = "https://www.instagram.com/meran.alyas/?__pwa=1"
    snapchat_url = "https://www.snapchat.com/add/meran.alyas"

    st.markdown(
        f'''
        <div class="social-container">
            <a href="{instagram_url}" target="_blank" class="social-btn insta-btn"><i class="fa-brands fa-instagram"></i></a>
            <a href="{snapchat_url}" target="_blank" class="social-btn snap-btn"><i class="fa-brands fa-snapchat"></i></a>
        </div>
        ''',
        unsafe_allow_html=True
    )

# ==================== الصفحة الثانية: نبذة عني ====================
def about_page():
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>About Me / نبذة عني</h1>", unsafe_allow_html=True)
    if st.session_state.lang == "en":
        st.write("Welcome to my personal portfolio page! Here you can learn more about my skills, projects, and work.")
    else:
        st.write("مرحباً بك في صفحتي الشخصية! هنا يمكنك التعرف على مهاراتي، مشاريعي، واهتماماتي.")

# ==================== الصفحة الثالثة: التواصل ====================
def contact_page():
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Contact / التواصل</h1>", unsafe_allow_html=True)
    if st.session_state.lang == "en":
        st.write("Feel free to reach out via social media or send a direct message below:")
    else:
        st.write("تواصل معي عبر وسائل التواصل الاجتماعي أو أرسل رسالة مباشرة:")
    
    with st.form("contact_form"):
        name = st.text_input("Name / الاسم")
        email = st.text_input("Email / البريد الإلكتروني")
        message = st.text_area("Message / الرسالة")
        submit = st.form_submit_button("Send / إرسال")
        if submit:
            st.success("Message sent successfully! / تم إرسال الرسالة بنجاح!")

# ==================== إعداد وتفعيل القائمة الجانبية للتنقل بين الصفحات ====================
p1 = st.Page(home_page, title="Home / الرئيسية", icon="🏠")
p2 = st.Page(about_page, title="About / عني", icon="👤")
p3 = st.Page(contact_page, title="Contact / التواصل", icon="📩")

pg = st.navigation([p1, p2, p3])
pg.run()
