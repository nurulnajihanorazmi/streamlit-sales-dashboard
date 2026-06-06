
import streamlit as st
import pandas as pd

st.title("Sales Dashboard")

df = pd.read_csv("data/sales.csv")

region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["region"].unique().tolist())
)

if region != "All":
    df = df[df["region"] == region]

product = st.sidebar.selectbox(
    "Select Product",
    ["All"] + sorted(df["product"].unique().tolist())
)

if product != "All":
    df = df[df["product"] == product]

st.metric(
    "Total Units Sold",
    int(df["units_sold"].sum())
)

st.metric(
    "Total Revenue",
    f"${df['revenue'].sum():,.2f}"
)

st.line_chart(df.groupby("date")["revenue"].sum())

st.dataframe(df)
