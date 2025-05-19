import streamlit as st
import datetime
import pandas as pd
import numpy as np
import time

# Initialize Session State
if "counter" not in st.session_state:
    st.session_state.counter = 0
    st.session_state.click_history = []  # Stores timestamped click history
    st.session_state.auto_click = False  # Auto-click toggle
    st.session_state.user_name = ""  # Store user's name

# App Title
st.title("🎯 Enhanced Click Counter App")

# User Name Input (Dynamic Update)
user_name = st.text_input("Enter Your Name:", st.session_state.user_name)

if user_name:  
    st.session_state.user_name = user_name  # Save in session state
    st.subheader(f"Welcome, {st.session_state.user_name}! 🚀")
else:
    st.stop()  # Stop execution until name is entered

# Display Counter
st.header(f"Clicks: {st.session_state.counter}")

# Layout: Two Columns (Buttons & Chart)
col1, col2 = st.columns([1, 1])

# Custom Increment Value
with col1:
    increment_value = st.number_input("Set Increment Value:", min_value=1, max_value=10, value=1)

# Auto-Click Mode Toggle
with col2:
    auto_click = st.toggle("🤖 Enable Auto-Click Mode")

# Click Sound Effect
click_sound = """
<audio autoplay>
  <source src="https://www.fesliyanstudios.com/play-mp3/4385" type="audio/mpeg">
</audio>
"""

# Increment Function
def increment():
    st.session_state.counter += increment_value
    st.session_state.click_history.append(datetime.datetime.now().strftime("%H:%M:%S"))
    st.markdown(click_sound, unsafe_allow_html=True)  # Play sound on click
    if st.session_state.counter in [10, 50, 100]:  
        st.balloons()

# Reset Function
def reset():
    st.session_state.counter = 0
    st.session_state.click_history = []

# Buttons
col1, col2, col3 = st.columns(3)
col1.button("🎯 Click Me", on_click=increment)
col2.button("🔄 Reset", on_click=reset)
col3.button("❌ Exit", on_click=st.stop)

# Auto-Click Logic
if auto_click:
    for _ in range(5):  # Simulate 5 auto-clicks
        increment()
        time.sleep(1)

# Click History Table
if st.session_state.click_history:
    st.write("📜 Click History:")
    df = pd.DataFrame(st.session_state.click_history, columns=["Timestamp"])
    st.dataframe(df)

# Live Click Chart
if st.session_state.click_history:
    timestamps = list(range(len(st.session_state.click_history)))
    clicks = np.arange(1, len(st.session_state.click_history) + 1)
    chart_data = pd.DataFrame({"Time": timestamps, "Clicks": clicks})
    st.line_chart(chart_data)
