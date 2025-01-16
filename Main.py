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


 

if menu == "Main":
    st.image("banner.png")
    st.title("🍟 Welcome to BurgerThing 🍔")
    st.write("Combo Promotions & Deals")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("promo1.png")
    with col2:
        st.image("promo2.png")
    with col3:
        st.image("promo3.png")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("promo4.png")
    with col2:
        st.image("promo5.png")
    with col3:
            st.image("promo6.png")
if menu == "Burgers":
    st.title("Burgers Menu 🍔")
    st.write("Here are our amazing burgers!")
    col1, col2 = st.columns(2)
    with col1:
        st.image("burger1.png")
        st.write("Classic Cheeseburger - $5.99")
    with col2:
        st.image("burger2.png")
        st.write("Mushroom Swiss Burger - $5.99")
    col1, col2 = st.columns(2)
    with col1:
        st.image("burger3.png")
        st.write("Chicken Burger - $5.99")
    with col2:
        st.image("burger4.png")
        st.write("Avocado Grilled Chicken Burger - $6.99")
    def order():
        st.session_state['success'] = True 

    if 'success' not in st.session_state:
        st.session_state['success'] = False

    with st.expander("Place Order"):
        st.radio("Which order do you want to save?", 
             ['Classic Cheeseburger ($5.99)', 'Mushroom Swiss Burger ($5.99)', 
              'Chicken Burger ($5.99)', 'Avocado Grilled Chicken Burger ($6.99)'])
    if st.button("Submit"):
        order()

    if st.session_state['success']:
        st.success("Your order has been placed successfully!")
                
 
   
elif menu == "Desserts":
    st.title("Desserts Menu 🍰")
    st.write("Delicious desserts waiting for you!")
    col1, col2 = st.columns(2)
    with col1:
        st.image("dessert1.png")
        st.write("Cheesecake - $3.50")
    with col2:
        st.image("dessert2.png")
        st.write("Ice Cream Sundae - $3.50")
    col1, col2 = st.columns(2)
    with col1:
        st.image("dessert3.png")
        st.write("Fruit Tart - $3.50")
    with col2:
        st.image("dessert4.png")
        st.write("Tiramisu - $4.50")
    def order():
        st.session_state['success'] = True 

    if 'success' not in st.session_state:
        st.session_state['success'] = False

    with st.expander("Place Order"):
        st.radio("Which order do you want to save?", 
             ['Cheesecake ($3.50)', 'Ice Cream Sundae ($3.50)', 
              'Fruit Tart ($3.50)', 'Tiramisu ($4.50)'])
    if st.button("Submit"):
        order()

    if st.session_state['success']:
        st.success("Your order has been placed successfully!")



elif menu == "Drinks":
    st.title("Drinks Menu 🥤")
    st.write("Refresh your thirst with our refreshing drinks!")
    col1, col2 = st.columns(2)
    with col1:
        st.image("drinks1.png")
        st.write("Soda - $2.50")
    with col2:
        st.image("drinks2.png")
        st.write("Orange Juice - $2.99")
    col1, col2 = st.columns(2)
    with col1:
        st.image("drinks3.png")
        st.write("Chocalate Latte With Whipped Cream - $3.50")
    with col2:
        st.image("drinks4.png")
        st.write("Coffee - $2.99")
    def order():
        st.session_state['success'] = True 

    if 'success' not in st.session_state:
        st.session_state['success'] = False

    with st.expander("Place Order"):
        st.radio("Which order do you want to save?", 
             ['Soda ($2.50)', 'Orange Juice ($2.99)', 
              'Chocalate Latte With Whipped Cream ($3.50)', 'Coffee ($2.99)'])
    if st.button("Submit"):
        order()

    if st.session_state['success']:
        st.success("Your order has been placed successfully!")


elif menu == "Pizzas":
    st.title("Pizzas Menu 🍕")
    st.write("Indulge in our mouthwatering pizzas!")
    col1, col2 = st.columns(2)
    with col1:
        st.image("pizza1.png")
        st.write("Meat Lover's Pizza - $14.30")
    with col2:
        st.image("pizza2.png")
        st.write("Hawaiian Pizza - $10.30")
    col1, col2 = st.columns(2)
    with col1:
        st.image("pizza3.png")
        st.write("Pepperoni Pizza - $7.50")
    with col2:
        st.image("pizza4.png")
        st.write("Margarita Pizza - $13.50")
    def order():
        st.session_state['success'] = True 

    if 'success' not in st.session_state:
        st.session_state['success'] = False

    with st.expander("Place Order"):
        st.radio("Which order do you want to save?", 
             ['Meat Lovers Pizza ($14.30)', 'Hawaiian Pizza ($10.30)',
              'Pepperoni Pizza ($7.50)', 'Margarita Pizza ($13.50)'])
    if st.button("Submit"):
        order()

    if st.session_state['success']:
        st.success("Your order has been placed successfully!")


elif menu == "Sides":
    st.title("Sides Menu 🍟")
    st.write("Complete your meal with our delicious sides!")
    col1, col2 = st.columns(2)
    with col1:
        st.image("sides1.png")
        st.write("Garlic Bread - $8.50")
    with col2:
        st.image("sides2.png")
        st.write("French Fries - $5.30")
    col1, col2 = st.columns(2)
    with col1:
        st.image("sides3.png")
        st.write("Mozarella Sticks - $6.50")
    with col2:
        st.image("sides4.png")
        st.write("Salad - $8.00")
    def order():
        st.session_state['success'] = True 

    if 'success' not in st.session_state:
        st.session_state['success'] = False

    with st.expander("Place Order"):
        st.radio("Which order do you want to save?", 
             ['Garlic Bread ($8.50)', 'French Fries ($5.30)', 
              'Mozarella Sticks ($6.50)', 'Salad ($8.00)'])
    if st.button("Submit"):
        order()

    if st.session_state['success']:
        st.success("Your order has been placed successfully!")