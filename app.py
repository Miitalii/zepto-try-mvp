# app.py

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Zepto Try - AI Discovery Engine", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #FFF5F5; }
    .stButton>button { background-color: #FF6B6B; color: white; border-radius: 8px; }
    .trust-badge { background-color: #E8F5E9; color: #2E7D32; padding: 8px; border-radius: 6px; font-size: 12px; }
    .offer-box { background-color: #FFF3E0; padding: 15px; border-radius: 10px; border-left: 4px solid #FF6B6B; }
</style>
""", unsafe_allow_html=True)

# Logo + Header
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image("logo.png", width=80)
with col_title:
    st.title("Zepto Try")
    st.markdown("<p style='color: #888; font-size: 16px;'>AI-Powered Category Discovery Engine</p>", unsafe_allow_html=True)
st.markdown("---")

# Simulated cart
st.header("1. Your Cart")
cart_items = st.multiselect(
    "Select items in your cart:",
    ["Amul Milk 500ml", "Lay's Chips", "Bananas 6pc", "Bread", "Coca-Cola", "Eggs 6pc", "Maggi Noodles", "Onions 1kg"],
    default=["Amul Milk 500ml", "Lay's Chips", "Bananas 6pc"]
)

if cart_items:
    # AI Category Analyzer (simulated with rules)
    category_map = {
        "Amul Milk 500ml": "dairy", "Bread": "dairy", "Eggs 6pc": "dairy",
        "Lay's Chips": "snacks", "Coca-Cola": "snacks", "Maggi Noodles": "snacks",
        "Bananas 6pc": "fresh", "Onions 1kg": "fresh"
    }
    
    categories = [category_map.get(item, "other") for item in cart_items]
    dominant = max(set(categories), key=categories.count)
    
    # Complementary mapping
    complements = {
        "dairy": {"category": "Beauty & Personal Care", "product": "Nivea Soft Cream (50ml)", "price": 49, "original": 89, "badge": "100% Original • 7-Day Return", "reason": "Dairy buyers often need moisturizers for daily care"},
        "snacks": {"category": "Beauty & Personal Care", "product": "Face Cleansing Wipes (10pc)", "price": 39, "original": 75, "badge": "100% Original • 7-Day Return", "reason": "Snack nights = self-care nights. Users who buy chips add wipes 3x more often"},
        "fresh": {"category": "Household", "product": "Godrej Aer Spray", "price": 59, "original": 99, "badge": "100% Original • 7-Day Return", "reason": "Fresh produce shoppers often refresh home fragrance"},
        "other": {"category": "Electronics", "product": "Boat Earphones", "price": 199, "original": 399, "badge": "100% Original • 7-Day Return", "reason": "Popular add-on for your basket"}
    }
    
    suggestion = complements.get(dominant, complements["other"])
    
    st.header("2. 🤖 AI Discovery Recommendation")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/150/FF6B6B/FFFFFF?text=" + suggestion["product"][:3], width=120)
    with col2:
        st.markdown(f"**{suggestion['product']}**")
        st.markdown(f"<span class='trust-badge'>✓ {suggestion['badge']}</span>", unsafe_allow_html=True)
        st.markdown(f"<div class='offer-box'><b>₹{suggestion['price']}</b> <s>₹{suggestion['original']}</s> ({int((1-suggestion['price']/suggestion['original'])*100)}% off)<br><small>{suggestion['reason']}</small></div>", unsafe_allow_html=True)
    
    # Trust Q&A
    st.header("3. 🛡️ Trust Shield")
    user_question = st.text_input("Ask about this product:", placeholder="e.g., Is this original? Can I return it?")
    
    if user_question:
        responses = {
            "original": "✅ Yes! This product is **100% brand original**. We source directly from authorized distributors. Every item has a unique authenticity code you can verify.",
            "return": "✅ **7-day no-questions-asked return**. If you're unsatisfied, tap 'Return' in your order history. Pickup happens within 24 hours and refund is processed instantly to your Zepto Wallet or original payment method.",
            "expire": "✅ All products have **minimum 6 months shelf life**. We never deliver near-expiry items for non-grocery categories.",
            "price": f"✅ This is a **discovery price** for first-time buyers of {suggestion['category']}. Regular price is ₹{suggestion['original']}. Amazon sells this at ₹{suggestion['original']-10} but with 2-day delivery. You get it in 10 minutes!",
            "default": "✅ This product comes with our **Triple Trust Guarantee**: (1) 100% Authentic, (2) 7-Day Easy Return, (3) Instant Refund. Try risk-free!"
        }
        
        query_lower = user_question.lower()
        if any(w in query_lower for w in ["original", "genuine", "fake", "authentic"]):
            response = responses["original"]
        elif any(w in query_lower for w in ["return", "replace", "exchange"]):
            response = responses["return"]
        elif any(w in query_lower for w in ["expire", "date", "old"]):
            response = responses["expire"]
        elif any(w in query_lower for w in ["price", "cost", "expensive", "cheap"]):
            response = responses["price"]
        else:
            response = responses["default"]
        
        st.info(response)
    
    # CTA
    st.header("4. 🎁 Add to Cart")
    c1, c2 = st.columns(2)
    with c1:
        if st.button(f"Add {suggestion['product']} - ₹{suggestion['price']}", type="primary"):
            st.success("Added! Your discovery journey begins 🎉")
            st.balloons()
    with c2:
        if st.button("Show me something else"):
            st.session_state.show_alt = True
    
    # Alternative
    if st.session_state.get("show_alt"):
        alt = {"category": "Electronics", "product": "Portronics Cable (1m)", "price": 29, "original": 79, "badge": "100% Original • 7-Day Return", "reason": "Essential backup cable for your devices"}
        st.markdown(f"**Alternative:** {alt['product']} — **₹{alt['price']}** <s>₹{alt['original']}</s>")

# Footer
st.markdown("---")
st.caption(f"Zepto Try MVP | Built for Growth Milestone | {datetime.now().year}")