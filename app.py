from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd
from modules import data_preprocessing, model_training, model_evaluation, api_fetcher, visualizations

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Load predefined dataset once
DATA_PATH = os.path.join('data', 'sample_dataset.csv')
df_predefined = data_preprocessing.load_data(DATA_PATH)
df_preprocessed = data_preprocessing.preprocess_data(df_predefined)
lr_model, rf_model, X_test, y_test = model_training.train_models(df_preprocessed)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/analysis/predefined')
def analysis_predefined():
    corr_fig = visualizations.correlation_heatmap(df_preprocessed)
    aq_trend_fig = visualizations.aqi_trend(df_preprocessed)
    feat_imp_fig = visualizations.feature_importance(rf_model, df_preprocessed)

    corr_json = corr_fig.to_json()
    aq_trend_json = aq_trend_fig.to_json()
    feat_imp_json = feat_imp_fig.to_json()

    return render_template('analysis_predefined.html',
                           corr_json=corr_json,
                           aq_trend_json=aq_trend_json,
                           feat_imp_json=feat_imp_json)

@app.route('/analysis/upload', methods=['GET', 'POST'])
def analysis_upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            df = pd.read_csv(file)
            df_proc = data_preprocessing.preprocess_data(df)
            lr, rf, X_test_up, y_test_up = model_training.train_models(df_proc)
            rmse_lr, r2_lr = model_evaluation.evaluate_model(lr, X_test_up, y_test_up)
            rmse_rf, r2_rf = model_evaluation.evaluate_model(rf, X_test_up, y_test_up)

            # Generate plots for uploaded dataset
            corr_fig = visualizations.correlation_heatmap(df_proc)
            aq_trend_fig = visualizations.aqi_trend(df_proc)
            feat_imp_fig = visualizations.feature_importance(rf, df_proc)

            corr_json = corr_fig.to_json()
            aq_trend_json = aq_trend_fig.to_json()
            feat_imp_json = feat_imp_fig.to_json()

            return render_template('analysis_upload.html',
                                   rmse_lr=rmse_lr, r2_lr=r2_lr,
                                   rmse_rf=rmse_rf, r2_rf=r2_rf,
                                   corr_json=corr_json,
                                   aq_trend_json=aq_trend_json,
                                   feat_imp_json=feat_imp_json)
    return render_template('analysis_upload.html')


@app.route('/analysis/live', methods=['GET', 'POST'])
def analysis_live():
    predicted_aqi = None
    city = state = country = None
    corr_json = aq_trend_json = feat_imp_json = None
    if request.method == 'POST':
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        if city and state and country:
            try:
                live_df = api_fetcher.fetch_live_aqi(city, state, country)
                df_proc = data_preprocessing.preprocess_data(live_df)

                # Model prediction
                features = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']
                for col in features:
                    if col not in df_proc.columns:
                        df_proc[col] = 0
                X_live = df_proc[features]
                predicted_aqi = rf_model.predict(X_live)[0]

                # Generate simple visualizations for live data (even if single row)
                corr_fig = visualizations.correlation_heatmap(df_proc)
                aq_trend_fig = visualizations.aqi_trend(df_proc)
                feat_imp_fig = visualizations.feature_importance(rf_model, df_proc)

                corr_json = corr_fig.to_json()
                aq_trend_json = aq_trend_fig.to_json()
                feat_imp_json = feat_imp_fig.to_json()
            except Exception as e:
                flash(f"Error fetching or processing live data: {str(e)}")

    return render_template('analysis_live.html',
                           city=city, predicted_aqi=predicted_aqi,
                           corr_json=corr_json, aq_trend_json=aq_trend_json, feat_imp_json=feat_imp_json)

if __name__ == "__main__":
    app.run(debug=True)
