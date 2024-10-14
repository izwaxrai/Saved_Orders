import streamlit as st

st.title("🍟 Saved Orders 🍔")
st.header("Place your order")
phone_number = st.text_input("Enter your phone number")

orders_db = {}

def save_order(phone_number, order):
    orders_db[phone_number] = order
    return f"Order for {phone_number} saved!"

def get_saved_order(phone_number):
    return orders_db.get(phone_number, "No order found for this number.")


