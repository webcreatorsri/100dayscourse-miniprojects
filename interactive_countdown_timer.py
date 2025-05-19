import streamlit as st
import time

# Main function
def main():
    st.set_page_config(page_title="Countdown Timer", page_icon="⏳")

    st.title("⏳ Interactive Countdown Timer")

    # User input for countdown start number
    start = st.number_input("Enter the countdown start number:", min_value=1, value=10, step=1)

    # User input for delay time
    delay = st.slider("Select countdown speed (seconds per step):", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

    # Countdown button
    if st.button("Start Countdown"):
        st.subheader("🚀 Countdown Begins!")
        countdown(start, delay)
        st.balloons()  # 🎉 Celebration effect
        st.success("🎊 Countdown Complete!")

# Function to perform countdown
def countdown(start, delay):
    countdown_placeholder = st.empty()
    for i in range(start, 0, -1):
        countdown_placeholder.subheader(f"⏳ {i}")
        time.sleep(delay)
    countdown_placeholder.subheader("🎉 Time's Up!")

if __name__ == "__main__":
    main()
