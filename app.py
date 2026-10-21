import streamlit as st
import base64

# إعداد الصفحة وتطبيق خلفية داكنة وتأثيرات الحركة والدوران للإطار
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none !important;}
            div[data-testid="stDecoration"] {display: none !important;}
            
            /* خلفية الموقع الداكنة (مثل المثال) */
            .stApp {
                background-color: #0b0b0b;
                color: #ffffff;
            }
            
            /* تنسيق الحاوية في المنتصف */
            .profile-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 40px;
                margin-bottom: 30px;
                position: relative;
            }
            
            /* حلقة متحركة تدور حول الصورة تماماً مثل المثال */
            .profile-container::after {
                content: '';
                position: absolute;
                width: 215px;
                height: 215px;
                border: 2px dashed rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                animation: spin 15s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            /* تنسيق الصورة الدائرية الداخلية */
            .profile-img {
                width: 190px !important;
                height: 190px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                border: 3px solid rgba(255, 255, 255, 0.1) !important;
                box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.8);
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# دالة لتحويل الصورة المحلية إلى نسق Base64 (سواء كانت صورة عادية أو متحركة GIF)
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# إذا كنت تريد استخدام الصورة المتحركة ضع اسم ملف الـ GIF هنا، أو الصورة العادية
image_filename = "unnamed.gif"  # أو ضع اسم صورتك الأخرى هنا

try:
    img_base64 = get_image_base64(image_filename)
    
    # تحديد نوع الصيغة تلقائياً (gif أو jpeg)
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

# النصوص المطلوبة بتنسيق أنيق ومتناسق مع الخلفية الداكنة
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 700;'>Welcome To My Account 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a0a0a0; font-size: 18px;'>The links will be added soon.</p>", unsafe_allow_html=True)
