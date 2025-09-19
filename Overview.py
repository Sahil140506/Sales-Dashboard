import streamlit as st
import pandas as pd

st.title("📌 Overview")

df = pd.read_csv("data/Online_Sales_Data.csv")

# KPIs
total_revenue = df["Total Revenue"].sum()
total_units = df["Units Sold"].sum()
total_transactions = df["Transaction ID"].nunique()

st.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
st.metric("📦 Total Units Sold", total_units)
st.metric("🧾 Total Transactions", total_transactions)
