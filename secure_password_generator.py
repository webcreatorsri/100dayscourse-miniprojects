import streamlit as st
import random
import string
import pyperclip

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    if length < 4:
        st.error("Password length must be at least 4 characters")
        return ""
    
    char_sets = ""
    if use_uppercase:
        char_sets += string.ascii_uppercase
    if use_lowercase:
        char_sets += string.ascii_lowercase
    if use_digits:
        char_sets += string.digits
    if use_special:
        char_sets += "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    
    if not char_sets:
        st.error("Select at least one character type!")
        return ""
    
    password = random.choices(char_sets, k=length)
    return ''.join(password)

def check_strength(password):
    score = sum([
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(c in "!@#$%^&*()_+-=[]{}|;:',.<>?/" for c in password)
    ])
    
    if score == 4:
        return "🟢 Strong"
    elif score == 3:
        return "🟠 Medium"
    else:
        return "🔴 Weak"

st.title("🔑 Secure Password Generator")

length = st.slider("Select password length:", min_value=4, max_value=50, value=12)
use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
use_digits = st.checkbox("Include Numbers", value=True)
use_special = st.checkbox("Include Special Characters", value=True)

generate_btn = st.button("Generate Password")
if generate_btn:
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    if password:
        st.success(f"Generated Password: `{password}`")
        st.text(f"Strength: {check_strength(password)}")
        if st.button("Copy to Clipboard"):
            pyperclip.copy(password)
            st.success("Password copied!")

st.caption("🔒 Keep your passwords safe!")
