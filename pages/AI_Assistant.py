import streamlit as st
import google.generativeai as genai

# ===========================
# PAGE CONFIG
# ===========================

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 StadiumSphere AI Assistant")

st.write("Ask me anything about FIFA World Cup, stadiums, tickets, parking, food or travel.")

# ===========================
# LOGIN CHECK
# ===========================

if "user" not in st.session_state:
    st.error("Please Login First")
    st.stop()

user = st.session_state["user"]

st.success(f"Welcome {user['name']} 👋")

# ===========================
# GEMINI API
# ===========================

# Replace with your own Gemini API Key
GEMINI_API_KEY = ""

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ===========================
# CHAT HISTORY
# ===========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ===========================
# CHAT INPUT
# ===========================

prompt = st.chat_input("Ask your question...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = model.generate_content(f"""
You are StadiumSphere AI.

You are an intelligent FIFA World Cup Stadium Assistant.

Always answer politely.

You help users with:

• FIFA World Cup

• Stadium Information

• Match Schedules

• Ticket Booking

• Food Ordering

• Parking

• Stadium Rules

• Travel Tips

• Fan Safety

If the user asks anything unrelated to football or stadiums, politely answer it but encourage them to ask stadium-related questions too.

User Name:
{user['name']}

Question:
{prompt}
""")

                answer = response.text

            except Exception as e:

                answer = f"❌ Error:\n\n{e}"

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

# ===========================
# SIDEBAR
# ===========================

st.sidebar.title("🤖 AI Features")

st.sidebar.success("Powered by Google Gemini")

st.sidebar.write("""
✅ Ticket Help

✅ Stadium Guide

✅ Parking Support

✅ Food Suggestions

✅ Match Information

✅ FIFA Rules

✅ Travel Assistance
""")

if st.sidebar.button("🏠 Dashboard"):
    st.switch_page("pages/Dashboard.py")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()