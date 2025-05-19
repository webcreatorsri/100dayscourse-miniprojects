import streamlit as st

# Set App Title and Description
st.set_page_config(page_title="📦 Smart Inventory Manager", layout="centered")
st.title("📦 Smart Inventory Manager")
st.write("Manage your inventory efficiently with our smart tracking system.")

# Inventory Management Class
class Inventory:
    total_items = 0

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        Inventory.total_items += quantity

    # Sell Product
    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Inventory.total_items -= amount
            return f"✅ {amount} {self.product_name}(s) sold!"
        return "❌ Insufficient quantity!"

    # Calculate Discount
    @staticmethod
    def calculate_discount(price, discount_percentage):
        return price * (1 - discount_percentage / 100)

    # Show Product Details
    def get_details(self):
        return {"Product": self.product_name, "Price": f"${self.price}", "Quantity": self.quantity}

# Initialize Session Storage
if "products" not in st.session_state:
    st.session_state.products = []

# Tabs for Different Features
tab1, tab2, tab3, tab4, tab5 = st.tabs(["➕ Add Product", "📜 View Inventory", "💰 Sell Product", "🔖 Discount Calculator", "📊 Total Report"])

# Add Product
with tab1:
    st.subheader("➕ Add New Product")
    product_name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0, format="%.2f")
    quantity = st.number_input("Quantity", min_value=1, step=1)

    if st.button("Add Product"):
        if product_name and price > 0 and quantity > 0:
            new_product = Inventory(product_name, price, quantity)
            st.session_state.products.append(new_product)
            st.success(f"✅ {quantity} {product_name}(s) added!")
        else:
            st.error("❌ Please enter valid product details.")

# View Inventory
with tab2:
    st.subheader("📜 Inventory List")
    if not st.session_state.products:
        st.warning("⚠️ No products in inventory.")
    else:
        for product in st.session_state.products:
            st.write(product.get_details())

# Sell Product
with tab3:
    st.subheader("💰 Sell Product")
    product_names = [p.product_name for p in st.session_state.products]
    if product_names:
        selected_product = st.selectbox("Select Product", product_names)
        quantity_to_sell = st.number_input("Quantity to Sell", min_value=1, step=1)

        if st.button("Sell"):
            for product in st.session_state.products:
                if product.product_name == selected_product:
                    st.success(product.sell_product(quantity_to_sell))
                    break
    else:
        st.warning("⚠️ No products available for sale.")

# Discount Calculator
with tab4:
    st.subheader("🔖 Discount Calculator")
    price = st.number_input("Enter Price", min_value=0.0, format="%.2f")
    discount_percentage = st.number_input("Discount Percentage", min_value=0.0, max_value=100.0, format="%.2f")

    if st.button("Calculate Discount"):
        discounted_price = Inventory.calculate_discount(price, discount_percentage)
        st.success(f"💲 Discounted Price: ${discounted_price:.2f}")

# Total Items Report
with tab5:
    st.subheader("📊 Total Inventory Report")
    total_items = sum(p.quantity for p in st.session_state.products)
    st.info(f"🛒 Total Items in Inventory: {total_items}")
