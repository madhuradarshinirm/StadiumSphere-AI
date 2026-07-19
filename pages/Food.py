import streamlit as st

st.set_page_config(
    page_title="Food Ordering",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 Stadium Food Ordering")

# -----------------------
# LOGIN CHECK
# -----------------------

if "user" not in st.session_state:
    st.error("Please Login First")
    st.stop()

user = st.session_state["user"]

st.success(f"Welcome {user['name']} 👋")

st.info("🍽 Food ordering is available only after entering the stadium.")

inside = st.checkbox("✅ I have entered the stadium")

if inside:

    st.subheader("Choose Your Food")

    menu = {
        "🍕 Pizza": 350,
        "🍔 Burger": 250,
        "🌭 Hot Dog": 200,
        "🍟 French Fries": 150,
        "🍿 Popcorn": 180,
        "🥤 Coke": 100,
        "☕ Coffee": 120,
        "🍗 Chicken Wings": 450
    }

    total = 0
    order = []

    for item, price in menu.items():

        qty = st.number_input(
            f"{item} (₹{price})",
            min_value=0,
            max_value=10,
            value=0,
            key=item
        )

        if qty > 0:
            total += qty * price
            order.append((item, qty, price))

    st.divider()

    st.subheader("Delivery Details")

    seat = st.text_input("Seat Number")

    if order:

        st.subheader("Order Summary")

        for item, qty, price in order:
            st.write(f"{item} × {qty} = ₹{qty * price}")

        st.success(f"💰 Total Amount : ₹{total}")

        if st.button("Place Order", use_container_width=True):

            st.success("✅ Food Order Placed Successfully!")

            st.toast("🍔 Preparing your order...")

            st.toast(f"🪑 Delivering to Seat {seat}")

            st.balloons()

    else:

        st.warning("Select at least one item.")

else:

    st.warning("🚫 Food ordering will be enabled after stadium entry.")

st.divider()

if st.button("🏠 Back to Dashboard", use_container_width=True):
    st.switch_page("pages/Dashboard.py")