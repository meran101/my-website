import streamlit as st
import base64

# إعداد الصفحة وتصميم الخلفية مع تأثير الحلقات المتحركة من حول الصورة الثابتة
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
            
            /* حاوية الصورة في المنتصف لتضمين التأثيرات من حولها */
            .profile-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 60px;
                margin-bottom: 50px;
                position: relative;
            }
            
            /* حلقة مدارية أولى متحركة تدور حول الصورة الثابتة */
            .profile-container::before {
                content: '';
                position: absolute;
                width: 230px;
                height: 230px;
                border: 1px dotted rgba(255, 255, 255, 0.4);
                border-radius: 50%;
                animation: spin 20s linear infinite;
            }

            /* حلقة مدارية ثانية تدور بعكس الاتجاه لإعطاء عمق وتأثير احترافي */
            .profile-container::after {
                content: '';
                position: absolute;
                width: 255px;
                height: 255px;
                border: 2px dashed rgba(76, 175, 80, 0.3);
                border-radius: 50%;
                animation: spin-reverse 30s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            @keyframes spin-reverse {
                0% { transform: rotate(360deg); }
                100% { transform: rotate(0deg); }
            }
            
            /* تنسيق الصورة الثابتة الدائرية في المنتصف مع إطار وتوهج خفيف */
            .profile-img {
                width: 190px !important;
                height: 190px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                border: 3px solid #4CAF50 !important;
                box-shadow: 0px 0px 25px rgba(76, 175, 80, 0.4);
                position: relative;
                z-index: 2;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# دالة لتحويل الصورة المحلية الثابتة إلى نسق Base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# استخدام الصورة الثابتة المرفوعة لديك
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
    st.error("تعذر تحميل الصورة، تأكد من اسم الملف في المستودع.")

# النصوص المطلوبة بتنسيق أنيق
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 700;'>Welcome To My Account 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a0a0a0; font-size: 18px;'>The links will be added soon.</p>", unsafe_allow_html=True)
