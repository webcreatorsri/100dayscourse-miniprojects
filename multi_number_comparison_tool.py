import streamlit as st

# Function to compare multiple numbers
def analyze_numbers(numbers):
    results = []
    
    if not numbers:
        return ["No numbers entered!"]

    # Convert all to float
    numbers = [float(num) for num in numbers]

    # Find min and max
    min_num = min(numbers)
    max_num = max(numbers)
    results.append(f"📉 Smallest Number: {min_num}")
    results.append(f"📈 Largest Number: {max_num}")

    # Absolute difference
    diff = abs(max_num - min_num)
    results.append(f"🔢 Absolute Difference: {diff}")

    # Check zero presence
    zero_status = "Yes, at least one number is zero." if 0 in numbers else "No zeros found."
    results.append(f"🟢 Contains Zero? {zero_status}")

    # Check for negatives
    negative_count = sum(1 for num in numbers if num < 0)
    results.append(f"🔴 Negative Numbers Count: {negative_count}")

    # Check even/odd
    even_odd = {num: "Even" if num % 2 == 0 else "Odd" for num in numbers}
    for num, status in even_odd.items():
        results.append(f"{num} is {status}.")

    return results

# Main function
def main():
    st.set_page_config(page_title="Multi-Number Analysis", page_icon="🔢")

    st.title("🔢 Multi-Number Comparison Tool")

    # Get multiple numbers from the user
    numbers_input = st.text_area("Enter numbers separated by commas (e.g., 5, 10, -3, 8):")
    
    # Convert input into a list of numbers
    try:
        numbers = [num.strip() for num in numbers_input.split(",") if num.strip()]
        numbers = [float(num) for num in numbers]  # Convert to float
    except ValueError:
        st.error("Invalid input! Please enter numbers only.")
        return

    # Perform analysis when button is clicked
    if st.button("Analyze Numbers"):
        if numbers:
            results = analyze_numbers(numbers)
            st.balloons()  # 🎉 Celebration effect
            st.subheader("📊 Analysis Results")
            for res in results:
                st.write(res)
        else:
            st.warning("Please enter at least one number!")

if __name__ == "__main__":
    main()
