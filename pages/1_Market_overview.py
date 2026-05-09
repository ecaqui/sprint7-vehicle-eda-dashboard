import streamlit as st
import plotly.express as px
from src.data_loader import load_data

df = load_data()

st.title("📊 Market Overview")

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Listings", len(df))
col2.metric("Average Price", f"${df['price'].mean():,.0f}")
col3.metric("Average Mileage", f"{df['odometer'].mean():,.0f}")
col4.metric("Manufacturers", df['manufacturer'].nunique())

# Price Distribution
fig_price = px.histogram(
    df,
    x="price",
    nbins=50,
    title="Vehicle Price Distribution"
)

st.plotly_chart(fig_price, use_container_width=True)

# Vehicle Types
fig_type = px.histogram(
    df,
    x="type",
    color="type",
    title="Vehicle Type Distribution"
)

st.plotly_chart(fig_type, use_container_width=True)

# Manufacturers
top_manufacturers = (
    df["manufacturer"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_manufacturers.columns = ["manufacturer", "count"]

fig_manufacturer = px.bar(
    top_manufacturers,
    x="manufacturer",
    y="count",
    title="Top Manufacturers"
)

st.plotly_chart(fig_manufacturer, use_container_width=True)

st.info(
    "Pickup trucks and SUVs dominate the used vehicle market."
)
