from flask import Blueprint, render_template, send_file
from modules.eda import visualize_predefined_data

predefined_bp = Blueprint('predefined', __name__)

@predefined_bp.route('/predefined')
def show_predefined():
    visualize_predefined_data()
    return send_file('static/outputs/predefined_visualization.png', mimetype='image/png')
