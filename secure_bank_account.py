import streamlit as st
import random

# Initialize session state for accounts if not already set
if "accounts" not in st.session_state:
    st.session_state.accounts = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_account" not in st.session_state:
    st.session_state.current_account = None

# Function to Create a Bank Account
def create_account():
    st.subheader("🆕 Create a New Account")
    
    name = st.text_input("Enter your name")
    pin = st.text_input("Set a 4-digit PIN", type="password")

    if st.button("Create Account"):
        if name and pin and len(pin) == 4 and pin.isdigit():
            account_number = str(random.randint(100000, 999999))  # Generate a random 6-digit account number
            st.session_state.accounts[account_number] = {"name": name, "pin": pin, "balance": 0}
            
            st.success(f"🎉 Account Created Successfully!\n\nYour Account Number: `{account_number}`")
            st.session_state.current_account = account_number  # Store the generated account number
            st.session_state.logged_in = True  # Auto login after account creation

        else:
            st.error("❌ Invalid Input. Please enter a valid name and a 4-digit PIN.")

# Function to Access an Existing Account
def access_account():
    st.subheader("🔑 Access Your Account")
    
    account_number = st.text_input("Enter your Account Number")
    pin = st.text_input("Enter your PIN", type="password")

    if st.button("Login"):
        if account_number in st.session_state.accounts:
            account = st.session_state.accounts[account_number]
            if account["pin"] == pin:
                st.session_state.logged_in = True
                st.session_state.current_account = account_number
                st.success("✅ Login Successful!")
            else:
                st.error("❌ Invalid PIN. Please try again.")
        else:
            st.error("❌ Invalid Account Number. Please check and try again.")

# Account Dashboard After Login
def account_dashboard():
    account_number = st.session_state.current_account
    account = st.session_state.accounts[account_number]

    st.subheader(f"Welcome, {account['name']}! 👋")
    st.write(f"**Your Account Number:** `{account_number}`")
    st.write(f"💰 **Current Balance:** ${account['balance']}")

    action = st.radio("Select an action:", ["Deposit", "Withdraw", "Logout"])

    if action == "Deposit":
        deposit_amount = st.number_input("Enter deposit amount:", min_value=1)
        if st.button("Deposit Money"):
            account["balance"] += deposit_amount
            st.success(f"✅ Successfully deposited ${deposit_amount}")

    elif action == "Withdraw":
        withdraw_amount = st.number_input("Enter withdrawal amount:", min_value=1)
        if st.button("Withdraw Money"):
            if withdraw_amount <= account["balance"]:
                account["balance"] -= withdraw_amount
                st.success(f"✅ Successfully withdrew ${withdraw_amount}")
            else:
                st.error("❌ Insufficient Balance!")

    elif action == "Logout":
        st.session_state.logged_in = False
        st.session_state.current_account = None
        st.success("🚪 Logged out successfully!")

# Main App Logic
def main():
    st.title("🏦 Secure Bank Account System")

    if st.session_state.logged_in and st.session_state.current_account:
        account_dashboard()
    else:
        menu = ["Create Account", "Access Account"]
        choice = st.sidebar.selectbox("Select an Option", menu)

        if choice == "Create Account":
            create_account()
        elif choice == "Access Account":
            access_account()

# Run the App
if __name__ == "__main__":
    main()
