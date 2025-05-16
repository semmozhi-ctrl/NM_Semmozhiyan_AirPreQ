from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import pandas as pd
from preprocessing import preprocess_data
from eda import generate_visualizations
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data'
app.config['OUTPUT_FOLDER'] = 'static/outputs'
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename.endswith('.csv'):
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(file_path)

            df = pd.read_csv(file_path)
            df_clean = preprocess_data(df)
            plot_path = generate_visualizations(df_clean, filename)

            return render_template('upload.html', plot_path=plot_path)
    return render_template('upload.html')

@app.route('/predefined')
def predefined():
    df = pd.read_csv('data/dataset.csv')
    df_clean = preprocess_data(df)
    plot_path = generate_visualizations(df_clean, "predefined")

    return render_template('predefined.html', plot_path=plot_path)

@app.route('/live')
def live():
    # Reusing predefined for now
    df = pd.read_csv('data/dataset.csv')
    df_clean = preprocess_data(df)
    plot_path = generate_visualizations(df_clean, "live")

    return render_template('live.html', plot_path=plot_path)

if __name__ == '__main__':
    app.run(debug=True)
