import streamlit as st
import base64

# إعداد الصفحة وإخفاء الهيدر والفوتر وتطبيق الخلفية الداكنة الفخمة
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none !important;}
            div[data-testid="stDecoration"] {display: none !important;}
            
            /* خلفية الموقع الداكنة */
            .stApp {
                background-color: #080808;
                color: #ffffff;
            }
            
            /* حاوية الصورة في المنتصف تماماً */
            .profile-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 50px;
                margin-bottom: 30px;
            }
            
            /* تنسيق الصورة لضمان ظهور الحركة والوضوح */
            .profile-img {
                width: 220px !important;
                height: 220px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.8);
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# دالة لقراءة ملف الـ GIF المتحرك وتحويله بشكل سليم للمتصفح
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# اسم ملف الـ GIF المتحرك المرفوع في المستودع
image_filename = "unnamed.gif"

try:
    img_base64 = get_image_base64(image_filename)
    
    # عرض الصورة المتحركة عبر وسم HTML صريح لضمان استمرار الحركة
    st.markdown(
        f'''
        <div class="profile-container">
            <img src="data:image/gif;base64,{img_base64}" class="profile-img" alt="Animated Profile">
        </div>
        ''',
        unsafe_allow_html=True
    )
except Exception as e:
    st.error("تعذر تحميل ملف الـ GIF، تأكد من أن اسم الملف 'unnamed.gif' مرفوع بشكل صحيح في المستودع.")

# النصوص المطلوبة بدقة
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 700;'>Welcome To My Account 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a0a0a0; font-size: 18px;'>The links will be added soon.</p>", unsafe_allow_html=True)
