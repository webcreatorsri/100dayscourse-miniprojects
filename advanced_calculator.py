import streamlit as st
import math
import numpy as np

# Initialize session state for calculation history
if "history" not in st.session_state:
    st.session_state.history = []

# Function to perform calculations on multiple numbers
def calculate(numbers, operation):
    try:
        if operation == "Addition":
            return sum(numbers)
        elif operation == "Subtraction":
            return numbers[0] - sum(numbers[1:])
        elif operation == "Multiplication":
            return np.prod(numbers)  # Efficient multiplication of multiple numbers
        elif operation == "Division":
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    return "Cannot divide by zero"
                result /= num
            return result
        elif operation == "Exponentiation":
            if len(numbers) != 2:
                return "Exponentiation requires exactly 2 numbers."
            return numbers[0] ** numbers[1]
        elif operation == "Square Root":
            return [math.sqrt(num) if num >= 0 else "Invalid (negative number)" for num in numbers]
    except OverflowError:
        return "Result too large to compute"

# Main function
def main():
    st.set_page_config(page_title="Advanced Calculator", page_icon="🧮")

    st.title("🧮 Multi-Number Advanced Calculator")

    # Get multiple numbers from the user
    numbers_input = st.text_area("Enter numbers separated by commas (e.g., 5, 10, 15):")
    
    # Convert input into a list of numbers
    try:
        numbers = [float(num.strip()) for num in numbers_input.split(",") if num.strip()]
    except ValueError:
        st.error("Invalid input! Please enter numbers only.")
        return

    # Operation selection
    operation = st.selectbox(
        "Choose an operation:",
        ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Square Root"]
    )

    # Perform calculation
    if st.button("Calculate"):
        if numbers:
            result = calculate(numbers, operation)
            st.session_state.history.append(f"{operation}: {result}")

            st.balloons()  # Confetti effect 🎉
            st.subheader("📊 Calculation Result")
            st.write(f"**{operation} Result:** {result}")
        else:
            st.warning("Please enter at least one number!")

    # Show history
    if st.session_state.history:
        st.subheader("📝 Calculation History")
        for calc in st.session_state.history[-5:]:  # Show last 5 calculations
            st.write(calc)

if __name__ == "__main__":
    main()
