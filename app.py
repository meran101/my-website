import streamlit as st
import base64

# إعداد الصفحة وتصميم الخلفية مع تأثير الحلقات المدارية المتحركة باللون الأخضر
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
                margin-top: 50px;
                margin-bottom: 40px;
                position: relative;
            }
            
            /* حلقة مدارية أولى متوهجة باللون الأخضر */
            .profile-container::before {
                content: '';
                position: absolute;
                width: 235px;
                height: 235px;
                border-radius: 50%;
                background: conic-gradient(from 0deg, rgba(76, 175, 80, 0.8), transparent, rgba(76, 175, 80, 0.3), transparent);
                -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff calc(100% - 2px));
                mask: radial-gradient(farthest-side, transparent calc(100% - 2px), #fff calc(100% - 2px));
                animation: spin 15s linear infinite;
            }

            /* حلقة خارجية ثانية واسعة باللون الأخضر الخفيف */
            .profile-container::after {
                content: '';
                position: absolute;
                width: 270px;
                height: 270px;
                border-radius: 50%;
                border: 1px dashed rgba(76, 175, 80, 0.3);
                box-shadow: 0 0 20px rgba(76, 175, 80, 0.1), inset 0 0 20px rgba(76, 175, 80, 0.1);
                animation: spin-reverse 25s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            @keyframes spin-reverse {
                0% { transform: rotate(360deg); }
                100% { transform: rotate(0deg); }
            }
            
            /* تنسيق الصورة الثابتة الدائرية في المنتصف مع إطار أخضر وتوهج */
            .profile-img {
                width: 195px !important;
                height: 195px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                border: 2px solid #4CAF50 !important;
                box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.9), 0 0 15px rgba(76, 175, 80, 0.3);
                position: relative;
                z-index: 2;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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
    st.error("تعذر تحميل الصورة، تأكد من وجود ملف الصورة باسمه الصحيح في المستودع.")

# النصوص المطلوبة المحدثة
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 700;'>Welcome To My Account 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a0a0a0; font-size: 18px;'>The links will be added soon.</p>", unsafe_allow_html=True)
