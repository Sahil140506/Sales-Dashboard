import streamlit as st
import pandas as pd

st.title("📦 Product Analysis")

df = pd.read_csv("data/Online_Sales_Data.csv")

# By Product Category
category_sales = df.groupby("Product Category")["Total Revenue"].sum().reset_index()
st.subheader("By Product Category")
st.bar_chart(category_sales.set_index("Product Category"))

# By Product Name
product_sales = df.groupby("Product Name")["Total Revenue"].sum().reset_index()
top_products = product_sales.sort_values(by="Total Revenue", ascending=False).head(10)

st.subheader("Top 10 Products")
st.bar_chart(top_products.set_index("Product Name"))

