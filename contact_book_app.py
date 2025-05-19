import streamlit as st

def initialize_session():
    if "contacts" not in st.session_state:
        st.session_state.contacts = {}

def show_menu():
    st.title("📖 Contact Book App")
    st.sidebar.header("Menu")
    menu_choice = st.sidebar.radio("Select an option:", ["View Contacts", "Add Contact", "Search Contact", "Edit Contact", "Delete Contact", "Analytics"])
    return menu_choice

def view_contacts():
    st.subheader("📇 Contact List")
    if not st.session_state.contacts:
        st.info("Your contact book is empty.")
    else:
        for name, details in st.session_state.contacts.items():
            st.write(f"**{name}**")
            st.write(f"📞 {details['phone']}")
            st.write(f"📧 {details['email']}")
            st.write(f"🏷️ Category: {details['category']}")
            st.write("---")

def add_contact():
    st.subheader("➕ Add a New Contact")
    name = st.text_input("Name:")
    phone = st.text_input("Phone Number:")
    email = st.text_input("Email:")
    category = st.selectbox("Category:", ["Family", "Friends", "Work", "Others"])
    
    if st.button("Add Contact"):
        st.session_state.contacts[name] = {"phone": phone, "email": email, "category": category}
        st.success(f"{name} has been added to your contacts.")

def search_contact():
    st.subheader("🔍 Search Contact")
    search_name = st.text_input("Enter name to search:")
    if st.button("Search"):
        if search_name in st.session_state.contacts:
            details = st.session_state.contacts[search_name]
            st.write(f"**{search_name}**")
            st.write(f"📞 {details['phone']}")
            st.write(f"📧 {details['email']}")
            st.write(f"🏷️ Category: {details['category']}")
        else:
            st.warning(f"Contact {search_name} not found.")

def edit_contact():
    st.subheader("✏️ Edit Contact")
    if not st.session_state.contacts:
        st.info("No contacts available to edit.")
        return
    
    name = st.selectbox("Select contact to edit:", list(st.session_state.contacts.keys()))
    phone = st.text_input("New Phone Number:", st.session_state.contacts[name]["phone"])
    email = st.text_input("New Email:", st.session_state.contacts[name]["email"])
    category = st.selectbox("Category:", ["Family", "Friends", "Work", "Others"], index=["Family", "Friends", "Work", "Others"].index(st.session_state.contacts[name]["category"]))
    
    if st.button("Update Contact"):
        st.session_state.contacts[name] = {"phone": phone, "email": email, "category": category}
        st.success(f"{name}'s contact information updated.")

def delete_contact():
    st.subheader("❌ Delete Contact")
    if not st.session_state.contacts:
        st.info("No contacts available to delete.")
        return
    
    name = st.selectbox("Select contact to delete:", list(st.session_state.contacts.keys()))
    if st.button("Delete Contact"):
        del st.session_state.contacts[name]
        st.success(f"{name} has been deleted from your contacts.")

def show_analytics():
    st.subheader("📊 Contacts Analytics")
    if not st.session_state.contacts:
        st.info("No data to analyze.")
        return
    
    category_count = {}
    for contact in st.session_state.contacts.values():
        category_count[contact['category']] = category_count.get(contact['category'], 0) + 1
    
    st.bar_chart(category_count)

def main():
    initialize_session()
    choice = show_menu()
    if choice == "View Contacts":
        view_contacts()
    elif choice == "Add Contact":
        add_contact()
    elif choice == "Search Contact":
        search_contact()
    elif choice == "Edit Contact":
        edit_contact()
    elif choice == "Delete Contact":
        delete_contact()
    elif choice == "Analytics":
        show_analytics()

if __name__ == "__main__":
    main()