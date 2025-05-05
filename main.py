import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="AirPreQ – Air Quality Dashboard", layout="wide")

# --- STYLING ---
def set_theme(mode):
    if mode == "Dark":
        st.markdown("""
            <style>
                body { background-color: #1e1e1e; color: white; }
                .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
                    color: #f5f5f5;
                }
                .aqi-box { background: #292929; color: white; }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                .aqi-box {
                    background: linear-gradient(145deg, #e0e5ec, #ffffff);
                    color: black;
                }
            </style>
        """, unsafe_allow_html=True)

# --- AQI CLASSIFICATION ---
def classify_aqi(aqi):
    try:
        aqi = float(aqi)
        if aqi <= 50: return 'Good'
        elif aqi <= 100: return 'Moderate'
        elif aqi <= 200: return 'Unhealthy for Sensitive'
        elif aqi <= 300: return 'Unhealthy'
        elif aqi <= 400: return 'Very Unhealthy'
        else: return 'Hazardous'
    except:
        return 'Unknown'

# --- LOAD DATA ---
def load_data(uploaded_file=None):
    try:
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_csv("dataset.csv")
        required_cols = ['City', 'Date', 'PM2.5', 'PM10', 'NO2', 'SO2', 'O3', 'AQI']
        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df.dropna(subset=['Date', 'City', 'AQI'], inplace=True)
        df['AQI_Level'] = df['AQI'].apply(classify_aqi)
        return df
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")
        return pd.DataFrame()

# --- SIDEBAR ---
st.sidebar.title("⚙ Settings")
theme = st.sidebar.radio("Theme", ["Light", "Dark"])
set_theme(theme)

uploaded_file = st.sidebar.file_uploader("Upload Your Dataset (CSV)", type=["csv"])
df = load_data(uploaded_file)

if df.empty:
    st.warning("No valid data to display. Please upload a proper air quality CSV.")
    st.stop()

# --- UI HEADER ---
st.title("🛰 AirPreQ – Air Quality Monitoring Dashboard")
st.caption("Copyright © 2025 | Team *AirPreQ*")

# --- CITY SELECTION ---
unique_cities = sorted(df['City'].unique())
selected_city = st.selectbox("Select a City", unique_cities)
city_df = df[df['City'] == selected_city].sort_values('Date')

# --- AQI DISPLAY ---
latest_aqi = city_df.iloc[-1]['AQI']
aqi_status = classify_aqi(latest_aqi)
avg_aqi = city_df['AQI'].mean()

aqi_color = {
    'Good': 'green',
    'Moderate': 'yellow',
    'Unhealthy for Sensitive': 'orange',
    'Unhealthy': 'red',
    'Very Unhealthy': 'purple',
    'Hazardous': 'maroon',
    'Unknown': 'gray'
}.get(aqi_status, 'gray')

col1, col2, col3 = st.columns(3)
col1.markdown(f"<div class='aqi-box' style='border-radius:15px; padding:20px; text-align:center; font-weight:bold; color:{aqi_color};'>"
              f"Real-time AQI<br><span style='font-size:24px'>{latest_aqi:.0f}</span><br>{aqi_status}</div>", unsafe_allow_html=True)
col2.markdown(f"<div class='aqi-box' style='border-radius:15px; padding:20px; text-align:center;'>"
              f"Average AQI<br><span style='font-size:24px'>{avg_aqi:.2f}</span></div>", unsafe_allow_html=True)
col3.markdown(f"<div class='aqi-box' style='border-radius:15px; padding:20px; text-align:center;'>"
              f"Data Range<br><span style='font-size:20px'>{city_df['Date'].min().date()} ➜ {city_df['Date'].max().date()}</span></div>", unsafe_allow_html=True)

# --- TREND VISUALS ---
st.subheader("📈 Pollutant Trends")
pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2', 'O3']

for pollutant in pollutants:
    if pollutant in city_df.columns:
        fig, ax = plt.subplots(figsize=(10, 3))
        sns.lineplot(data=city_df, x='Date', y=pollutant, ax=ax, color='deepskyblue')
        ax.set_title(f"{pollutant} Trend in {selected_city}")
        ax.set_ylabel(f"{pollutant} (μg/m³)")
        ax.grid(True)
        st.pyplot(fig)

# --- AQI LEVEL DISTRIBUTION ---
st.subheader("📊 AQI Category Distribution")

aqi_order = ['Good', 'Moderate', 'Unhealthy for Sensitive', 'Unhealthy', 'Very Unhealthy', 'Hazardous']
level_counts = city_df['AQI_Level'].value_counts().reindex(aqi_order, fill_value=0)

fig2, ax2 = plt.subplots()
sns.barplot(x=level_counts.index, y=level_counts.values,
            palette=['green', 'yellow', 'orange', 'red', 'purple', 'maroon'], ax=ax2)
ax2.set_title(f"AQI Levels in {selected_city}")
ax2.set_ylabel("Number of Days")
ax2.set_xlabel("AQI Category")
ax2.tick_params(axis='x', rotation=30)
st.pyplot(fig2)

# --- FOOTER ---
st.markdown("---")
st.markdown("🧠 Built by *Team AirPreQ* | Powered by Streamlit, Pandas, Seaborn")