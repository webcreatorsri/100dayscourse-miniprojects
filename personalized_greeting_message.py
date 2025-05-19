import streamlit as st
import datetime
import random

# Function to get a greeting based on the time of day
def get_time_based_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# Function to generate a fun emoji
def get_random_emoji():
    emojis = ["😃", "🚀", "🎉", "🔥", "🌟", "💡", "🎨", "🎵", "⚽", "🍕"]
    return random.choice(emojis)

# Function to generate an age-based message
def get_age_message(age):
    if age < 13:
        return "You're a young explorer! Keep learning and having fun! 🎈"
    elif age < 20:
        return "Teen years are the best! Keep chasing your dreams! ✨"
    elif age < 40:
        return "You’re in your prime! Go conquer the world! 🚀"
    elif age < 60:
        return "Wisdom comes with experience. Keep inspiring! 🌟"
    else:
        return "Age is just a number! Keep shining! 🌼"

# Function to generate a random motivational quote
def get_motivational_quote():
    quotes = [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "Your limitation—it's only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream big and dare to fail. – Norman Vaughan"
    ]
    return random.choice(quotes)

# Main function
def main():
    st.set_page_config(page_title="Personalized Greeting", page_icon="😊")

    st.title("✨ Personalized Greeting Program ✨")

    # User input fields
    name = st.text_input("What is your name?")
    age = st.number_input("How old are you?", min_value=0, step=1)
    color = st.text_input("What is your favorite color?")

    if st.button("Generate Greeting"):
        if name and color:
            greeting = get_time_based_greeting()
            emoji = get_random_emoji()
            age_message = get_age_message(age)

            st.balloons()  # Confetti effect 🎉

            st.subheader("---- Personalized Greeting ----")
            st.markdown(f"<h2 style='color:{color};'>{greeting}, {name}! {emoji}</h2>", unsafe_allow_html=True)
            st.write(f"You are {age} years old, and {color} is a fantastic color! 🎨")
            st.write(age_message)

            # Display a motivational quote
            st.subheader("💡 Motivational Quote")
            st.write(get_motivational_quote())
        else:
            st.warning("Please enter your name and favorite color!")

if __name__ == "__main__":
    main()
