from flask import Flask, render_template
from routes.predefined_dashboard import predefined_bp
from routes.upload_dashboard import upload_bp
from routes.live_dashboard import live_bp

app = Flask(__name__)
app.register_blueprint(predefined_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(live_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
