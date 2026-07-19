import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="StadiumSphere AI",
    page_icon="🏟️",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.main{
    background:#f5f9ff;
}

.big-title{
    font-size:58px;
    font-weight:bold;
    color:#0b3d91;
}

.subtitle{
    font-size:22px;
    color:#555;
}

.feature-box{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.15);
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

col1, col2 = st.columns([1,4])

with col1:
    st.image("logo.png", width=120)

with col2:
    st.markdown("<div class='big-title'>🏟️ StadiumSphere AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Smart Stadium Experience for FIFA World Cup 2026</div>", unsafe_allow_html=True)

st.divider()

# ---------------- HERO ----------------

st.image("stadium.png", use_container_width=True)

st.success("⚽ Welcome to the Future of Smart Stadiums!")


# ---------------- LOGIN ----------------

st.subheader("Get Started")

c1, c2 = st.columns(2)

with c1:
    if st.button("🔐 Login", use_container_width=True):
        st.switch_page("pages/Login.py")

with c2:
    if st.button("📝 Signup", use_container_width=True):
        st.switch_page("pages/Signup.py")

st.divider()



# ---------------- MATCHES ----------------

st.subheader("⚽ Upcoming FIFA Matches")

try:
    matches = pd.read_csv("matches.csv")
    st.dataframe(matches, use_container_width=True)
except:
    st.warning("matches.csv not found.")

st.divider()


st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit, SQLite & Google Gemini AI

<br>

© 2026 StadiumSphere AI | FIFA World Cup

</div>
""", unsafe_allow_html=True)