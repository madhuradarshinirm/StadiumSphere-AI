import streamlit as st
import pandas as pd
import uuid

from firebase_config import db
from email_service import send_ticket_email

st.set_page_config(
    page_title="Book Ticket",
    page_icon="🎟️",
    layout="wide"
)

st.title("🎟️ FIFA World Cup Ticket Booking")

# -------------------------
# Login Check
# -------------------------
if "user" not in st.session_state:
    st.error("Please login first.")
    st.stop()

user = st.session_state["user"]

# -------------------------
# Load Match Data
# -------------------------
matches = pd.read_csv("matches.csv")

match = st.selectbox(
    "⚽ Select Match",
    matches["Match"]
)

selected = matches[matches["Match"] == match].iloc[0]

stadium = selected["Stadium"]
date = selected["Date"]
time = selected["Time"]

st.info(f"🏟 Stadium : {stadium}")
st.info(f"📅 Date : {date}")
st.info(f"⏰ Time : {time}")

st.divider()

st.subheader("Passenger Details")

name = st.text_input(
    "Name",
    value=user["name"]
)

email = st.text_input(
    "Email",
    value=user["email"]
)

phone = st.text_input("Phone Number")

category = st.selectbox(
    "Seat Category",
    [
        "VIP",
        "Premium",
        "Gold",
        "Silver",
        "Economy"
    ]
)

ticket_count = st.number_input(
    "Number of Tickets",
    min_value=1,
    max_value=10,
    value=1
)

price = {
    "VIP": 10000,
    "Premium": 7000,
    "Gold": 5000,
    "Silver": 3000,
    "Economy": 1500
}

amount = price[category] * ticket_count

st.success(f"💰 Total Amount : ₹{amount}")

# -------------------------
# Book Ticket
# -------------------------
if st.button("🎟️ Confirm Booking", use_container_width=True):

    ticket = {
        "Ticket ID": str(uuid.uuid4())[:8].upper(),
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Match": match,
        "Stadium": stadium,
        "Date": date,
        "Time": time,
        "Category": category,
        "Tickets": ticket_count,
        "Amount": amount
    }

    # Save ticket to Firebase
    db.collection("tickets").add(ticket)

    # Send confirmation email
    try:
        send_ticket_email(email, ticket)
        st.success("📧 Confirmation email sent successfully!")
    except Exception as e:
        st.warning(f"Email could not be sent: {e}")

    # Save last ticket in session
    st.session_state["last_ticket"] = ticket

    st.success("✅ Ticket Booked Successfully!")

    st.balloons()

    st.switch_page("pages/My_Ticket.py")