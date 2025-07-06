#!/usr/bin/env python3
"""
Production deployment test script
Tests the app in production mode locally before deploying
"""
import os
import subprocess
import sys

def test_production_mode():
    """Test the app in production mode"""
    print("🧪 Testing AirPreQ in Production Mode")
    print("=" * 50)
    
    # Set production environment
    os.environ['FLASK_ENV'] = 'production'
    os.environ['PORT'] = '5000'
    
    print("✓ Environment set to production")
    print("✓ Port set to 5000")
    
    # Check dependencies
    try:
        import flask
        import pandas
        import sklearn
        import matplotlib
        import seaborn
        import plotly
        import requests
        print("✓ All Python dependencies available")
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        return False
    
    # Test import of our modules
    try:
        from modules import data_preprocessing, model_training, model_evaluation, api_fetcher, visualizations
        print("✓ All custom modules import successfully")
    except ImportError as e:
        print(f"✗ Module import error: {e}")
        return False
    
    # Check data file
    if os.path.exists('data/sample_dataset.csv'):
        print("✓ Sample dataset found")
    else:
        print("✗ Sample dataset missing")
        return False
    
    # Check static files
    static_files = [
        'static/css/styles.css',
        'static/images/logo.png',
        'templates/base.html',
        'templates/home.html'
    ]
    
    for file_path in static_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path} found")
        else:
            print(f"✗ {file_path} missing")
            return False
    
    print("\n🎉 All pre-deployment checks passed!")
    print("🚀 Your app is ready for deployment!")
    
    return True

def run_production_server():
    """Run the app with gunicorn for production testing"""
    print("\n🔥 Starting production server with Gunicorn...")
    print("📍 Access your app at: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    
    try:
        # Run with gunicorn
        subprocess.run([
            'gunicorn', 
            '--bind', '0.0.0.0:5000',
            '--workers', '1',
            '--timeout', '120',
            'app:app'
        ])
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except FileNotFoundError:
        print("\n⚠️  Gunicorn not found. Installing...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'gunicorn'])
        print("✓ Gunicorn installed. Please run the script again.")

if __name__ == "__main__":
    if test_production_mode():
        choice = input("\n🤔 Do you want to test the production server locally? (y/n): ")
        if choice.lower() in ['y', 'yes']:
            run_production_server()
        else:
            print("\n✅ Pre-deployment testing complete!")
            print("📝 Check DEPLOYMENT_GUIDE.md for deployment instructions")
    else:
        print("\n❌ Pre-deployment checks failed!")
        print("🔧 Please fix the issues above before deploying")
