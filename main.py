import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- CONFIG ----------
st.set_page_config(page_title="AirPreQ", layout="wide")

# ---------- STYLING ----------
st.markdown("""
    <style>
    .hero {
        background: linear-gradient(to right, rgba(0,0,0,0.7), rgba(0,0,0,0.4)), 
        url("https://images.unsplash.com/photo-1535920527007-57f6ef7c9c9e") no-repeat center center;
        background-size: cover;
        color: white;
        text-align: center;
        padding: 120px 20px;
        border-radius: 8px;
    }
    .hero h1 {
        font-size: 48px;
    }
    .hero p {
        font-size: 18px;
        font-weight: bold;
        color: #f94144;
    }
    .hero .btn {
        margin-top: 20px;
        padding: 12px 25px;
        background-color: #e63946;
        color: white;
        border: none;
        border-radius: 5px;
        font-weight: bold;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- PAGE SELECTION ----------
page = st.selectbox("Choose Page", ["Home", "Dashboard", "About Us", "Services", "Contact Us"])

# ---------- HOME PAGE ----------
if page == "Home":
    st.markdown("""
        <div class="hero">
            <p>// AIR MONITORING //</p>
            <h1>Advanced Air Quality Monitoring System</h1>
            <button class="btn">Learn More</button>
        </div>
    """, unsafe_allow_html=True)

# ---------- DASHBOARD ----------
elif page == "Dashboard":
    st.header("🌍 Air Quality Dashboard")

    @st.cache_data
    def load_data(file):
        try:
            df = pd.read_csv(file)
            df.columns = df.columns.str.strip()  # Strip spaces
            st.write("Available Columns:", df.columns.tolist())  # Debug
            df['Date'] = pd.to_datetime(df['Date'])
            return df
        except Exception as e:
            st.error(f"Error loading file: {e}")
            return pd.DataFrame()

    df = load_data("dataset.csv")

    if df.empty:
        st.warning("Dataset not available or incorrect format.")
    elif 'City' not in df.columns:
        st.error("❌ 'City' column not found in dataset.")
    else:
        unique_cities = sorted(df['City'].unique())
        selected_city = st.selectbox("Select a city", unique_cities)
        city_data = df[df['City'] == selected_city]

        def classify_aqi(aqi):
            if aqi <= 50: return 'Good'
            elif aqi <= 100: return 'Moderate'
            elif aqi <= 200: return 'Unhealthy for Sensitive'
            elif aqi <= 300: return 'Unhealthy'
            elif aqi <= 400: return 'Very Unhealthy'
            else: return 'Hazardous'

        city_data['AQI_Level'] = city_data['AQI'].apply(classify_aqi)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Average AQI", f"{city_data['AQI'].mean():.2f}")
        with col2:
            st.metric("Max AQI", f"{city_data['AQI'].max()}")

        st.subheader("📈 AQI Trend Over Time")
        fig1, ax1 = plt.subplots(figsize=(10, 4))
        ax1.plot(city_data['Date'], city_data['AQI'], color='blue')
        ax1.set_title("AQI Over Time")
        ax1.set_xlabel("Date")
        ax1.set_ylabel("AQI")
        ax1.grid(True)
        st.pyplot(fig1)

        st.subheader("📊 AQI Category Distribution")
        level_counts = city_data['AQI_Level'].value_counts()
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        sns.barplot(x=level_counts.index, y=level_counts.values, palette="coolwarm", ax=ax2)
        ax2.set_ylabel("Days")
        ax2.set_xlabel("AQI Category")
        st.pyplot(fig2)

# ---------- ABOUT US ----------
elif page == "About Us":
    st.header("About AirPreQ")
    st.write("AirPreQ is a next-gen air quality monitoring solution combining real-time AQI analysis with beautiful UI.")

# ---------- SERVICES ----------
elif page == "Services":
    st.header("Our Services")
    st.write("- Real-time AQI Monitoring\n- Data Visualization\n- City-wide Reports\n- Health Advisory")

# ---------- CONTACT ----------
elif page == "Contact Us":
    st.header("Contact Us")
    st.write("📧 support@airpreq.com\n📞 +1 234 567 890")

# ---------- FOOTER ----------
st.markdown("""
<hr>
<p style='text-align:center'>© 2025 Team AirPreQ. All rights reserved.</p>
""", unsafe_allow_html=True)
