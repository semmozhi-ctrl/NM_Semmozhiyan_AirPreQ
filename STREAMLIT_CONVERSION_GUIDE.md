# Convert Flask AirPreQ to Streamlit (100% Free Forever)

## Why Convert to Streamlit?

- ✅ **100% Free Forever** - No credit card, no limits
- ✅ **Perfect for ML Apps** - Built for data science
- ✅ **Easy Deployment** - One-click to Streamlit Cloud
- ✅ **No Server Management** - Fully managed
- ✅ **Great for Demos** - Perfect for showcasing ML projects

## Streamlit vs Flask Comparison

| Feature | Flask | Streamlit |
|---------|-------|-----------|
| Cost | Varies | 100% Free |
| ML Focus | General | ML/Data Science |
| Deployment | Complex | One-click |
| UI Creation | Manual HTML/CSS | Built-in widgets |
| Best For | Web apps | Data apps |

## Conversion Strategy

### Option 1: Full Conversion (Recommended)
Convert entire Flask app to Streamlit with enhanced ML features.

### Option 2: Hybrid Approach
Keep Flask for API, create Streamlit frontend for demos.

### Option 3: Streamlit + Flask API
Use Streamlit for UI, Flask as backend API service.

## File Structure After Conversion

```
airpreq-streamlit/
├── streamlit_app.py        # Main Streamlit app
├── requirements.txt        # Dependencies
├── pages/                  # Multi-page app
│   ├── 01_🏠_Home.py
│   ├── 02_📊_Analysis.py
│   ├── 03_📈_Live_Data.py
│   ├── 04_👥_About.py
│   └── 05_📞_Contact.py
├── modules/                # Your existing modules
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── api_fetcher.py
│   └── visualizations.py
├── data/
│   └── sample_dataset.csv
├── static/
│   └── images/
└── .streamlit/
    └── config.toml
```

## Sample Streamlit App Structure

### Main App (streamlit_app.py)
```python
import streamlit as st
import pandas as pd
import plotly.express as px
from modules import data_preprocessing, model_training, api_fetcher

# Page config
st.set_page_config(
    page_title="AirPreQ - Air Quality Prediction",
    page_icon="🌬️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(45deg, #1f77b4, #ff7f0e);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">🌬️ AirPreQ</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem;">Advanced Air Quality Prediction Platform</p>', unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🎯 Accuracy", "99.2%", "↑ 2.1%")
    
    with col2:
        st.metric("🏙️ Cities", "500+", "↑ 50")
        
    with col3:
        st.metric("📊 Predictions", "10K+", "↑ 1.2K")
        
    with col4:
        st.metric("👥 Users", "2.5K+", "↑ 300")

    # Quick analysis section
    st.markdown("### 🚀 Quick Analysis")
    
    tab1, tab2, tab3 = st.tabs(["📈 Live Data", "📊 Upload Data", "🔮 Predictions"])
    
    with tab1:
        st.markdown("#### Real-time Air Quality Data")
        city = st.selectbox("Select City", ["Chennai", "Mumbai", "Delhi", "Bangalore"])
        if st.button("Get Live Data"):
            # Your existing API fetching logic
            data = api_fetcher.get_live_data(city)
            st.json(data)
    
    with tab2:
        st.markdown("#### Upload Your Data")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head())
            
            if st.button("Analyze Data"):
                # Your existing analysis logic
                results = data_preprocessing.analyze_data(df)
                st.success("Analysis complete!")
                st.plotly_chart(px.line(df, x='date', y='aqi'))
    
    with tab3:
        st.markdown("#### Make Predictions")
        with st.form("prediction_form"):
            col1, col2 = st.columns(2)
            with col1:
                pm25 = st.number_input("PM2.5", min_value=0.0, max_value=500.0, value=50.0)
                pm10 = st.number_input("PM10", min_value=0.0, max_value=500.0, value=100.0)
            with col2:
                no2 = st.number_input("NO2", min_value=0.0, max_value=500.0, value=40.0)
                so2 = st.number_input("SO2", min_value=0.0, max_value=500.0, value=20.0)
            
            submitted = st.form_submit_button("Predict AQI")
            if submitted:
                # Your existing prediction logic
                prediction = model_training.predict_aqi(pm25, pm10, no2, so2)
                st.success(f"Predicted AQI: {prediction}")
                
                # Color coding
                if prediction < 50:
                    st.success("🟢 Good Air Quality")
                elif prediction < 100:
                    st.warning("🟡 Moderate Air Quality")
                else:
                    st.error("🔴 Poor Air Quality")

if __name__ == "__main__":
    main()
```

