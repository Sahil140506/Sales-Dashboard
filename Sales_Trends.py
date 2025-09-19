import streamlit as st
import pandas as pd

st.title("📈 Sales Trends")

df = pd.read_csv("data/Online_Sales_Data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Group by Date
sales_trends = df.groupby("Date")["Total Revenue"].sum().reset_index()

st.line_chart(sales_trends.set_index("Date"))
