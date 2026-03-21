
import streamlit as st
import pandas as pd

st.title("E-Commerce Dashboard")

# load data
df = pd.read_csv("main_data.csv")

# METRICS
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("Avg Recency", round(df['recency'].mean(), 1))
col3.metric("Avg Monetary", round(df['monetary'].mean(), 1))

# SEGMENT CHART
st.subheader("Customer Segment Distribution")
st.bar_chart(df['segment'].value_counts())

# FILTER
st.subheader("Filter by Segment")

segment_filter = st.selectbox("Select Segment", df['segment'].unique())

filtered_df = df[df['segment'] == segment_filter]

st.dataframe(filtered_df)

# DATASET
st.subheader("Dataset Preview")
st.dataframe(df.head())

# SUMMARY
st.subheader("Statistical Summary")
st.write(df.describe())
