import streamlit as st
import pandas as pd

st.title("Social Media Engagement Dashboard")
df = pd.read_csv("social_media_data.csv")

st.metric("Average Engagement Rate", round(df['engagement_rate'].mean(),2))
st.bar_chart(df.groupby("platform")["engagement_rate"].mean())