import streamlit as st
import pandas as pd
import os

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Load or initialize expenses
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        return pd.read_csv(EXPENSE_FILE)
    return pd.DataFrame(columns=["Category", "Amount", "Description"])

# Save expenses
def save_expenses(df):
    df.to_csv(EXPENSE_FILE, index=False)

# Load existing data
expenses = load_expenses()

# Streamlit UI
st.title("💰 Expense Tracker")
st.sidebar.header("Add New Expense")

# Input fields
category = st.sidebar.selectbox("Category", ["Food", "Transport", "Rent", "Utilities", "Other"])
amount = st.sidebar.number_input("Amount ($)", min_value=0.01, format="%.2f")
description = st.sidebar.text_input("Description")

if st.sidebar.button("Add Expense"):
    if description:
        new_expense = pd.DataFrame([[category, amount, description]], columns=["Category", "Amount", "Description"])
        expenses = pd.concat([expenses, new_expense], ignore_index=True)
        save_expenses(expenses)
        st.sidebar.success("Expense added!")
    else:
        st.sidebar.error("Please enter a description.")

# Display Expenses
st.subheader("📋 Expense History")
st.dataframe(expenses)

# Expense Summary
st.subheader("📊 Expense Summary")

total_expense = expenses["Amount"].sum()
st.metric(label="Total Expenses", value=f"${total_expense:.2f}")

# Category-wise Expense Breakdown
if not expenses.empty:
    st.bar_chart(expenses.groupby("Category")["Amount"].sum())

# Delete Expense
if st.button("Clear All Expenses"):
    expenses = pd.DataFrame(columns=["Category", "Amount", "Description"])
    save_expenses(expenses)
    st.success("All expenses cleared!")
    st.rerun()

st.sidebar.write("📌 Developed with Streamlit")
