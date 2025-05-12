from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/dashboard/predefined')
def dashboard_predefined():
    df = pd.read_csv('static/data/sample_aqi.csv')
    return render_template('dashboard_predefined.html', tables=[df.head().to_html(classes='data')], titles=df.columns.values)

@app.route('/dashboard/upload', methods=['GET', 'POST'])
def dashboard_upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            return render_template('dashboard_upload.html', tables=[df.head().to_html(classes='data')], titles=df.columns.values)
    return render_template('dashboard_upload.html', tables=None)

@app.route('/dashboard/live')
def dashboard_live():
    return render_template('dashboard_live.html')  # You can integrate API later

if __name__ == '__main__':
    app.run(debug=True)
