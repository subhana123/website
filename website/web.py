import streamlit as st

# Sample product catalog
products = {
    "Laptop": 800,
    "Smartphone": 500,
    "Headphones": 100,
    "Smartwatch": 150
}

# Initialize session state for cart if not already present
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Title
st.title("🛒 Simple eCommerce Store")

# Display products
st.subheader("Products Available")
for product, price in products.items():
    col1, col2 = st.columns([3, 1])
    col1.write(f"**{product}** - ${price}")
    if col2.button(f"Add {product}"):
        if product in st.session_state.cart:
            st.session_state.cart[product] += 1
        else:
            st.session_state.cart[product] = 1

# Cart section
st.subheader("🛍️ Your Cart")
if st.session_state.cart:
    total_price = 0
    for item, quantity in st.session_state.cart.items():
        st.write(f"{item} x {quantity} - ${products[item] * quantity}")
        total_price += products[item] * quantity
    
    st.write(f"**Total: ${total_price}**")
    if st.button("Checkout"):
        st.success("Thank you for your purchase! 🎉")
        st.session_state.cart = {}
else:
    st.write("Your cart is empty.")
