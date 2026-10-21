import streamlit as st
import base64

# إعداد الصفحة وتصميم الخلفية مع التأثيرات وأزرار التواصل الاجتماعي
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
            
            /* حاوية الصورة في المنتصف */
            .profile-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 40px;
                margin-bottom: 30px;
                position: relative;
            }
            
            /* خط دوران أخضر متصل يدور حول الصورة */
            .profile-container::before {
                content: '';
                position: absolute;
                width: 225px;
                height: 225px;
                border-radius: 50%;
                border: 3px solid transparent;
                border-top-color: #4CAF50;
                border-right-color: #4CAF50;
                animation: spin 1.5s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            /* تنسيق الصورة الثابتة الدائرية */
            .profile-img {
                width: 195px !important;
                height: 195px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                border: 3px solid #4CAF50 !important;
                box-shadow: 0px 0px 25px rgba(76, 175, 80, 0.3);
                position: relative;
                z-index: 2;
            }
            
            /* حاوية الأيقونات لتجاورها بجانب بعضها */
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
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# استدعاء مكتبة FontAwesome لأيقونات التواصل الاجتماعي
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)

# دالة لتحويل الصورة المحلية إلى نسق Base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# اسم ملف الصورة الثابتة
image_filename = "IMG_20240908_230026_233.jpg"

try:
    img_base64 = get_image_base64(image_filename)
    st.markdown(
        f'''
        <div class="profile-container">
            <img src="data:image/jpeg;base64,{img_base64}" class="profile-img" alt="Profile Picture">
        </div>
        ''',
        unsafe_allow_html=True
    )
except Exception as e:
    st.error("تعذر تحميل الصورة، تأكد من وجود اسم الملف بشكل صحيح في المستودع.")

# النصوص المطلوبة بتنسيق أنيق
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 700;'>Welcome To My Account 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a0a0a0; font-size: 18px;'>The links will be added soon.</p>", unsafe_allow_html=True)

# روابط إنستغرام وسناب شات
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
