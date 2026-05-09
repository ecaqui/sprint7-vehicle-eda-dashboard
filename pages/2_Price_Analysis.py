import streamlit as st
import plotly.express as px
from src.data_loader import load_data

df = load_data()

st.title("💰 Price Analysis")

# Scatter plot
fig_scatter = px.scatter(
    df,
    x="odometer",
    y="price",
    color="type",
    title="Price vs Mileage"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# Boxplot
fig_box = px.box(
    df,
    x="type",
    y="price",
    title="Price Distribution by Vehicle Type"
)

st.plotly_chart(fig_box, use_container_width=True)

# Year vs Price
fig_year_price = px.scatter(
    df,
    x="model_year",
    y="price",
    color="condition",
    title="Model Year vs Price"
)

st.plotly_chart(fig_year_price, use_container_width=True)

# Heatmap
correlation_df = df[
    ["price", "odometer", "model_year"]
].corr()

fig_heatmap = px.imshow(
    correlation_df,
    text_auto=True,
    title="Correlation Heatmap"
)

st.plotly_chart(fig_heatmap, use_container_width=True)

st.success(
    "Mileage shows a strong negative relationship with vehicle prices."
)
