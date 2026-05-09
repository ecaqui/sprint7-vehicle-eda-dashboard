import streamlit as st
import plotly.express as px
from src.data_loader import load_data

df = load_data()

st.title("📈 Market Trends")

# Listings by year
year_counts = (
    df["model_year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

year_counts.columns = ["model_year", "count"]

fig_year = px.line(
    year_counts,
    x="model_year",
    y="count",
    title="Listings by Model Year"
)

st.plotly_chart(fig_year, use_container_width=True)

# Condition vs Model Year
fig_condition_year = px.histogram(
    df,
    x="model_year",
    color="condition",
    title="Condition vs Model Year",
    barmode="group"
)

st.plotly_chart(fig_condition_year, use_container_width=True)

# Price trend
price_trend = (
    df.groupby("model_year")["price"]
    .mean()
    .reset_index()
)

fig_price_trend = px.line(
    price_trend,
    x="model_year",
    y="price",
    title="Average Price by Model Year"
)

st.plotly_chart(fig_price_trend, use_container_width=True)

st.warning(
    "Newer vehicles consistently maintain higher market prices."
)
