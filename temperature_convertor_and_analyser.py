import streamlit as st
import matplotlib.pyplot as plt

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def get_temperature_advice(temp_c):
    if temp_c < 0:
        return "❄️ Extremely Cold! Wear heavy winter clothing."
    elif temp_c < 10:
        return "🥶 Cold! Wear warm clothing."
    elif temp_c < 20:
        return "🌤️ Cool! A light jacket is enough."
    elif temp_c < 30:
        return "🌞 Warm! T-shirt and shorts weather."
    else:
        return "🔥 Hot! Stay hydrated and wear light clothing."

st.title("🌡️ Temperature Converter & Advisor")

option = st.radio("Select Conversion Type:", [
    "Celsius to Fahrenheit & Kelvin",
    "Fahrenheit to Celsius & Kelvin",
    "Kelvin to Celsius & Fahrenheit"
])

temp_input = st.number_input("Enter Temperature:", step=0.1)

if st.button("Convert & Analyze"):
    if option == "Celsius to Fahrenheit & Kelvin":
        temp_f = celsius_to_fahrenheit(temp_input)
        temp_k = celsius_to_kelvin(temp_input)
        temp_c = temp_input
    elif option == "Fahrenheit to Celsius & Kelvin":
        temp_c = fahrenheit_to_celsius(temp_input)
        temp_k = fahrenheit_to_kelvin(temp_input)
        temp_f = temp_input
    elif option == "Kelvin to Celsius & Fahrenheit":
        temp_c = kelvin_to_celsius(temp_input)
        temp_f = kelvin_to_fahrenheit(temp_input)
        temp_k = temp_input
    
    st.success(f"🌡️ Celsius: {temp_c:.2f} °C")
    st.success(f"🌡️ Fahrenheit: {temp_f:.2f} °F")
    st.success(f"🌡️ Kelvin: {temp_k:.2f} K")
    
    st.subheader("📊 Temperature Comparison Chart")
    temps = [temp_c, temp_f, temp_k]
    labels = ["Celsius", "Fahrenheit", "Kelvin"]
    
    fig, ax = plt.subplots()
    ax.bar(labels, temps, color=['blue', 'red', 'green'])
    ax.set_ylabel("Temperature Value")
    ax.set_title("Temperature Scale Comparison")
    st.pyplot(fig)
    
    st.subheader("🧥 Temperature Advice")
    st.info(get_temperature_advice(temp_c))
