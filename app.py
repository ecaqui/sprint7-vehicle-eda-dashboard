import streamlit as st

st.set_page_config(
    page_title="Vehicle Analytics Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Vehicle Analytics Dashboard")

st.markdown("""
## Professional Automotive Market Intelligence Platform

This dashboard provides advanced analytics for the US used vehicle market.

### Features:
- Market overview
- Price analysis
- Vehicle segmentation
- Market trends
- Interactive filters
- Automatic insights
- Professional visualizations

Use the sidebar to navigate between dashboard pages.
""")

st.image(
    "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7",
    use_container_width=True
)
