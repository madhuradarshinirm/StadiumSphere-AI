import streamlit as st
from firebase_config import db

st.set_page_config(page_title="Signup", page_icon="📝")

st.title("📝 Create Account")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

if st.button("Create Account"):

    if not name or not email or not password:
        st.error("Please fill all fields.")

    elif password != confirm:
        st.error("Passwords do not match.")

    else:

        users = db.collection("users").where("email", "==", email).stream()

        if list(users):
            st.error("Email already exists.")

        else:

            db.collection("users").add({
                "name": name,
                "email": email,
                "password": password
            })

            st.success("✅ Account Created Successfully!")
            st.balloons()