import streamlit as st
import random
import datetime

# Function to get a greeting based on the time of day
def get_time_based_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# Function to generate an emoji based on the hobby
def get_hobby_emoji(hobby):
    hobby_dict = {
        "reading": "📖",
        "coding": "💻",
        "gaming": "🎮",
        "music": "🎵",
        "traveling": "✈️",
        "sports": "⚽",
        "painting": "🎨",
        "cooking": "🍳"
    }
    return hobby_dict.get(hobby.lower(), "🌟")

# Function to generate a random motivational quote
def get_motivational_quote():
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad. – Cory House",
        "Programming isn’t about what you know; it’s about what you can figure out. – Chris Pine",
        "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. – Martin Fowler",
        "The best way to predict the future is to invent it. – Alan Kay",
        "First, solve the problem. Then, write the code. – John Johnson"
    ]
    return random.choice(quotes)

# Main function
def main():
    st.set_page_config(page_title="Welcome Generator", page_icon="🤖")

    st.title("✨ Welcome Message Generator ✨")

    # User input fields
    name = st.text_input("What's your name?")
    hobby = st.text_input("What's your favorite hobby?")

    # Greeting style selection
    greeting_style = st.selectbox("Choose a greeting style:", ["Casual", "Formal"])

    if st.button("Generate Welcome Message"):
        if name and hobby:
            emoji = get_hobby_emoji(hobby)
            greeting = get_time_based_greeting()
            st.balloons()  # Confetti effect 🎉

            st.subheader("--- Welcome Message ---")
            if greeting_style == "Casual":
                st.write(f"{greeting}, {name}! 👋 {emoji}")
                st.write("Welcome to the world of Python Programming! 🚀")
                st.write(f"Wow! {hobby} sounds amazing. Keep enjoying it! 😃")
            else:
                st.write(f"{greeting}, {name}.")
                st.write("It is a pleasure to welcome you to this Python Programming experience.")
                st.write(f"We are delighted to know that you have an interest in {hobby}.")

            # Display a motivational quote
            st.subheader("💡 Motivational Quote")
            st.write(get_motivational_quote())
        else:
            st.warning("Please enter both your name and hobby!")

if __name__ == "__main__":
    main()
