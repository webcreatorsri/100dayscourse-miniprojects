import streamlit as st
import random

# Function to generate math questions
def generate_question(difficulty):
    if difficulty == "Easy":
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
    elif difficulty == "Medium":
        num1, num2 = random.randint(10, 50), random.randint(10, 50)
    else:  # Hard
        num1, num2 = random.randint(50, 100), random.randint(50, 100)

    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    return f"{num1} {operator} {num2}", answer

# Main Math Quiz Function
def math_quiz():
    st.set_page_config(page_title="Math Quiz Game", page_icon="🧮")

    st.title("🧮 Fun Math Quiz Game!")
    st.write("Test your math skills by solving these random problems.")

    # Select difficulty level
    difficulty = st.selectbox("Select Difficulty Level:", ["Easy", "Medium", "Hard"])

    # Select number of questions
    num_questions = st.slider("Number of Questions:", min_value=3, max_value=10, value=5, step=1)

    if "score" not in st.session_state:
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.question, st.session_state.answer = generate_question(difficulty)

    # Display the current question
    st.subheader(f"Question {st.session_state.current_question + 1}/{num_questions}")
    st.write(f"🔢 Solve: **{st.session_state.question}**")

    # User input for answer
    user_answer = st.text_input("Enter your answer:", key="user_input")

    if st.button("Submit Answer"):
        if user_answer.strip().isdigit():
            user_answer = int(user_answer)

            if user_answer == st.session_state.answer:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! The correct answer is {st.session_state.answer}")

            # Move to next question
            st.session_state.current_question += 1

            if st.session_state.current_question < num_questions:
                st.session_state.question, st.session_state.answer = generate_question(difficulty)
                st.rerun()  # ✅ Updated from st.experimental_rerun()
            else:
                st.subheader("🎉 Quiz Completed!")
                st.write(f"Your Final Score: **{st.session_state.score}/{num_questions}**")
                
                # Score-based feedback
                if st.session_state.score == num_questions:
                    st.success("🏆 Perfect Score! You're a math genius!")
                elif st.session_state.score >= num_questions // 2:
                    st.info("👍 Great job! You did well.")
                else:
                    st.warning("📚 Keep practicing! You’ll get better.")

                # Reset button
                if st.button("Play Again"):
                    st.session_state.score = 0
                    st.session_state.current_question = 0
                    st.session_state.question, st.session_state.answer = generate_question(difficulty)
                    st.rerun()  # ✅ Updated from st.experimental_rerun()
        else:
            st.warning("Please enter a valid numeric answer!")

# Run the app
if __name__ == "__main__":
    math_quiz()
