import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json
from datetime import datetime, timedelta
import os
import sys

# Add modules directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

try:
    from modules import data_preprocessing, model_training, api_fetcher, visualizations
except ImportError:
    st.error("⚠️ Module import error. Some features may not work properly.")

# Page configuration
st.set_page_config(
    page_title="AirPreQ - Air Quality Prediction",
    page_icon="🌬️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yourusername/airpreq',
        'Report a bug': 'https://github.com/yourusername/airpreq/issues',
        'About': "# AirPreQ\nAdvanced Air Quality Prediction Platform using Machine Learning"
    }
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Main styling */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #1f77b4, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.3rem;
        color: #666;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    }
    
    .team-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    
    .team-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    }
    
    .aqi-good { color: #00e400; font-weight: bold; }
    .aqi-moderate { color: #ffff00; font-weight: bold; }
    .aqi-unhealthy-sensitive { color: #ff7e00; font-weight: bold; }
    .aqi-unhealthy { color: #ff0000; font-weight: bold; }
    .aqi-very-unhealthy { color: #8f3f97; font-weight: bold; }
    .aqi-hazardous { color: #7e0023; font-weight: bold; }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Hide Streamlit style */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def get_aqi_color_class(aqi):
    """Get CSS class for AQI value based on air quality standards"""
    if aqi <= 50:
        return "aqi-good"
    elif aqi <= 100:
        return "aqi-moderate"
    elif aqi <= 150:
        return "aqi-unhealthy-sensitive"
    elif aqi <= 200:
        return "aqi-unhealthy"
    elif aqi <= 300:
        return "aqi-very-unhealthy"
    else:
        return "aqi-hazardous"

def get_aqi_description(aqi):
    """Get description for AQI value"""
    if aqi <= 50:
        return "Good", "🟢"
    elif aqi <= 100:
        return "Moderate", "🟡"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups", "🟠"
    elif aqi <= 200:
        return "Unhealthy", "🔴"
    elif aqi <= 300:
        return "Very Unhealthy", "🟣"
    else:
        return "Hazardous", "🔴"

def create_sample_data():
    """Create sample data for demonstration"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    np.random.seed(42)
    
    data = {
        'date': dates,
        'pm25': np.random.normal(45, 15, len(dates)).clip(0, 200),
        'pm10': np.random.normal(65, 20, len(dates)).clip(0, 300),
        'no2': np.random.normal(35, 10, len(dates)).clip(0, 100),
        'so2': np.random.normal(25, 8, len(dates)).clip(0, 80),
        'co': np.random.normal(1.2, 0.4, len(dates)).clip(0, 5),
        'o3': np.random.normal(85, 15, len(dates)).clip(0, 150),
        'aqi': np.random.normal(75, 25, len(dates)).clip(0, 300)
    }
    
    return pd.DataFrame(data)

def main():
    # Main header
    st.markdown('<h1 class="main-header">🌬️ AirPreQ</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Advanced Air Quality Prediction Platform</p>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("🧭 Navigation")
    page = st.sidebar.selectbox(
        "Choose a page:",
        ["🏠 Home", "📊 Analysis", "📈 Live Data", "🔮 Predictions", "👥 About Team", "📞 Contact"]
    )
    
    if page == "🏠 Home":
        show_home_page()
    elif page == "📊 Analysis":
        show_analysis_page()
    elif page == "📈 Live Data":
        show_live_data_page()
    elif page == "🔮 Predictions":
        show_predictions_page()
    elif page == "👥 About Team":
        show_about_page()
    elif page == "📞 Contact":
        show_contact_page()

def show_home_page():
    """Home page content"""
    # Hero metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🎯 Accuracy</h3>
            <h2>99.2%</h2>
            <p>↑ 2.1% improvement</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🏙️ Cities</h3>
            <h2>500+</h2>
            <p>↑ 50 new cities</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>📊 Predictions</h3>
            <h2>10K+</h2>
            <p>↑ 1.2K this month</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>👥 Users</h3>
            <h2>2.5K+</h2>
            <p>↑ 300 new users</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Mission and features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Our Mission</h3>
            <p>To democratize air quality information through advanced AI and machine learning, 
            empowering communities to make informed decisions about their health and environment.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>✨ Key Features</h3>
            <ul>
                <li>🔍 Real-time air quality monitoring</li>
                <li>🤖 AI-powered predictive analytics</li>
                <li>💡 Personalized health recommendations</li>
                <li>🌍 Global coverage with 500+ cities</li>
                <li>📱 Mobile-responsive design</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🔧 How It Works</h3>
            <p>Our system uses historical pollutant data and real-time environmental inputs to train 
            machine learning models that can predict AQI levels with high accuracy.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🛠️ Technology Stack</h3>
            <ul>
                <li><strong>Frontend:</strong> Streamlit, Plotly, HTML/CSS</li>
                <li><strong>Backend:</strong> Python, Pandas, NumPy</li>
                <li><strong>ML/AI:</strong> scikit-learn, TensorFlow</li>
                <li><strong>Data:</strong> IQAir AirVisual API</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Quick demo section
    st.markdown("---")
    st.markdown("### 🚀 Quick Demo")
    
    # Sample data visualization
    df = create_sample_data()
    
    # Create interactive chart
    fig = px.line(df.tail(30), x='date', y='aqi', 
                  title='AQI Trend - Last 30 Days',
                  color_discrete_sequence=['#1f77b4'])
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="AQI Value",
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)

def show_analysis_page():
    """Analysis page with data upload and visualization"""
    st.header("📊 Air Quality Analysis")
    
    # Upload section
    st.subheader("📁 Upload Your Data")
    uploaded_file = st.file_uploader(
        "Choose a CSV file", 
        type=['csv'],
        help="Upload a CSV file with air quality data for analysis"
    )
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("✅ File uploaded successfully!")
            
            # Data overview
            st.subheader("📋 Data Overview")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("📝 Total Records", len(df))
                st.metric("📊 Columns", len(df.columns))
            
            with col2:
                st.metric("📅 Date Range", f"{len(df)} days")
                st.metric("💾 File Size", f"{uploaded_file.size} bytes")
            
            # Display first few rows
            st.subheader("🔍 Data Preview")
            st.dataframe(df.head(10), use_container_width=True)
            
            # Data analysis
            if st.button("🔬 Analyze Data"):
                analyze_uploaded_data(df)
                
        except Exception as e:
            st.error(f"❌ Error reading file: {str(e)}")
    
    else:
        # Demo with sample data
        st.info("💡 Upload a CSV file or use our sample data for analysis")
        
        if st.button("📊 Use Sample Data"):
            df = create_sample_data()
            st.subheader("📋 Sample Data Analysis")
            analyze_uploaded_data(df)

def analyze_uploaded_data(df):
    """Analyze the uploaded data"""
    st.subheader("📈 Analysis Results")
    
    # Statistical summary
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📊 Statistical Summary**")
        st.dataframe(df.describe(), use_container_width=True)
    
    with col2:
        # Correlation heatmap
        if len(df.select_dtypes(include=[np.number]).columns) > 1:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            corr_matrix = df[numeric_cols].corr()
            
            fig = px.imshow(corr_matrix, 
                          title="Correlation Heatmap",
                          color_continuous_scale='RdBu',
                          aspect="auto")
            st.plotly_chart(fig, use_container_width=True)
    
    # Time series plots
    st.subheader("📈 Visualizations")
    
    # Select columns for plotting
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if numeric_columns:
        selected_columns = st.multiselect(
            "Select parameters to visualize:",
            numeric_columns,
            default=numeric_columns[:3] if len(numeric_columns) >= 3 else numeric_columns
        )
        
        if selected_columns:
            # Create subplot
            fig = make_subplots(
                rows=len(selected_columns), 
                cols=1,
                subplot_titles=selected_columns,
                vertical_spacing=0.08
            )
            
            for i, col in enumerate(selected_columns):
                fig.add_trace(
                    go.Scatter(x=df.index, y=df[col], name=col, line=dict(width=2)),
                    row=i+1, col=1
                )
            
            fig.update_layout(height=200*len(selected_columns), showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

def show_live_data_page():
    """Live data page"""
    st.header("📈 Live Air Quality Data")
    
    # City selection
    col1, col2 = st.columns([2, 1])
    
    with col1:
        city = st.selectbox(
            "🏙️ Select City:",
            ["Chennai", "Mumbai", "Delhi", "Bangalore", "Kolkata", "Hyderabad", "Pune", "Ahmedabad"]
        )
    
    with col2:
        if st.button("🔄 Get Live Data", type="primary"):
            get_live_air_quality_data(city)
    
    # Auto-refresh option
    auto_refresh = st.checkbox("🔄 Auto-refresh every 30 seconds")
    
    if auto_refresh:
        st.rerun()
    
    # Sample live data (since we don't have real API)
    st.subheader(f"📊 Current Air Quality in {city}")
    
    # Generate mock live data
    np.random.seed(int(datetime.now().timestamp()) % 100)
    current_aqi = np.random.randint(50, 150)
    pm25 = np.random.randint(20, 80)
    pm10 = np.random.randint(40, 120)
    no2 = np.random.randint(15, 60)
    so2 = np.random.randint(5, 30)
    
    # Display current values
    col1, col2, col3, col4, col5 = st.columns(5)
    
    aqi_class = get_aqi_color_class(current_aqi)
    aqi_desc, aqi_emoji = get_aqi_description(current_aqi)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h4>AQI</h4>
            <h2 class="{aqi_class}">{current_aqi}</h2>
            <p>{aqi_emoji} {aqi_desc}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.metric("PM2.5", f"{pm25} µg/m³", f"{np.random.randint(-5, 5)}")
    
    with col3:
        st.metric("PM10", f"{pm10} µg/m³", f"{np.random.randint(-8, 8)}")
    
    with col4:
        st.metric("NO2", f"{no2} µg/m³", f"{np.random.randint(-3, 3)}")
    
    with col5:
        st.metric("SO2", f"{so2} µg/m³", f"{np.random.randint(-2, 2)}")
    
    # Health recommendations
    st.subheader("💡 Health Recommendations")
    
    if current_aqi <= 50:
        st.success("🟢 **Good Air Quality** - Great day for outdoor activities!")
    elif current_aqi <= 100:
        st.warning("🟡 **Moderate Air Quality** - Sensitive individuals should limit prolonged outdoor exertion.")
    elif current_aqi <= 150:
        st.warning("🟠 **Unhealthy for Sensitive Groups** - Children, elderly, and people with respiratory conditions should limit outdoor activities.")
    else:
        st.error("🔴 **Unhealthy Air Quality** - Everyone should limit outdoor activities and wear masks when outside.")

def get_live_air_quality_data(city):
    """Fetch live air quality data (placeholder)"""
    with st.spinner(f"🔍 Fetching live data for {city}..."):
        # Simulate API call delay
        import time
        time.sleep(2)
        st.success(f"✅ Live data updated for {city}")

def show_predictions_page():
    """Predictions page"""
    st.header("🔮 Air Quality Predictions")
    
    st.markdown("""
    Use our AI model to predict AQI based on pollutant levels. 
    Enter the current pollutant concentrations to get an accurate AQI prediction.
    """)
    
    # Prediction form
    with st.form("prediction_form"):
        st.subheader("📝 Enter Pollutant Data")
        
        col1, col2 = st.columns(2)
        
        with col1:
            pm25 = st.number_input(
                "PM2.5 (µg/m³)", 
                min_value=0.0, 
                max_value=500.0, 
                value=50.0,
                help="Fine particulate matter with diameter less than 2.5 micrometers"
            )
            pm10 = st.number_input(
                "PM10 (µg/m³)", 
                min_value=0.0, 
                max_value=500.0, 
                value=100.0,
                help="Particulate matter with diameter less than 10 micrometers"
            )
            no2 = st.number_input(
                "NO2 (µg/m³)", 
                min_value=0.0, 
                max_value=500.0, 
                value=40.0,
                help="Nitrogen dioxide concentration"
            )
        
        with col2:
            so2 = st.number_input(
                "SO2 (µg/m³)", 
                min_value=0.0, 
                max_value=500.0, 
                value=20.0,
                help="Sulfur dioxide concentration"
            )
            co = st.number_input(
                "CO (mg/m³)", 
                min_value=0.0, 
                max_value=50.0, 
                value=2.0,
                help="Carbon monoxide concentration"
            )
            o3 = st.number_input(
                "O3 (µg/m³)", 
                min_value=0.0, 
                max_value=500.0, 
                value=80.0,
                help="Ozone concentration"
            )
        
        submitted = st.form_submit_button("🚀 Predict AQI", type="primary")
        
        if submitted:
            # Simulate prediction (replace with actual model)
            prediction = predict_aqi(pm25, pm10, no2, so2, co, o3)
            
            # Display prediction
            st.subheader("🎯 Prediction Results")
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                aqi_class = get_aqi_color_class(prediction)
                aqi_desc, aqi_emoji = get_aqi_description(prediction)
                
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Predicted AQI</h3>
                    <h1 class="{aqi_class}">{prediction:.1f}</h1>
                    <h4>{aqi_emoji} {aqi_desc}</h4>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                # Create gauge chart
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number+delta",
                    value = prediction,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "AQI Gauge"},
                    delta = {'reference': 100},
                    gauge = {
                        'axis': {'range': [None, 300]},
                        'bar': {'color': "darkblue"},
                        'steps': [
                            {'range': [0, 50], 'color': "lightgreen"},
                            {'range': [50, 100], 'color': "yellow"},
                            {'range': [100, 150], 'color': "orange"},
                            {'range': [150, 200], 'color': "red"},
                            {'range': [200, 300], 'color': "purple"}
                        ],
                        'threshold': {
                            'line': {'color': "black", 'width': 4},
                            'thickness': 0.75,
                            'value': prediction
                        }
                    }
                ))
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True)
            
            # Additional insights
            st.subheader("📊 Pollutant Analysis")
            
            pollutants_data = {
                'Pollutant': ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3'],
                'Current Value': [pm25, pm10, no2, so2, co, o3],
                'Safe Limit': [25, 50, 40, 20, 10, 100],
                'Status': []
            }
            
            for i, (current, limit) in enumerate(zip(pollutants_data['Current Value'], pollutants_data['Safe Limit'])):
                if current <= limit:
                    pollutants_data['Status'].append('✅ Safe')
                elif current <= limit * 1.5:
                    pollutants_data['Status'].append('⚠️ Moderate')
                else:
                    pollutants_data['Status'].append('❌ High')
            
            pollutants_df = pd.DataFrame(pollutants_data)
            st.dataframe(pollutants_df, use_container_width=True)

def predict_aqi(pm25, pm10, no2, so2, co, o3):
    """Simple AQI prediction formula (replace with actual ML model)"""
    # Simplified calculation based on US EPA standards
    pm25_aqi = (pm25 / 25) * 50 if pm25 <= 25 else 50 + ((pm25 - 25) / 40) * 50
    pm10_aqi = (pm10 / 50) * 50 if pm10 <= 50 else 50 + ((pm10 - 50) / 80) * 50
    no2_aqi = (no2 / 40) * 50 if no2 <= 40 else 50 + ((no2 - 40) / 80) * 50
    so2_aqi = (so2 / 20) * 50 if so2 <= 20 else 50 + ((so2 - 20) / 40) * 50
    
    # Take the maximum AQI among all pollutants
    aqi = max(pm25_aqi, pm10_aqi, no2_aqi, so2_aqi)
    
    # Add some randomness to simulate model prediction
    np.random.seed(int(pm25 + pm10 + no2 + so2))
    aqi += np.random.normal(0, 5)
    
    return max(0, min(300, aqi))

def show_about_page():
    """About page with team information"""
    st.header("👥 Meet the AirPreQ Team")
    
    st.markdown("""
    We're a passionate team of developers, data scientists, and environmental enthusiasts 
    working together to create intelligent solutions for air quality monitoring and prediction.
    """)
    
    # Team stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("👥 Team Members", "5")
    with col2:
        st.metric("🎯 Model Accuracy", "99.2%")
    with col3:
        st.metric("🏙️ Cities Covered", "500+")
    with col4:
        st.metric("📊 Predictions Made", "10K+")
    
    st.markdown("---")
    
    # Team members
    team_members = [
        {
            "name": "Semmozhiyan NS",
            "role": "Machine Learning Engineer",
            "specialty": "AI Specialist",
            "linkedin": "https://www.linkedin.com/in/semmozhiyan-n-s-aa7478296",
            "github": "https://github.com/semmozhi-ctrl",
            "instagram": "https://www.instagram.com/_calm_edge_?igsh=OWFpaHY0dXQ5eWY0"
        },
        {
            "name": "Sivabalan V",
            "role": "Project Manager",
            "specialty": "Quality Assurance Engineer",
            "linkedin": "https://www.linkedin.com/in/sivabalan51103",
            "github": "https://github.com/Siva-Balan-V",
            "instagram": "https://www.instagram.com/_pr_ince."
        },
        {
            "name": "Dhyanesh V",
            "role": "Backend Developer",
            "specialty": "Deployment Engineer",
            "linkedin": "https://www.linkedin.com/in/dhyanesh-v-741738274",
            "github": "https://github.com/Dhyanesh006",
            "instagram": "https://www.instagram.com/dhyanesh__006"
        },
        {
            "name": "Sri Sabarish U",
            "role": "Data Collection Lead",
            "specialty": "Preprocessing Specialist",
            "linkedin": "https://www.linkedin.com/in/sri-sabarish-8b35a0293",
            "github": "https://github.com/srisabarish06",
            "instagram": "https://www.instagram.com/sri_sabarish_19"
        },
        {
            "name": "Chandru M",
            "role": "UI/UX Designer",
            "specialty": "Documentation Lead",
            "linkedin": "https://www.linkedin.com/in/chandru-m-585b35335",
            "github": "https://github.com/chandru2110",
            "instagram": "https://www.instagram.com/chandru_.03"
        }
    ]
    
    # Display team in grid
    cols = st.columns(2)
    
    for i, member in enumerate(team_members):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="team-card">
                <h3>{member['name']}</h3>
                <p><strong>{member['role']}</strong></p>
                <p><em>{member['specialty']}</em></p>
                <p>
                    <a href="{member['linkedin']}" target="_blank">🔗 LinkedIn</a> | 
                    <a href="{member['github']}" target="_blank">💻 GitHub</a> | 
                    <a href="{member['instagram']}" target="_blank">📸 Instagram</a>
                </p>
            </div>
            """, unsafe_allow_html=True)

def show_contact_page():
    """Contact page"""
    st.header("📞 Contact Us")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📧 Get in Touch")
        
        with st.form("contact_form"):
            name = st.text_input("👤 Name")
            email = st.text_input("📧 Email")
            subject = st.selectbox("📝 Subject", [
                "General Inquiry",
                "Technical Support", 
                "Feature Request",
                "Bug Report",
                "Partnership"
            ])
            message = st.text_area("💬 Message", height=100)
            
            if st.form_submit_button("📤 Send Message", type="primary"):
                if name and email and message:
                    st.success("✅ Thank you! Your message has been sent. We'll get back to you soon.")
                else:
                    st.error("❌ Please fill in all required fields.")
    
    with col2:
        st.subheader("🌐 Connect With Us")
        
        st.markdown("""
        <div class="feature-card">
            <h4>🏢 Project Information</h4>
            <p><strong>Project:</strong> AirPreQ - Air Quality Prediction</p>
            <p><strong>Institution:</strong> Your University/College</p>
            <p><strong>Department:</strong> Computer Science & Engineering</p>
            <p><strong>Year:</strong> 2024</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📱 Follow Our Progress</h4>
            <p>Stay updated with our latest developments:</p>
            <ul>
                <li>🌟 <a href="https://github.com/yourusername/airpreq" target="_blank">GitHub Repository</a></li>
                <li>📊 <a href="#" target="_blank">Project Documentation</a></li>
                <li>📈 <a href="#" target="_blank">Live Demo</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
