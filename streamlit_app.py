
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

# Interactive dashboard filters
st.sidebar.header("🔎 Dashboard Filters")

hotel_options = sorted(df["hotel"].dropna().unique().tolist())
year_options = sorted(df["arrival_date_year"].dropna().unique().tolist())
segment_options = sorted(df["market_segment"].dropna().unique().tolist())

selected_hotels = st.sidebar.multiselect(
    "Hotel Type",
    hotel_options,
    default=hotel_options
)

selected_years = st.sidebar.multiselect(
    "Arrival Year",
    year_options,
    default=year_options
)

selected_segments = st.sidebar.multiselect(
    "Market Segment",
    segment_options,
    default=segment_options
)

df = df[
    df["hotel"].isin(selected_hotels)
    & df["arrival_date_year"].isin(selected_years)
    & df["market_segment"].isin(selected_segments)
].copy()

# HotelIQ Executive Overview KPIs
st.header("📊 Executive Overview")

total_bookings = len(df)
total_cancellations = int(df["is_canceled"].sum())

cancellation_rate = (
    total_cancellations / total_bookings * 100
    if total_bookings > 0 else 0
)

estimated_booking_value = df["estimated_booking_value"].sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Bookings", f"{total_bookings:,}")

with col2:
    st.metric("Cancellations", f"{total_cancellations:,}")

with col3:
    st.metric("Cancellation Rate", f"{cancellation_rate:.2f}%")

with col4:
    st.metric(
        "Estimated Booking Value",
        f"{estimated_booking_value / 1_000_000:,.2f}M"
    )

st.caption(
    "Estimated booking value is calculated from booking data "
    "and does not represent confirmed collected revenue."
)

st.dataframe(df.head(10), use_container_width=True)

st.subheader("Available Dataset Columns")
st.write(df.columns.tolist())