### Multi-page Structure

#### pages/01_🏠_Home.py
```python
import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("🏠 Welcome to AirPreQ")
st.markdown("""
## About AirPreQ
AirPreQ is an advanced air quality prediction platform that uses machine learning 
to provide accurate forecasts of air pollution levels.

### Key Features
- 🎯 **99.2% Accuracy** - State-of-the-art ML models
- 🌍 **500+ Cities** - Global coverage
- 📱 **Real-time Data** - Live air quality monitoring
- 🔮 **Predictions** - Future air quality forecasts
""")

# Your existing home page content
```

#### pages/02_📊_Analysis.py
```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analysis", page_icon="📊")

st.title("📊 Air Quality Analysis")

# Your existing analysis functionality
uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Data overview
    st.subheader("Data Overview")
    st.dataframe(df.head())
    
    # Visualizations
    st.subheader("Visualizations")
    fig = px.line(df, x='date', y='aqi', title='AQI Trend')
    st.plotly_chart(fig, use_container_width=True)
```

## Deployment to Streamlit Cloud

### 1. Push to GitHub
```bash
cd your-streamlit-app
git init
git add .
git commit -m "Streamlit version of AirPreQ"
git remote add origin https://github.com/yourusername/airpreq-streamlit.git
git push -u origin main
```

### 2. Deploy on Streamlit Cloud
1. Go to: https://share.streamlit.io/
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file: `streamlit_app.py`
6. Click "Deploy"

### 3. Your App is Live! 🎉
URL: `https://yourusername-airpreq-streamlit-main.streamlit.app/`

## Configuration Files

### requirements.txt
```txt
streamlit==1.28.0
pandas==2.0.3
numpy==1.24.3
plotly==5.15.0
scikit-learn==1.3.0
requests==2.31.0
```

### .streamlit/config.toml
```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"

[server]
maxUploadSize = 200
enableCORS = false
```

## Benefits of Streamlit Version

### 1. Enhanced ML Features
- Built-in widgets for data input
- Interactive plots with Plotly
- Easy model deployment
- Real-time updates

### 2. Better User Experience
- Mobile-responsive by default
- Professional UI without CSS coding
- Interactive elements
- Fast loading

### 3. Cost Benefits
- 100% free hosting
- No server maintenance
- Automatic scaling
- Global CDN

## Migration Checklist

- [ ] Convert Flask routes to Streamlit pages
- [ ] Replace HTML templates with Streamlit components
- [ ] Update data handling for Streamlit
- [ ] Test all functionality
- [ ] Deploy to Streamlit Cloud
- [ ] Update documentation

## Sample Conversion

### Flask Code:
```python
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict(data)
    return jsonify({'prediction': prediction})
```

### Streamlit Code:
```python
def predict_page():
    st.title("🔮 Air Quality Prediction")
    
    with st.form("prediction"):
        pm25 = st.number_input("PM2.5")
        pm10 = st.number_input("PM10")
        
        if st.form_submit_button("Predict"):
            prediction = model.predict([pm25, pm10])
            st.success(f"Predicted AQI: {prediction}")
```

Would you like me to help you convert your Flask app to Streamlit for permanent free hosting?
