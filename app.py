import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="موقعي الشخصي", page_icon="👤", layout="centered")

# --- كود إخفاء الشعار والقوائم وشريط الاستضافة بالكامل ---
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
            /* إخفاء شعار Hosted with Streamlit في الأسفل */
            div[data-testid="stToolbar"] {visibility: hidden;}
            footer {visibility: hidden !important;}
            .viewerBadge_container__1QSob {display: none !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- باقي الكود كما هو ---
st.title("👋 مرحباً بك في موقعي!")
st.subheader("مطور تطبيقات ومبرمج")

st.markdown("""
### 📝 نبذة عني (Bio):
مرحباً! أنا ميران، مهتم بتطوير البرمجيات وتحليل البيانات وبناء التطبيقات باستخدام Python وStreamlit. 
أسعى دائماً لتعلم كل ما هو جديد في عالم التكنولوجيا وتقديم حلول برمجة مبتكرة.
""")

st.divider()

st.header("🛠️ المهارات")
st.write("- **لغات البرمجة:** Python, HTML, CSS")
st.write("- **الأدوات والمنصات:** Streamlit, GitHub, VS Code")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.link_button("🌐 حسابي على GitHub", "https://github.com/meran101")

with col2:
    st.link_button("📧 البريد الإلكتروني", "mailto:laptop132ootm@gmail.com")