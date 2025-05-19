import streamlit as st
import bcrypt

# User Profile Class
class UserProfile:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = self.hash_password(password)

    # Password Hashing
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # Verify Password
    def verify_password(self, password):
        return bcrypt.checkpw(password.encode(), self.__password.encode())

    # Update Email
    def update_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self.email = new_email
            return "✅ Email updated successfully!"
        return "❌ Invalid email format!"

    # Update Password
    def update_password(self, old_password, new_password):
        if self.verify_password(old_password):
            if len(new_password) >= 6:
                self.__password = self.hash_password(new_password)
                return "✅ Password updated successfully!"
            return "❌ Password must be at least 6 characters long!"
        return "❌ Incorrect old password!"

    # Get Display Data
    def get_display_info(self):
        return {"Username": self.username, "Email": self.email, "Password": "🔒 Hidden"}

# Streamlit App
st.title("🔐 Secure User Profile App")

# Session Storage for Users
if "users" not in st.session_state:
    st.session_state.users = []

# Tabs for Features
tab1, tab2, tab3, tab4 = st.tabs(["🆕 Create User", "📜 View Profiles", "✏️ Update Email", "🔑 Change Password"])

# Create User
with tab1:
    st.subheader("Create a New User")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Create User"):
        if username and email and password:
            user = UserProfile(username, email, password)
            st.session_state.users.append(user)
            st.success("🎉 User created successfully!")
        else:
            st.error("❌ Please fill in all fields.")

# View Profiles
with tab2:
    st.subheader("User Profiles")
    if not st.session_state.users:
        st.warning("⚠️ No users found.")
    else:
        for user in st.session_state.users:
            user_info = user.get_display_info()
            st.write(user_info)

# Update Email
with tab3:
    st.subheader("Update Email")
    search_user = st.text_input("Enter Username to Update Email")
    new_email = st.text_input("New Email")
    if st.button("Update Email"):
        found = False
        for user in st.session_state.users:
            if user.username == search_user:
                st.success(user.update_email(new_email))
                found = True
                break
        if not found:
            st.error("❌ User not found!")

# Change Password
with tab4:
    st.subheader("Change Password")
    search_user_pw = st.text_input("Enter Username")
    old_password = st.text_input("Old Password", type="password")
    new_password = st.text_input("New Password", type="password")
    if st.button("Change Password"):
        found = False
        for user in st.session_state.users:
            if user.username == search_user_pw:
                st.success(user.update_password(old_password, new_password))
                found = True
                break
        if not found:
            st.error("❌ User not found!")
