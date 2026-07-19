import streamlit as st
from firebase_config import db

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Login")

email = st.text_input("📧 Email")
password = st.text_input("🔒 Password", type="password")

if st.button("Login", use_container_width=True):

    docs = db.collection("users").where("email", "==", email).stream()

    user = None

    for doc in docs:
        data = doc.to_dict()

        if data["password"] == password:
            user = data
            break

    if user:

        st.session_state["user"] = user

        st.success(f"Welcome {user['name']} 🎉")

        st.switch_page("pages/Dashboard.py")

    else:

        st.error("Invalid Email or Password")