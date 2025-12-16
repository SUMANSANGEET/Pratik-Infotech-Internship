import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Social Media Engagement Dashboard", layout="wide")

df = pd.read_csv("social_media_data.csv")

st.title("📊 Social Media Engagement Analytics Dashboard")

# Sidebar Filters
platform = st.sidebar.multiselect("Select Platform", df["platform"].unique(), default=df["platform"].unique())
content = st.sidebar.multiselect("Select Content Type", df["post_type"].unique(), default=df["post_type"].unique())

filtered_df = df[(df["platform"].isin(platform)) & (df["post_type"].isin(content))]

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Engagement Rate (%)", round(filtered_df["engagement_rate"].mean(), 2))
col2.metric("Total Reach", int(filtered_df["reach"].sum()))
col3.metric("Total Likes", int(filtered_df["likes"].sum()))
col4.metric("Total Posts", filtered_df.shape[0])

st.divider()

# Charts
st.subheader("Engagement by Platform")
st.bar_chart(filtered_df.groupby("platform")["engagement_rate"].mean())

st.subheader("Engagement by Content Type")
st.bar_chart(filtered_df.groupby("post_type")["engagement_rate"].mean())

st.subheader("Top Performing Posts")
st.dataframe(
    filtered_df.sort_values(by="engagement_rate", ascending=False).head(10)
)
