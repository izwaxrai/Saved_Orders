import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="BurgerThing",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Order Here 👇")

menu = st.sidebar.selectbox("Choose your order", ["Main", "Burgers", "Desserts", "Drinks", "Pizzas", "Sides"])

if "orders" not in st.session_state:
    st.session_state.orders = []

def display_order_form():
    with st.sidebar.form(key="order_form"):
        st.write("Select items to save an order:")
        selected_items = st.multiselect(
            label="Which items would you like to save?",
            options=[
                "Classic Cheeseburger", "Mushroom Swiss Burger", "Chicken Burger",
                "Avocado Grilled Chicken Burger", "Cheesecake", "Ice Cream Sundae",
                "Fruit Tart", "Tiramisu", "Soda", "Orange Juice",
                "Chocolate Latte With Whipped Cream", "Coffee", "Meat Lovers Pizza",
                "Hawaiian Pizza", "Pepperoni Pizza", "Margarita Pizza", "Garlic Bread",
                "French Fries", "Mozzarella Sticks", "Salad"
            ]
        )
        
        submit = st.form_submit_button(label="Save Order")

        if submit and selected_items:
            st.session_state.orders.append(selected_items)
            st.sidebar.success("Order saved successfully!")

st.sidebar.title("Order Management")
display_order_form()

if st.session_state.orders:
    st.sidebar.title("Saved Orders")
    for i, order in enumerate(st.session_state.orders):
        st.sidebar.write(f"Order {i+1}: {', '.join(order)}")

# --- MAIN MENU ---
if menu == "Main":
    st.image("https://images.unsplash.com/photo-1550547660-d9450f859349?w=1200&auto=format&fit=crop&q=60")
    st.title("🍟 Welcome to BurgerThing 🍔")
    st.write("Combo Promotions & Deals")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&auto=format&fit=crop&q=60")
    with col2:
        st.image("https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400&auto=format&fit=crop&q=60")
    with col3:
        st.image("https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=400&auto=format&fit=crop&q=60")
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1551024601-bec78aea704b?w=400&auto=format&fit=crop&q=60")
    with col2:
        st.image("https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=400&auto=format&fit=crop&q=60")
    with col3:
        st.image("https://images.unsplash.com/photo-1576107232684-1279f390859f?w=400&auto=format&fit=crop&q=60")

# --- BURGERS ---
elif menu == "Burgers":
    st.title("Burgers Menu 🍔")
    st.write("Here are our amazing burgers!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500&auto=format&fit=crop&q=60")
        st.write("Classic Cheeseburger - $5.99")
    with col2:
        st.image("https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=500&auto=format&fit=crop&q=60")
        st.write("Mushroom Swiss Burger - $5.99")
        
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1625813506062-0aeb1d7a094b?w=500&auto=format&fit=crop&q=60")
        st.write("Chicken Burger - $5.99")
    with col2:
        st.image("https://images.unsplash.com/photo-1610440042657-612c34d95e9f?w=500&auto=format&fit=crop&q=60")
        st.write("Avocado Grilled Chicken Burger - $6.99")

    with st.expander("Place Order"):
        burger_choice = st.radio("Which order do you want to save?", 
             ['Classic Cheeseburger ($5.99)', 'Mushroom Swiss Burger ($5.99)', 
              'Chicken Burger ($5.99)', 'Avocado Grilled Chicken Burger ($6.99)'], key="burger_radio")
        if st.button("Submit", key="burger_submit"):
            st.success(f"Your order for {burger_choice} has been placed successfully!")

