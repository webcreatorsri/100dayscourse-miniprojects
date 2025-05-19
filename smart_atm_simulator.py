import streamlit as st

# Set App Title and Description
st.set_page_config(page_title="💳 Smart ATM Simulator", layout="centered")
st.title("💳 Smart ATM Simulator")
st.write("A secure and easy-to-use ATM system to manage your transactions.")

# Bank Account Class
class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance

    # Validate PIN
    def validate_pin(self, entered_pin):
        return entered_pin == self.__pin

    # Check Balance
    def check_balance(self):
        return self.__balance

    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"✅ Deposited ${amount}. New Balance: ${self.__balance}"
        return "❌ Invalid deposit amount."

    # Withdraw Money
    def withdraw(self, amount):
        if amount > self.__balance:
            return "❌ Insufficient funds."
        elif amount > 0:
            self.__balance -= amount
            return f"✅ Withdrawn ${amount}. New Balance: ${self.__balance}"
        return "❌ Invalid withdrawal amount."

    # Change PIN
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            return "✅ PIN changed successfully."
        return "❌ Failed to change PIN. Ensure the old PIN is correct and the new PIN is 4 digits."

# Initialize Session Storage
if "accounts" not in st.session_state:
    st.session_state.accounts = {}

# Tabs for Different Features
tab1, tab2, tab3 = st.tabs(["➕ Create Account", "🔑 Access Account", "🏦 ATM Services"])

# Create Account
with tab1:
    st.subheader("➕ Create a New Bank Account")
    account_number = st.text_input("Enter Account Number")
    pin = st.text_input("Set a 4-digit PIN", type="password")

    if st.button("Create Account"):
        if account_number and pin and len(pin) == 4 and pin.isdigit():
            st.session_state.accounts[account_number] = BankAccount(account_number, pin)
            st.success("✅ Account created successfully!")
        else:
            st.error("❌ Invalid details! Ensure the PIN is 4 digits.")

# Access Account
with tab2:
    st.subheader("🔑 Access Your Account")
    acc_num = st.text_input("Enter Your Account Number")
    acc_pin = st.text_input("Enter Your PIN", type="password")

    if st.button("Login"):
        account = st.session_state.accounts.get(acc_num)
        if account and account.validate_pin(acc_pin):
            st.session_state["logged_in"] = acc_num
            st.success("✅ Login Successful! Go to '🏦 ATM Services' tab.")
        else:
            st.error("❌ Invalid account number or PIN.")

# ATM Services (Only Visible After Login)
with tab3:
    if "logged_in" in st.session_state:
        acc = st.session_state.accounts[st.session_state["logged_in"]]
        st.subheader("🏦 ATM Services")
        st.write(f"💼 Welcome, Account {st.session_state['logged_in']}")

        action = st.radio("Select Transaction:", ["Check Balance", "Deposit", "Withdraw", "Change PIN"])

        if action == "Check Balance":
            st.info(f"💰 Your Balance: ${acc.check_balance()}")

        elif action == "Deposit":
            amount = st.number_input("Enter Amount to Deposit", min_value=1, step=1)
            if st.button("Deposit"):
                st.success(acc.deposit(amount))

        elif action == "Withdraw":
            amount = st.number_input("Enter Amount to Withdraw", min_value=1, step=1)
            if st.button("Withdraw"):
                st.success(acc.withdraw(amount))

        elif action == "Change PIN":
            old_pin = st.text_input("Enter Old PIN", type="password")
            new_pin = st.text_input("Enter New 4-digit PIN", type="password")
            if st.button("Change PIN"):
                st.success(acc.change_pin(old_pin, new_pin))

        if st.button("Logout"):
            del st.session_state["logged_in"]
            st.warning("You have been logged out.")
    else:
        st.warning("⚠️ Please log in first from '🔑 Access Account' tab.")
