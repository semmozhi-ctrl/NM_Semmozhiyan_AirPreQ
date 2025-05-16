import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

def correlation_heatmap(df):
    corr = df.corr()
    fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r')
    return fig

def aqi_trend(df):
    if 'Date' in df.columns:
        df_sorted = df.sort_values('Date')
        fig = px.line(df_sorted, x='Date', y='AQI', title='AQI Trend Over Time')
        return fig
    else:
        return None

def feature_importance(rf_model, df):
    features = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']
    importances = rf_model.feature_importances_
    fig = px.bar(x=features, y=importances, title='Feature Importance (Random Forest)')
    return fig
