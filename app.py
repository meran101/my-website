import streamlit as st
import base64

# إعداد الصفحة وإخفاء الهيدر والفوتر وشعار Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none !important;}
            div[data-testid="stDecoration"] {display: none !important;}
            
            /* تنسيق الحاوية لتكون الصورة في المنتصف تماماً */
            .profile-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 30px;
                margin-bottom: 25px;
            }
            
            /* جعل الصورة دائرية تماماً مع إطار أنيق */
            .profile-img {
                width: 190px !important;
                height: 190px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                border: 4px solid #4CAF50 !important;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.15) !important;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# دالة لتحويل الصورة المحلية إلى نسق Base64 لضمان عرضها ودائريتها
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# اسم ملف الصورة المرفوع لديك في المستودع
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

# النصوص والعناوين المحدثة
st.markdown("<h1 style='text-align: center;'>Welcome To My Account 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>The links will be added soon.</p>", unsafe_allow_html=True)
