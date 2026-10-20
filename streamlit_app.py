
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="HotelIQ | Hotel Analytics",
    page_icon="🏨",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/HotelIQ_SQL_Ready.csv")


df = load_data()

# Introduction
st.title("🏨 HotelIQ")
st.subheader("Hotel Revenue, Demand & Cancellation Intelligence")

st.markdown("""
An interactive hotel booking analytics dashboard.

Explore booking trends, cancellation patterns, and
data-driven insights to support hotel management decisions.
""")

# Sidebar filters
st.sidebar.header("🔎 Dashboard Filters")

hotel_options = sorted(df["hotel"].dropna().unique().tolist())
year_options = sorted(df["arrival_date_year"].dropna().unique().tolist())
segment_options = sorted(df["market_segment"].dropna().unique().tolist())

selected_hotels = st.sidebar.multiselect(
    "Hotel Type", hotel_options, default=hotel_options
)

selected_years = st.sidebar.multiselect(
    "Arrival Year", year_options, default=year_options
)

selected_segments = st.sidebar.multiselect(
    "Market Segment", segment_options, default=segment_options
)

df = df[
    df["hotel"].isin(selected_hotels)
    & df["arrival_date_year"].isin(selected_years)
    & df["market_segment"].isin(selected_segments)
].copy()

# Executive Overview
st.header("📊 Executive Overview")

total_bookings = len(df)
total_cancellations = int(df["is_canceled"].sum())
cancellation_rate = (
    total_cancellations / total_bookings * 100
    if total_bookings else 0
)
estimated_booking_value = df["estimated_booking_value"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Bookings", f"{total_bookings:,}")
col2.metric("Cancellations", f"{total_cancellations:,}")
col3.metric("Cancellation Rate", f"{cancellation_rate:.2f}%")
col4.metric(
    "Estimated Booking Value",
    f"{estimated_booking_value / 1_000_000:,.2f}M"
)

st.caption(
    "Estimated booking value is not confirmed collected revenue."
)

# Cancellation by Hotel Type
st.subheader("Cancellation Rate by Hotel Type")

if not df.empty:
    hotel_cancellation = (
        df.groupby("hotel")["is_canceled"]
        .mean()
        .mul(100)
        .reset_index(name="Cancellation Rate (%)")
    )

    st.bar_chart(
        hotel_cancellation,
        x="hotel",
        y="Cancellation Rate (%)"
    )

# Cancellation by Lead Time
st.subheader("Cancellation Rate by Lead Time")

lead_time_order = [
    "0-7 days", "8-30 days", "31-90 days",
    "91-180 days", "181+ days"
]

if not df.empty:
    lead_time_cancellation = (
        df.groupby("lead_time_group")["is_canceled"]
        .mean()
        .mul(100)
        .reindex(lead_time_order)
        .dropna()
        .reset_index(name="Cancellation Rate (%)")
    )

    st.bar_chart(
        lead_time_cancellation,
        x="lead_time_group",
        y="Cancellation Rate (%)"
    )

# Cancellation by Market Segment
st.subheader("Cancellation Rate by Market Segment")

if not df.empty:
    segment_cancellation = (
        df.groupby("market_segment")["is_canceled"]
        .mean()
        .mul(100)
        .reset_index(name="Cancellation Rate (%)")
        .sort_values("Cancellation Rate (%)", ascending=False)
    )

    st.bar_chart(
        segment_cancellation,
        x="market_segment",
        y="Cancellation Rate (%)"
    )

# Monthly Booking Trends
st.subheader("Monthly Booking Trends")

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

if not df.empty:
    monthly_bookings = (
        df.groupby("arrival_date_month")
        .size()
        .reindex(month_order, fill_value=0)
        .reset_index(name="Bookings")
    )

    st.line_chart(
        monthly_bookings,
        x="arrival_date_month",
        y="Bookings"
    )

# Machine Learning Insights
st.header("🤖 Machine Learning Insights")

st.write(
    "Random Forest classification model for identifying "
    "patterns associated with hotel booking cancellations."
)

ml1, ml2, ml3, ml4, ml5 = st.columns(5)

ml1.metric("Accuracy", "74.90%")
ml2.metric("Precision", "65.12%")
ml3.metric("Recall", "73.26%")
ml4.metric("F1 Score", "68.95%")
ml5.metric("ROC-AUC", "0.8321")

st.caption(
    "Historical held-out test results from the original "
    "HotelIQ model. These metrics do not change with filters."
)

# Dataset Preview
with st.expander("📋 Explore the Dataset"):
    st.write(f"Showing 10 of {len(df):,} filtered bookings")
    st.dataframe(df.head(10), use_container_width=True)

if df.empty:
    st.warning("No bookings match the selected filters.")
