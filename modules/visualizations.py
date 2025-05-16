import plotly.express as px
import pandas as pd


def correlation_heatmap(df):
    # Keep only numeric columns and remove constant columns
    numeric_df = df.select_dtypes(include='number')
    numeric_df = numeric_df.loc[:, numeric_df.nunique() > 1]

    # Only select known pollutant features if available
    target_cols = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene','AQI']
    features = [col for col in target_cols if col in numeric_df.columns]

    if len(features) < 2:
        return px.imshow([[0]], labels=dict(x="Not enough data", y="Not enough data"), title="Correlation Heatmap")

    corr = numeric_df[features].corr()

    fig = px.imshow(corr,
                    text_auto=True,
                    color_continuous_scale='RdBu_r',
                    title='Correlation Heatmap',
                    aspect="auto")
    return fig


def aqi_trend(df):
    if df.shape[0] < 2 or 'Date' not in df.columns or 'AQI' not in df.columns:
        return px.line(title="Insufficient data to plot AQI Trend")

    df_sorted = df.sort_values('Date')
    fig = px.line(df_sorted, x='Date', y='AQI', title='AQI Trend Over Time')
    return fig

def feature_importance(rf_model, df):
    features = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']
    features_present = [f for f in features if f in df.columns]
    if not features_present:
        return px.bar(title="No features available for importance")

    importances = rf_model.feature_importances_[:len(features_present)]
    fig = px.bar(x=features_present, y=importances, title='Feature Importance (Random Forest)')
    return fig
