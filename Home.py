import streamlit as st

# Title of the app
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.sidebar.title("📊 Navigation")
st.sidebar.markdown("Use the sidebar to navigate between pages.")

st.title("Welcome to the Sales Dashboard! 🚀")
st.markdown("""
This dashboard helps you analyze sales performance:
- 💰 Track total revenue and units sold  
- 📈 Monitor sales trends over time  
- 🌍 Compare performance across regions  
- 📦 Find top-selling products  
- 💳 Analyze payment methods  

👉 Select a page from the sidebar to begin!
""")
