import streamlit as st

# إعداد الصفحة وإخفاء العلامة المائية
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none !important;}
            div[data-testid="stDecoration"] {display: none !important;}
            
            /* تنسيق الصورة لتكون دائرية وفي المنتصف */
            .profile-img-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 20px;
                margin-bottom: 20px;
            }
            .profile-img-container img {
                width: 180px;
                height: 180px;
                border-radius: 50%;
                object-fit: cover;
                border: 4px solid #4CAF50; /* لون الإطار حول الصورة (اختياري) */
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# عرض الصورة بشكل دائري في المنتصف
# (استبدل الرابط أدناه برابط صورتك المباشر أو اسم صورتك المرفوعة مثل "my_photo.jpg")
image_url = "https://images.unsplash.com/photo-1534528741775-53994a69daeb"

st.markdown(f"""
    <div class="profile-img-container">
        <img src="{image_url}" alt="Profile Picture">
    </div>
""", unsafe_allow_html=True)

# عنوان الموقع والنصوص
st.markdown("<h1 style='text-align: center;'>أهلاً بك في موقعي الشخصي 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>هذا هو موقعي المصمم بكل حب!</p>", unsafe_allow_html=True)
