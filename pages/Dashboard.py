import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏟️",
    layout="wide"
)

# -----------------------------
# LOGIN CHECK
# -----------------------------

if "user" not in st.session_state:
    st.error("Please Login First")
    st.stop()

user = st.session_state["user"]

# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 5px 12px rgba(0,0,0,0.18);
}

.title{
    font-size:42px;
    font-weight:bold;
    color:#0b3d91;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.markdown("<div class='title'>🏟️ StadiumSphere AI Dashboard</div>", unsafe_allow_html=True)

st.success(f"👋 Welcome, {user['name']}")

st.write(f"📧 **Email:** {user['email']}")

st.divider()

# -----------------------------
# QUICK STATS
# -----------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("🏟 Stadiums", "16")
c2.metric("⚽ Matches", "104")
c3.metric("👥 Fans", "5M+")
c4.metric("🤖 AI", "24/7")

st.divider()

st.subheader("🚀 Smart Stadium Services")

# -----------------------------
# ROW 1
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="card">
<h2>🎟️ Book Match Ticket</h2>
<p>Reserve your FIFA World Cup ticket.</p>
</div>
""", unsafe_allow_html=True)

    if st.button("Book Ticket", use_container_width=True):
        st.switch_page("pages/Book_Ticket.py")

with col2:

    st.markdown("""
<div class="card">
<h2>🎫 My Tickets</h2>
<p>View your booked tickets.</p>
</div>
""", unsafe_allow_html=True)

    if st.button("My Ticket", use_container_width=True):
        st.switch_page("pages/My_Ticket.py")

st.write("")

# -----------------------------
# ROW 2
# -----------------------------

col3, col4 = st.columns(2)

with col3:

    st.markdown("""
<div class="card">
<h2>🍔 Food Ordering</h2>
<p>Order food after entering the stadium.</p>
</div>
""", unsafe_allow_html=True)

    if st.button("Food Ordering", use_container_width=True):
        st.switch_page("pages/Food.py")

with col4:

    st.markdown("""
<div class="card">
<h2>🅿️ Parking</h2>
<p>Reserve your parking slot.</p>
</div>
""", unsafe_allow_html=True)

    if st.button("Parking", use_container_width=True):
        st.switch_page("pages/Parking.py")

st.write("")

# -----------------------------
# ROW 3
# -----------------------------

col5, col6 = st.columns(2)

with col5:

    st.markdown("""
<div class="card">
<h2>🤖 AI Assistant</h2>
<p>Chat with Gemini AI.</p>
</div>
""", unsafe_allow_html=True)

    if st.button("AI Assistant", use_container_width=True):
        st.switch_page("pages/AI_Assistant.py")

with col6:

    st.markdown("""
<div class="card">
<h2>🚪 Logout</h2>
<p>Sign out securely.</p>
</div>
""", unsafe_allow_html=True)

    if st.button("Logout", use_container_width=True):
        del st.session_state["user"]
        st.success("Logged out successfully!")
        st.switch_page("app.py")

st.divider()

