import streamlit as st
import base64

# إعداد الصفحة وتصميم الخلفية مع تأثير مدار النجوم تماماً مثل المثال
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
                margin-bottom: 30px;
                position: relative;
            }
            
            /* حلقة النجوم/الجسيمات الدائرية المتحركة (تشبه الصورة تماماً) */
            .profile-container::before {
                content: '';
                position: absolute;
                width: 230px;
                height: 230px;
                border: 1px dotted rgba(255, 255, 255, 0.4);
                border-radius: 50%;
                animation: spin 20s linear infinite;
                box-shadow: 0 0 15px rgba(255, 255, 255, 0.05);
            }

            /* حلقة ثانية تدور بعكس الاتجاه لإعطاء عمق وكثافة تشبه النجوم */
            .profile-container::after {
                content: '';
                position: absolute;
                width: 250px;
                height: 250px;
                border: 2px dashed rgba(255, 255, 255, 0.15);
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
            
            /* تنسيق الصورة الدائرية في المنتصف */
            .profile-img {
                width: 190px !important;
                height: 190px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                border: 2px solid rgba(255, 255, 255, 0.2) !important;
                box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.9);
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

# اسم ملف الصورة (الصورة العادية أو المتحركة GIF)
image_filename = "IMG_20240908_230026_233.jpg"

try:
    img_base64 = get_image_base64(image_filename)
    img_format = "gif" if image_filename.endswith(".gif") else "jpeg"
    
    st.markdown(
        f'''
        <div class="profile-container">
            <img src="data:image/{img_format};base64,{img_base64}" class="profile-img" alt="Profile Picture">
        </div>
        ''',
        unsafe_allow_html=True
    )
except Exception as e:
    st.error("تعذر تحميل الصورة، تأكد من اسم الملف في المستودع.")

# النصوص المطلوبة بتنسيق أنيق
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 700; font-family: sans-serif;'>Welcome To My Account 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #999999; font-size: 18px; font-family: sans-serif;'>The links will be added soon.</p>", unsafe_allow_html=True)
