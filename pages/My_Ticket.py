import streamlit as st
import qrcode
from io import BytesIO
from firebase_config import db

st.set_page_config(
    page_title="My Ticket",
    page_icon="🎫",
    layout="wide"
)

st.title("🎫 My FIFA World Cup Ticket")

# -------------------------
# Login Check
# -------------------------
if "user" not in st.session_state:
    st.error("Please login first.")
    st.stop()

user = st.session_state["user"]

# -------------------------
# Get Ticket from Firebase
# -------------------------
docs = (
    db.collection("tickets")
    .where("Email", "==", user["email"])
    .stream()
)

tickets = [doc.to_dict() for doc in docs]

if not tickets:
    st.warning("No tickets booked yet.")
    st.stop()

# Show latest ticket
ticket = tickets[-1]

st.success("✅ Ticket Found")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Ticket Details")

    st.write(f"**🎟 Ticket ID:** {ticket['Ticket ID']}")
    st.write(f"**👤 Name:** {ticket['Name']}")
    st.write(f"**📧 Email:** {ticket['Email']}")
    st.write(f"**📱 Phone:** {ticket['Phone']}")
    st.write(f"**⚽ Match:** {ticket['Match']}")
    st.write(f"**🏟 Stadium:** {ticket['Stadium']}")
    st.write(f"**📅 Date:** {ticket['Date']}")
    st.write(f"**⏰ Time:** {ticket['Time']}")
    st.write(f"**💺 Category:** {ticket['Category']}")
    st.write(f"**🎫 Tickets:** {ticket['Tickets']}")
    st.write(f"**💰 Amount:** ₹{ticket['Amount']}")

with col2:

    qr = qrcode.make(
        f"""
Ticket ID: {ticket['Ticket ID']}
Name: {ticket['Name']}
Match: {ticket['Match']}
Stadium: {ticket['Stadium']}
Date: {ticket['Date']}
Time: {ticket['Time']}
Category: {ticket['Category']}
"""
    )

    buf = BytesIO()
    qr.save(buf)

    st.image(buf)

    st.download_button(
        "⬇ Download QR",
        data=buf.getvalue(),
        file_name="ticket_qr.png",
        mime="image/png"
    )

st.divider()

st.success("🎉 Enjoy the FIFA World Cup!")