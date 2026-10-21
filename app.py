import streamlit as st
import base64

# إعداد حالة اللغة والتأثير الأولي في التخزين المؤقت
if "lang" not in st.session_state:
    st.session_state.lang = "en"

def toggle_language():
    if st.session_state.lang == "en":
        st.session_state.lang = "ar"
    else:
        st.session_state.lang = "en"

# إعداد التصميم وتأثير الإخفاء التلقائي عند فتح الموقع (Splash Screen)
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
            
            /* تأثير شاشة البداية (Splash Screen) التي تختفي بعد فتح الموقع */
            @keyframes splashFadeOut {
                0% {
                    opacity: 1;
                    visibility: visible;
                }
                80% {
                    opacity: 1;
                }
                100% {
                    opacity: 0;
                    visibility: hidden;
                    pointer-events: none;
                }
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

            /* نبض الشعار أو الاسم أثناء التحميل الأولي */
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
            
            /* حاوية الصورة الأساسية في الموقع */
            .profile-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 30px;
                margin-bottom: 30px;
                position: relative;
            }
            
            /* الحلقات المدارية المتوهجة */
            .profile-container::before {
                content: '';
                position: absolute;
                width: 235px;
                height: 235px;
                border-radius: 50%;
                border: 2px dashed rgba(76, 175, 80, 0.4);
                box-shadow: 0 0 20px rgba(76, 175, 80, 0.2), inset 0 0 20px rgba(76, 175, 80, 0.2);
                animation: spin 15s linear infinite;
            }

            .profile-container::after {
                content: '';
                position: absolute;
                width: 270px;
                height: 270px;
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
            
            /* تنسيق الصورة الثابتة الدائرية وتوهجها */
            .profile-img {
                width: 195px !important;
                height: 195px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                border: 3px solid #4CAF50 !important;
                box-shadow: 0px 0px 30px rgba(76, 175, 80, 0.4);
                position: relative;
                z-index: 2;
            }
            
            /* حاوية الأيقونات */
            .social-container {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 20px;
                margin-top: 25px;
            }
            
            /* تنسيق الأيقونات المشترك */
            .social-btn {
                display: inline-flex;
                justify-content: center;
                align-items: center;
                width: 50px;
                height: 50px;
                border-radius: 50%;
                color: white;
                font-size: 24px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                text-decoration: none;
            }
            
            /* زر إنستغرام */
            .insta-btn {
                background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
                box-shadow: 0px 4px 15px rgba(214, 36, 159, 0.4);
            }
            .insta-btn:hover {
                transform: scale(1.1);
                box-shadow: 0px 6px 20px rgba(214, 36, 159, 0.7);
            }

            /* زر سناب شات */
            .snap-btn {
                background: #FFFC00;
                color: #000000;
                box-shadow: 0px 4px 15px rgba(255, 252, 0, 0.4);
            }
            .snap-btn:hover {
                transform: scale(1.1);
                box-shadow: 0px 6px 20px rgba(255, 252, 0, 0.7);
            }
            
            /* تنسيق زر الترجمة */
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

# استدعاء مكتبة FontAwesome للأيقونات
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)

# دالة لتحويل الصورة إلى Base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

image_filename = "IMG_20240908_230026_233.jpg"

try:
    img_base64 = get_image_base64(image_filename)
    
    # عرض شاشة البداية المتوهجة التي تختفي تلقائياً عند فتح الموقع
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

# زر الترجمة في أعلى الصفحة
col1, col2 = st.columns([5, 1])
with col2:
    button_label = "العربية 🌐" if st.session_state.lang == "en" else "English 🌐"
    st.button(button_label, on_click=toggle_language)

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
    st.error("تعذر تحميل الصورة، تأكد من وجود الملف بشكل صحيح في المستودع.")

# تحديد النصوص حسب اللغة
if st.session_state.lang == "en":
    title_text = "Welcome To My Account 👋"
    subtitle_text = "My social media accounts"
else:
    title_text = "أهلاً بك في حسابي 👋"
    subtitle_text = "حساباتي على وسائل التواصل الاجتماعي"

# عرض النصوص
st.markdown(f"<h1 style='text-align: center; color: #ffffff; font-weight: 700;'>{title_text}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #a0a0a0; font-size: 18px;'>{subtitle_text}</p>", unsafe_allow_html=True)

# روابط التواصل
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
