import streamlit as st
import random

# ---- CONFIGURATION & WINDOW SETTINGS ----
st.set_page_config(
    page_title="BurgerThing - Favorites Kiosk",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- PERSISTENT STATE MANAGEMENT ----
if "saved_orders" not in st.session_state:
    st.session_state.saved_orders = []
if "current_tray" not in st.session_state:
    st.session_state.current_tray = []

# ---- SIDEBAR: ORDER PROFILE & QUICK RECALL ----
st.sidebar.title("👤 Customer Profiles")

# Section 1: Save Current Build
st.sidebar.subheader("💾 Save This Configuration")
with st.sidebar.form(key="save_profile_form"):
    profile_name = st.text_input("Favorite Label (e.g., 'My Usual', 'Dad's Cheat Meal'):", "")
    items_to_bundle = st.multiselect(
        "Select items to bundle into this preset:",
        options=[
            "Classic Cheeseburger", "Bacon Flame BBQ", "Chicken Burger",
            "Avocado Grilled Burger", "Birthday Cake Cupcakes", "Ice Cream Sundae",
            "Fountain Soda", "Fresh Orange Juice", "Pepperoni Pizza", "Garlic Bread Fries"
        ]
    )
    save_submit = st.form_submit_button("Lock Order Preset")
    
    if save_submit:
        if profile_name and items_to_bundle:
            st.session_state.saved_orders.append({"name": profile_name, "items": items_to_bundle})
            st.sidebar.success(f"Preset '{profile_name}' created!")
        else:
            st.sidebar.warning("Please provide a name and select items.")

st.sidebar.write("---")

# Section 2: Display and Recall Saved Combos
st.sidebar.subheader("⭐ Load Quick Combos")
if not st.session_state.saved_orders:
    st.sidebar.info("No saved favorites found yet. Build one above!")
else:
    for idx, preset in enumerate(st.session_state.saved_orders):
        st.sidebar.write(f"🔹 **{preset['name']}**")
        st.sidebar.write(f", ".join(preset["items"]))
        if st.sidebar.button(f"Load Preset #{idx+1}", key=f"load_pre_{idx}"):
            st.session_state.current_tray = list(preset["items"])
            st.sidebar.toast(f"Loaded {preset['name']} to your screen!")
            st.rerun()

# ---- MAIN INTERFACE LAYOUT ----
st.title("🍔 BurgerThing Self-Service E-Kiosk")
st.write("### Browse Categories & Build Your Custom Tray")

# Interactive category selection tabs on main container screen
tab_burgers, tab_desserts, tab_drinks, tab_pizzas = st.tabs(["🔥 Burgers", "🍰 Desserts", "🥤 Drinks", "🍕 Specialty Items"])

# --- BURGERS CATEGORY ---
with tab_burgers:
    st.write("#### Flame Grilled Selections")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500&auto=format&fit=crop&q=60", width=300)
        st.write("**Classic Cheeseburger** — `$5.99`")
        if st.button("Add Classic Cheeseburger", key="add_b1"):
            st.session_state.current_tray.append("Classic Cheeseburger")
            st.rerun()
            
    with col2:
        st.image("https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=500&auto=format&fit=crop&q=60", width=300)
        st.write("**Bacon Flame BBQ** — `$7.29`")
        if st.button("Add Bacon Flame BBQ", key="add_b2"):
            st.session_state.current_tray.append("Bacon Flame BBQ")
            st.rerun()

# --- DESSERTS CATEGORY ---
with tab_desserts:
    st.write("#### Sweet Treats")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1519869325930-281384150729?w=500&auto=format&fit=crop&q=60", width=300)
        st.write("**Birthday Cake Cupcakes** — `$3.99`")
        if st.button("Add Birthday Cake Cupcakes", key="add_e1"):
            st.session_state.current_tray.append("Birthday Cake Cupcakes")
            st.rerun()
            
    with col2:
        st.image("https://images.unsplash.com/photo-1579954115545-a95591f28bfc?w=500&auto=format&fit=crop&q=60", width=300)
        st.write("**Ice Cream Sundae** — `$3.25`")
        if st.button("Add Ice Cream Sundae", key="add_e2"):
            st.session_state.current_tray.append("Ice Cream Sundae")
            st.rerun()

# --- DRINKS CATEGORY ---
with tab_drinks:
    st.write("#### Refreshing Beverages")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=500&auto=format&fit=crop&q=60", width=300)
        st.write("**Fountain Soda** — `$1.99`")
        if st.button("Add Fountain Soda", key="add_d1"):
            st.session_state.current_tray.append("Fountain Soda")
            st.rerun()
            
    with col2:
        st.image("https://images.unsplash.com/photo-1613478223719-2ab802602423?w=500&auto=format&fit=crop&q=60", width=300)
        st.write("**Fresh Orange Juice** — `$2.50`")
        if st.button("Add Fresh Orange Juice", key="add_d2"):
            st.session_state.current_tray.append("Fresh Orange Juice")
            st.rerun()

# --- SPECIALTY ITEMS ---
with tab_pizzas:
    st.write("#### Alternative Mains & Sides")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500&auto=format&fit=crop&q=60", width=300)
        st.write("**Pepperoni Pizza** — `$8.99`")
        if st.button("Add Pepperoni Pizza", key="add_p1"):
            st.session_state.current_tray.append("Pepperoni Pizza")
            st.rerun()
            
    with col2:
        st.image("https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=500&auto=format&fit=crop&q=60", width=300)
        st.write("**Garlic Bread Fries** — `$4.25`")
        if st.button("Add Garlic Bread Fries", key="add_p2"):
            st.session_state.current_tray.append("Garlic Bread Fries")
            st.rerun()

st.write("---")

# ---- ACTIVE MONITOR TRAY ----
st.header("🛒 Active Ordering Tray")

if not st.session_state.current_tray:
    st.info("Your current tray is empty. Tap items above or load a quick preset combo profile from the sidebar panel!")
else:
    st.write("Items currently on your scanner:")
    for item in st.session_state.current_tray:
        st.write(f"- **{item}**")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Clear Active Tray", type="secondary"):
            st.session_state.current_tray = []
            st.rerun()
    with c2:
        if st.button("Confirm & Transmit Order To Kitchen", type="primary"):
            ticket = random.randint(400, 599)
            st.success(f"🎉 Order Transmitted! Ticket Reference Generated: **#{ticket}**")
            st.session_state.current_tray = []
