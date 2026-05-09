import streamlit as st
import plotly.express as px
from src.data_loader import load_data

df = load_data()

st.title("🚘 Vehicle Segmentation")

# Filters
manufacturer = st.sidebar.multiselect(
    "Manufacturer",
    df["manufacturer"].dropna().unique(),
    default=df["manufacturer"].dropna().unique()
)

filtered_df = df[
    df["manufacturer"].isin(manufacturer)
]

# Vehicle Type by Manufacturer
fig_type_manufacturer = px.histogram(
    filtered_df,
    x="manufacturer",
    color="type",
    title="Vehicle Type by Manufacturer",
    barmode="group"
)

st.plotly_chart(fig_type_manufacturer, use_container_width=True)

# Fuel Type
fig_fuel = px.histogram(
    filtered_df,
    x="fuel",
    color="fuel",
    title="Fuel Type Distribution"
)

st.plotly_chart(fig_fuel, use_container_width=True)

# Transmission
fig_transmission = px.histogram(
    filtered_df,
    x="transmission",
    color="transmission",
    title="Transmission Distribution"
)

st.plotly_chart(fig_transmission, use_container_width=True)

# Condition
fig_condition = px.histogram(
    filtered_df,
    x="condition",
    color="condition",
    title="Vehicle Condition Distribution"
)

st.plotly_chart(fig_condition, use_container_width=True)
