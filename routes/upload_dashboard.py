from flask import Blueprint, request, render_template
from modules.eda import visualize_uploaded_data
import os

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        file = request.files['file']
        filepath = os.path.join('datasets', file.filename)
        file.save(filepath)
        visualize_uploaded_data(filepath)
        return send_file('static/outputs/uploaded_visualization.png', mimetype='image/png')
    return render_template('upload.html')
