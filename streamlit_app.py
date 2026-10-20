
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("data/HotelIQ_SQL_Ready.csv")

st.set_page_config(
    page_title="HotelIQ | Hotel Analytics",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 HotelIQ")
st.subheader("Hotel Revenue, Demand & Cancellation Intelligence")

st.markdown("""
Welcome to **HotelIQ**, an interactive hotel booking analytics dashboard.

Explore booking trends, cancellation patterns, and
data-driven insights to support better hotel management decisions.
""")
df = load_data()

st.success(f"Dataset loaded successfully: {len(df):,} bookings")

st.subheader("Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)
