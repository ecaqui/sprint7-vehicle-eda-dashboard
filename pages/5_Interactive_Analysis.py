import pandas as pd
import plotly.express as px
import streamlit as st
from src.data_loader import load_data

# Configuración de página
st.set_page_config(
    page_title="Interactive Analysis",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.header("Interactive Vehicle Analysis")

# Texto descriptivo
st.write("""
This section provides interactive exploratory data analysis (EDA)
for the vehicle dataset. Use the checkboxes below to visualize
different relationships and distributions in the data.
""")

# Cargar datos
df = load_data()

# Vista previa de datos
st.subheader("Dataset Preview")
st.dataframe(df.dropna().head())

# Información general
st.subheader("Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Vehicles", len(df))

with col2:
    st.metric("Average Price", f"${int(df['price'].mean())}")

with col3:
    st.metric("Average Odometer", f"{int(df['odometer'].mean())} mi")

# Línea divisoria
st.markdown("---")

# Histograma interactivo
hist_checkbox = st.checkbox(
    "Show Histogram of Vehicle Prices"
)

if hist_checkbox:

    st.subheader("Vehicle Price Distribution")

    fig_hist = px.histogram(
        df,
        x="price",
        nbins=50,
        title="Distribution of Vehicle Prices",
    )

    fig_hist.update_layout(
        xaxis_title="Price",
        yaxis_title="Count"
    )

    st.plotly_chart(fig_hist, use_container_width=True)

# Scatter plot interactivo
scatter_checkbox = st.checkbox(
    "Show Scatter Plot: Price vs Odometer"
)

if scatter_checkbox:

    st.subheader("Price vs Odometer")

    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        color="type",
        title="Relationship Between Price and Mileage",
        opacity=0.6
    )

    fig_scatter.update_layout(
        xaxis_title="Odometer",
        yaxis_title="Price"
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

# Botón adicional
if st.button("Show Random Vehicle Sample"):

    st.subheader("Random Vehicle Sample")

    st.dataframe(
        df.dropna().sample(5)
    )