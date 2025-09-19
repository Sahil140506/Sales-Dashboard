import streamlit as st
import pandas as pd

st.title("🌍 Regional Analysis")

df = pd.read_csv("data/Online_Sales_Data.csv")

region_sales = df.groupby("Region")["Total Revenue"].sum().reset_index()

st.bar_chart(region_sales.set_index("Region"))
