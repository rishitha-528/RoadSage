import streamlit as st
import pandas as pd


st.set_page_config(page_title="RoadSage", page_icon="🚦", layout="wide")


df = pd.read_csv("data/traffic_data.csv")
df.columns = df.columns.str.lower()


st.title("🚦 RoadSage – Smart Traffic Prediction System")


st.subheader("Enter Traffic Conditions")

col1, col2, col3 = st.columns(3)

with col1:
    vehicle_count = st.slider("Vehicle Count", 0, 300, 100)

with col2:
    weather = st.selectbox("Weather Condition", ["Clear", "Rain", "Fog"])

with col3:
    road_type = st.selectbox("Road Type", ["Highway", "City Road", "Residential"])


vehicle_score = vehicle_count / 200

weather_weight = {
    "Clear": 0.1,
    "Rain": 0.4,
    "Fog": 0.6
}

road_weight = {
    "Highway": 0.5,
    "City Road": 0.3,
    "Residential": 0.2
}

traffic_score = (
    vehicle_score +
    weather_weight[weather] +
    road_weight[road_type]
)


if traffic_score < 0.5:
    result = "Low Traffic 🟢"
elif traffic_score < 0.9:
    result = "Medium Traffic 🟡"
else:
    result = "High Traffic 🔴"


st.subheader(" Prediction Result")
st.success(f"Predicted Traffic Level: **{result}**")


st.markdown("""
###How Prediction Works
- Vehicle count represents traffic volume  
- Weather affects speed and congestion  
- Road type impacts flow capacity  

All factors are combined using weighted scoring.
""")


st.markdown("---")
st.caption("RoadSage | Intelligent Traffic Prediction System")
