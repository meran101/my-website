import streamlit as st

# 1. إعدادات عنوان الصفحة والأيقونة
st.set_page_config(
    page_title="موقعي الشخصي",
    page_icon="💻",
    layout="centered"
)

# 2. تصميم الواجهة والمعلومات
st.title("مرحباً بك في موقعي الشخصي! 👋")

st.divider()  # خط فاصل أنيق

# 3. قسم الروابط (أزرار الحسابات)
st.subheader("🔗 روابط التواصل الاجتماعي:")

# استبدل الروابط أدناه بروابط حساباتك الحقيقية
st.link_button("حسابي على إنستغرام (Instagram)", "https://www.instagram.com/meran.alyas/?__pwa=1")
st.link_button("قناتي على تيليجرام (Telegram)", "https://t.me/your_username")

st.divider()

# --- قسم البايو والمعلومات الشخصية ---
st.title("👋 مرحباً بك في موقعي!")
st.subheader("مطور تطبيقات ومبرمج")

st.markdown("""
### 📝 نبذة عني (Bio):
مرحباً! أنا ميران، مهتم بتطوير البرمجيات وتحليل البيانات وبناء التطبيقات باستخدام Python وStreamlit. 
أسعى دائماً لتعلم كل ما هو جديد في عالم التكنولوجيا وتقديم حلول برمجة مبتكرة.
""")

st.divider() # خط فاصل

# --- قسم المهارات والمشاريع ---
st.header("🛠️ المهارات")
st.write("- **لغات البرمجة:** Python, HTML, CSS")
st.write("- **الأدوات والمنصات:** Streamlit, GitHub, VS Code")

st.divider()

with col1:
    st.link_button("🌐 حسابي على GitHub", "https://github.com/meran101")

with col2:
    st.link_button("📧 البريد الإلكتروني", "mailto:laptop132ootm@gmail.com")import streamlit as stimport streamlit as st

# كود إخفاء الشعار والقوائم بالكامل
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppHeader {display: none;}
            .stAppFooter {display: none;}
            [data-testid="stHeader"] {display: none;}
            [data-testid="stStatusWidget"] {display: none;}
            #stDecoration {display: none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)