import streamlit as st
import base64

# إعداد حالة اللغة والتسجيل في التخزين المؤقت
if "lang" not in st.session_state:
    st.session_state.lang = "en"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def toggle_language():
    if st.session_state.lang == "en":
        st.session_state.lang = "ar"
    else:
        st.session_state.lang = "en"

# إعداد التصميم وتأثيرات الواجهة
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none !important;}
            div[data-testid="stDecoration"] {display: none !important;}
            
            /* خلفية الموقع الداكنة الفخمة */
            .stApp {
                background-color: #080808;
                color: #ffffff;
            }
            
            /* تأثير شاشة البداية (Splash Screen) */
            @keyframes splashFadeOut {
                0% { opacity: 1; visibility: visible; }
                80% { opacity: 1; }
                100% { opacity: 0; visibility: hidden; pointer-events: none; }
            }

            .splash-screen {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background-color: #050505;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                z-index: 99999;
                animation: splashFadeOut 1.5s ease-in-out forwards;
            }

            .splash-logo {
                width: 90px;
                height: 90px;
                border-radius: 50%;
                border: 3px solid #4CAF50;
                box-shadow: 0 0 25px rgba(76, 175, 80, 0.6);
                animation: pulseLogo 1.2s infinite alternate;
                object-fit: cover;
                margin-bottom: 15px;
            }

            @keyframes pulseLogo {
                0% { transform: scale(0.9); box-shadow: 0 0 15px rgba(76, 175, 80, 0.4); }
                100% { transform: scale(1.1); box-shadow: 0 0 35px rgba(76, 175, 80, 0.8); }
            }

            .splash-text {
                color: #ffffff;
                font-size: 20px;
                font-weight: 600;
                letter-spacing: 2px;
            }
            
            /* حاوية الصورة الأساسية */
            .profile-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 20px;
                margin-bottom: 25px;
                position: relative;
            }
            
            .profile-container::before {
                content: '';
                position: absolute;
                width: 225px;
                height: 225px;
                border-radius: 50%;
                border: 2px dashed rgba(76, 175, 80, 0.4);
                box-shadow: 0 0 20px rgba(76, 175, 80, 0.2), inset 0 0 20px rgba(76, 175, 80, 0.2);
                animation: spin 15s linear infinite;
            }

            .profile-container::after {
                content: '';
                position: absolute;
                width: 255px;
                height: 255px;
                border-radius: 50%;
                background: conic-gradient(from 0deg, rgba(76, 175, 80, 0.6), transparent, rgba(76, 175, 80, 0.2), transparent);
                -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff calc(100% - 2px));
                mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff calc(100% - 2px));
                animation: spin-reverse 20s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            @keyframes spin-reverse {
                0% { transform: rotate(360deg); }
                100% { transform: rotate(0deg); }
            }
            
            .profile-img {
                width: 185px !important;
                height: 185px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                border: 3px solid #4CAF50 !important;
                box-shadow: 0px 0px 30px rgba(76, 175, 80, 0.4);
                position: relative;
                z-index: 2;
            }
            
            /* الأيقونات */
            .social-container {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 20px;
                margin-top: 20px;
                margin-bottom: 30px;
            }
            
            .social-btn {
                display: inline-flex;
                justify-content: center;
                align-items: center;
                width: 45px;
                height: 45px;
                border-radius: 50%;
                color: white;
                font-size: 22px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                text-decoration: none;
            }
            
            .insta-btn {
                background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
                box-shadow: 0px 4px 15px rgba(214, 36, 159, 0.4);
            }
            .insta-btn:hover { transform: scale(1.1); }

            .snap-btn {
                background: #FFFC00;
                color: #000000;
                box-shadow: 0px 4px 15px rgba(255, 252, 0, 0.4);
            }
            .snap-btn:hover { transform: scale(1.1); }
            
            /* تنسيق صندوق تسجيل الدخول الفخم */
            .login-box {
                background: rgba(20, 20, 20, 0.8);
                border: 1px solid rgba(76, 175, 80, 0.3);
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
                max-width: 400px;
                margin: 0 auto;
                backdrop-filter: blur(10px);
            }
            
            div.stButton > button {
                background-color: #1a1a1a !important;
                color: #ffffff !important;
                border: 1px solid #4CAF50 !important;
                border-radius: 20px !important;
                padding: 5px 15px !important;
                font-size: 14px !important;
                transition: all 0.3s ease !important;
            }
            div.stButton > button:hover {
                background-color: #4CAF50 !important;
                color: #ffffff !important;
                border-color: #4CAF50 !important;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)

# زر الترجمة في الأعلى
col1, col2 = st.columns([5, 1])
with col2:
    button_label = "العربية 🌐" if st.session_state.lang == "en" else "English 🌐"
    st.button(button_label, on_click=toggle_language)

# دالة تحويل الصورة
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

image_filename = "IMG_20240908_230026_233.jpg"

try:
    img_base64 = get_image_base64(image_filename)
    st.markdown(
        f'''
        <div class="splash-screen">
            <img src="data:image/jpeg;base64,{img_base64}" class="splash-logo" alt="Loading...">
            <div class="splash-text">Loading Website...</div>
        </div>
        ''',
        unsafe_allow_html=True
    )
except Exception as e:
    pass

try:
    st.markdown(
        f'''
        <div class="profile-container">
            <img src="data:image/jpeg;base64,{img_base64}" class="profile-img" alt="Profile Picture">
        </div>
        ''',
        unsafe_allow_html=True
    )
except Exception as e:
    st.error("تعذر تحميل الصورة.")

# النصوص حسب اللغة
if st.session_state.lang == "en":
    title_text = "Welcome To My Account 👋"
    subtitle_text = "My social media accounts"
    login_title = "Secure Member Access"
    user_label = "Username"
    pass_label = "Password"
    login_btn = "Login"
    success_msg = "Welcome back, Meran! Access Granted."
    error_msg = "Invalid credentials. Please try again."
else:
    title_text = "أهلاً بك في حسابي 👋"
    subtitle_text = "حساباتي على وسائل التواصل الاجتماعي"
    login_title = "تسجيل دخول الأعضاء"
    user_label = "اسم المستخدم"
    pass_label = "كلمة المرور"
    login_btn = "تسجيل الدخول"
    success_msg = "أهلاً بك مجدداً يا ميران! تم تسجيل الدخول بنجاح."
    error_msg = "بيانات الدخول غير صحيحة، حاول مجدداً."

st.markdown(f"<h1 style='text-align: center; color: #ffffff; font-weight: 700;'>{title_text}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #a0a0a0; font-size: 18px; margin-bottom: 10px;'>{subtitle_text}</p>", unsafe_allow_html=True)

# أيقونات التواصل الاجتماعي
instagram_url = "https://www.instagram.com/meran.alyas/?__pwa=1"
snapchat_url = "https://www.snapchat.com/add/meran.alyas"

st.markdown(
    f'''
    <div class="social-container">
        <a href="{instagram_url}" target="_blank" class="social-btn insta-btn" title="Instagram">
            <i class="fa-brands fa-instagram"></i>
        </a>
        <a href="{snapchat_url}" target="_blank" class="social-btn snap-btn" title="Snapchat">
            <i class="fa-brands fa-snapchat"></i>
        </a>
    </div>
    ''',
    unsafe_allow_html=True
)

# قسم تسجيل الدخول الفخم في الأسفل
st.markdown(f"<hr style='border-color: rgba(255,255,255,0.1); margin: 30px 0;'>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: #4CAF50; font-size: 20px; margin-bottom: 20px;'>{login_title}</h3>", unsafe_allow_html=True)

with st.container():
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        with st.form("login_form"):
            username = st.text_input(user_label)
            password = st.text_input(pass_label, type="password")
            submit = st.form_submit_button(login_btn)
            
            if submit:
                if username == "meran.alyas" and password == "12345":
                    st.success(success_msg)
                    st.session_state.logged_in = True
                else:
                    st.error(error_msg)
