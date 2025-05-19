import streamlit as st
from datetime import datetime, timedelta
import time

# Streamlit Page Config
st.set_page_config(page_title="⏳ Event Countdown Timer", layout="centered")

st.title("⏳ Event Countdown Timer")

# Get Event Name from User
event_name = st.text_input("Enter Event Name:", "My Special Event")

# Get Event Date & Time with a Wider Year Range (1950 - 2100)
event_date = st.date_input("Select Event Date:", min_value=datetime(1950, 1, 1), max_value=datetime(2100, 12, 31))
event_time = st.time_input("Select Event Time:")

if st.button("Start Countdown 🚀"):
    if event_name and event_date and event_time:
        event_datetime = datetime.combine(event_date, event_time)
        st.session_state["event_datetime"] = event_datetime
        st.session_state["event_name"] = event_name
        st.session_state["countdown_active"] = True
        st.rerun()

# Display Countdown Timer
if "event_datetime" in st.session_state and st.session_state.get("countdown_active"):
    event_datetime = st.session_state["event_datetime"]
    event_name = st.session_state["event_name"]

    while True:
        time_left = event_datetime - datetime.now()
        if time_left.total_seconds() <= 0:
            st.success(f"🎉 {event_name} has started!")
            st.session_state["countdown_active"] = False
            break

        # Format Time Remaining
        days, seconds = divmod(time_left.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        st.metric(label=f"⏳ Time Left for {event_name}:", value=f"{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s")
        time.sleep(1)
        st.rerun()
