import streamlit as st

def initialize_session():
    if "shopping_list" not in st.session_state:
        st.session_state.shopping_list = []

def show_menu():
    st.title("🛒 Smart Shopping List App")
    st.sidebar.header("Menu")
    menu_choice = st.sidebar.radio("Select an option:", ["View List", "Add Item", "Remove Item", "Clear List", "Analytics"])
    return menu_choice

def view_list():
    st.subheader("📝 Your Shopping List")
    if not st.session_state.shopping_list:
        st.info("Your shopping list is empty.")
    else:
        for index, item in enumerate(st.session_state.shopping_list):
            st.write(f"{index + 1}. {item['name']} ({item['category']} - {item['quantity']})")

def add_item():
    st.subheader("➕ Add an Item")
    item_name = st.text_input("Item Name:")
    category = st.selectbox("Category:", ["Groceries", "Electronics", "Clothing", "Others"])
    quantity = st.number_input("Quantity:", min_value=1, value=1)
    
    if st.button("Add to List"):
        st.session_state.shopping_list.append({"name": item_name, "category": category, "quantity": quantity})
        st.success(f"{item_name} added to shopping list.")

def remove_item():
    st.subheader("❌ Remove an Item")
    if not st.session_state.shopping_list:
        st.info("Your shopping list is empty.")
        return
    
    item_names = [item['name'] for item in st.session_state.shopping_list]
    item_to_remove = st.selectbox("Select an item to remove:", item_names)
    
    if st.button("Remove Item"):
        st.session_state.shopping_list = [item for item in st.session_state.shopping_list if item['name'] != item_to_remove]
        st.success(f"{item_to_remove} removed from the shopping list.")

def clear_list():
    st.subheader("🗑️ Clear Shopping List")
    if st.button("Clear All"):
        st.session_state.shopping_list = []
        st.success("Shopping list has been cleared.")

def show_analytics():
    st.subheader("📊 Shopping List Analytics")
    if not st.session_state.shopping_list:
        st.info("No data to analyze.")
        return
    
    category_count = {}
    total_items = 0
    for item in st.session_state.shopping_list:
        total_items += item['quantity']
        category_count[item['category']] = category_count.get(item['category'], 0) + item['quantity']
    
    st.write(f"Total Items: {total_items}")
    st.bar_chart(category_count)

def main():
    initialize_session()
    choice = show_menu()
    if choice == "View List":
        view_list()
    elif choice == "Add Item":
        add_item()
    elif choice == "Remove Item":
        remove_item()
    elif choice == "Clear List":
        clear_list()
    elif choice == "Analytics":
        show_analytics()

if __name__ == "__main__":
    main()
