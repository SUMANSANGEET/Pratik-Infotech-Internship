import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Social Media Analytics & Prediction", layout="wide")

# Load Data
df = pd.read_csv("social_media_engagement_dataset.csv")

st.title("📊 Social Media Engagement Dashboard + Prediction")

# ======================
# ANALYTICS SECTION
# ======================
st.header("📈 Engagement Analytics")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Engagement Rate (%)", round(df["engagement_rate"].mean(), 2))
col2.metric("Total Reach", int(df["reach"].sum()))
col3.metric("Total Engagement", int(df["total_engagement"].sum()))
col4.metric("Total Posts", df.shape[0])

st.subheader("Engagement by Platform")
st.bar_chart(df.groupby("platform")["engagement_rate"].mean())

st.subheader("Engagement by Content Type")
st.bar_chart(df.groupby("post_type")["engagement_rate"].mean())

# ======================
# ML PREDICTION SECTION
# ======================
st.divider()
st.header("🤖 Engagement Rate Prediction")

# Encoding
le_platform = LabelEncoder()
le_type = LabelEncoder()
le_day = LabelEncoder()

df["platform_enc"] = le_platform.fit_transform(df["platform"])
df["type_enc"] = le_type.fit_transform(df["post_type"])
df["day_enc"] = le_day.fit_transform(df["weekday"])

X = df[["platform_enc", "type_enc", "reach", "caption_length"]]
y = df["engagement_rate"]

# Train Model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# User Input
platform = st.selectbox("Select Platform", le_platform.classes_)
post_type = st.selectbox("Select Content Type", le_type.classes_)
reach = st.number_input("Expected Reach", min_value=500, max_value=50000, step=500)
caption_len = st.slider("Caption Length", 20, 300, 120)

# Prediction
if st.button("Predict Engagement Rate"):
    input_data = [[
        le_platform.transform([platform])[0],
        le_type.transform([post_type])[0],
        reach,
        caption_len
    ]]
    
    prediction = model.predict(input_data)[0]
    
    st.success(f"📌 Predicted Engagement Rate: **{round(prediction, 2)}%**")