# --- DESSERTS ---
elif menu == "Desserts":
    st.title("Desserts Menu 🍰")
    st.write("Delicious desserts waiting for you!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1524351199679-46cddf530c04?w=500&auto=format&fit=crop&q=60")
        st.write("Cheesecake - $3.50")
    with col2:
        st.image("https://images.unsplash.com/photo-1579954115545-a95591f28bfc?w=500&auto=format&fit=crop&q=60")
        st.write("Ice Cream Sundae - $3.50")
        
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1519869325930-281384150729?w=500&auto=format&fit=crop&q=60")
        st.write("Fruit Tart - $3.50")
    with col2:
        st.image("https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=500&auto=format&fit=crop&q=60")
        st.write("Tiramisu - $4.50")

    with st.expander("Place Order"):
        dessert_choice = st.radio("Which order do you want to save?", 
             ['Cheesecake ($3.50)', 'Ice Cream Sundae ($3.50)', 
              'Fruit Tart ($3.50)', 'Tiramisu ($4.50)'], key="dessert_radio")
        if st.button("Submit", key="dessert_submit"):
            st.success(f"Your order for {dessert_choice} has been placed successfully!")

# --- DRINKS ---
elif menu == "Drinks":
    st.title("Drinks Menu 🥤")
    st.write("Refresh your thirst with our refreshing drinks!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=500&auto=format&fit=crop&q=60")
        st.write("Soda - $2.50")
    with col2:
        st.image("https://images.unsplash.com/photo-1613478223719-2ab802602423?w=500&auto=format&fit=crop&q=60")
        st.write("Orange Juice - $2.99")
        
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=500&auto=format&fit=crop&q=60")
        st.write("Chocolate Latte With Whipped Cream - $3.50")
    with col2:
        st.image("https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=500&auto=format&fit=crop&q=60")
        st.write("Coffee - $2.99")

    with st.expander("Place Order"):
        drink_choice = st.radio("Which order do you want to save?", 
             ['Soda ($2.50)', 'Orange Juice ($2.99)', 
              'Chocolate Latte With Whipped Cream ($3.50)', 'Coffee ($2.99)'], key="drink_radio")
        if st.button("Submit", key="drink_submit"):
            st.success(f"Your order for {drink_choice} has been placed successfully!")

# --- PIZZAS ---
elif menu == "Pizzas":
    st.title("Pizzas Menu 🍕")
    st.write("Indulge in our mouthwatering pizzas!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?w=500&auto=format&fit=crop&q=60")
        st.write("Meat Lover's Pizza - $14.30")
    with col2:
        st.image("https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=500&auto=format&fit=crop&q=60")
        st.write("Hawaiian Pizza - $10.30")
        
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500&auto=format&fit=crop&q=60")
        st.write("Pepperoni Pizza - $7.50")
    with col2:
        st.image("https://images.unsplash.com/photo-1604068549290-dea0e4a305ca?w=500&auto=format&fit=crop&q=60")
        st.write("Margarita Pizza - $13.50")

    with st.expander("Place Order"):
        pizza_choice = st.radio("Which order do you want to save?", 
             ['Meat Lovers Pizza ($14.30)', 'Hawaiian Pizza ($10.30)',
              'Pepperoni Pizza ($7.50)', 'Margarita Pizza ($13.50)'], key="pizza_radio")
        if st.button("Submit", key="pizza_submit"):
            st.success(f"Your order for {pizza_choice} has been placed successfully!")

# --- SIDES ---
elif menu == "Sides":
    st.title("Sides Menu 🍟")
    st.write("Complete your meal with our delicious sides!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1573140247632-f8fd74997d5c?w=500&auto=format&fit=crop&q=60")
        st.write("Garlic Bread - $8.50")
    with col2:
        st.image("https://images.unsplash.com/photo-1576107232684-1279f390859f?w=500&auto=format&fit=crop&q=60")
        st.write("French Fries - $5.30")
        
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1531749668029-2db88e4b76ce?w=500&auto=format&fit=crop&q=60")
        st.write("Mozzarella Sticks - $6.50")
    with col2:
        st.image("https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=500&auto=format&fit=crop&q=60")
        st.write("Salad - $8.00")

    with st.expander("Place Order"):
        side_choice = st.radio("Which order do you want to save?", 
             ['Garlic Bread ($8.50)', 'French Fries ($5.30)', 
              'Mozzarella Sticks ($6.50)', 'Salad ($8.00)'], key="sides_radio")
        if st.button("Submit", key="sides_submit"):
            st.success(f"Your order for {side_choice} has been placed successfully!")
