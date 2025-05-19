import streamlit as st
import hashlib
import json
import os

# File to store user credentials
USER_DATA_FILE = "users.json"

# Load user credentials
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as f:
        json.dump({}, f)

with open(USER_DATA_FILE, "r") as f:
    USER_CREDENTIALS = json.load(f)

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Save updated user credentials
def save_users():
    with open(USER_DATA_FILE, "w") as f:
        json.dump(USER_CREDENTIALS, f)

# Streamlit UI
st.title("🔐 Secure Login System")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

if menu == "Register":
    st.subheader("Create a New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    
    if st.button("Register"):
        if new_user in USER_CREDENTIALS:
            st.warning("⚠️ Username already exists. Choose a different one.")
        else:
            USER_CREDENTIALS[new_user] = hash_password(new_password)
            save_users()
            st.success("✅ Registration successful! You can now login.")

elif menu == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == hash_password(password):
            st.success(f"✅ Welcome, {username}!")
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
        else:
            st.error("❌ Invalid username or password.")
    
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        st.subheader(f"Hello, {st.session_state['username']}!")
        if st.button("Logout"):
            del st.session_state["logged_in"]
            del st.session_state["username"]
            st.rerun()
