from flask import Blueprint, send_file
from modules.eda import visualize_live_data

live_bp = Blueprint('live', __name__)

@live_bp.route('/live')
def live_data():
    visualize_live_data()
    return send_file('static/outputs/live_visualization.png', mimetype='image/png')
