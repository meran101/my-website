import streamlit as st

# 1. إعدادات عنوان الصفحة والأيقونة
st.set_page_config(
    page_title="موقعي الشخصي",
    page_icon="💻",
    layout="centered"
)

# 2. تصميم الواجهة والمعلومات
st.title("مرحباً بك في موقعي الشخصي! 👋")
st.write("أنا أتعلم البرمجة بايثون، وهذه هي صفحتي التي تضم حساباتي على منصات التواصل الاجتماعي.")

st.divider()  # خط فاصل أنيق

# 3. قسم الروابط (أزرار الحسابات)
st.subheader("🔗 روابط التواصل الاجتماعي:")

# استبدل الروابط أدناه بروابط حساباتك الحقيقية
st.link_button("حسابي على لينكد إن (LinkedIn)", "https://www.linkedin.com")
st.link_button("حسابي على إكس / تويتر (X)", "https://www.x.com")
st.link_button("حسابي على إنستغرام (Instagram)", "https://www.instagram.com")
st.link_button("قناتي على تيليجرام (Telegram)", "https://t.me/your_username")

st.divider()

# 4. تذييل الصفحة
st.caption("تم إنشاء هذا الموقع بكل فخر باستخدام لغة بايثون 🐍 ومكتبة Streamlit")