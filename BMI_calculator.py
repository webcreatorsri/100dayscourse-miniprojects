import streamlit as st

# App Title
st.title("⚖️ BMI Calculator")

# User Input
weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (m):", min_value=0.5, format="%.2f")

# Calculate BMI Function
def calculate_bmi(weight, height):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    return None

bmi = calculate_bmi(weight, height)

# Determine BMI Category
status = ""
if bmi:
    if bmi < 18.5:
        status = "🔵 Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "🟢 Normal weight"
    elif 25 <= bmi < 29.9:
        status = "🟠 Overweight"
    else:
        status = "🔴 Obesity"

# Display BMI Result
if bmi:
    st.subheader(f"Your BMI: {bmi}")
    st.markdown(f"### {status}")

    # Visualization
    st.progress(min(bmi / 40, 1.0))  # Scale progress bar dynamically

    # Health Advice
    st.write("💡 **Health Recommendations:**")
    if "Underweight" in status:
        st.info("Consider increasing calorie intake and strength training.")
    elif "Normal" in status:
        st.success("Great! Maintain a balanced diet and stay active.")
    elif "Overweight" in status:
        st.warning("Try incorporating more physical activity and mindful eating.")
    elif "Obesity" in status:
        st.error("Consider professional health guidance for a personalized approach.")

# Reset Button
if st.button("Reset"):
    st.experimental_rerun()
