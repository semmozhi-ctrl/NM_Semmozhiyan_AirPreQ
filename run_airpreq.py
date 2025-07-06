#!/usr/bin/env python3
"""
AirPreQ - Advanced Air Quality Intelligence
Launch Script with Modern UI/UX Design

Run this script to start the AirPreQ website with the new modern interface.
"""

import sys
import os
import subprocess

def check_dependencies():
    """Check if all required packages are installed."""
    required_packages = [
        'flask',
        'pandas', 
        'sklearn',
        'matplotlib',
        'seaborn',
        'plotly',
        'requests'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} - OK")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    print("\n🎉 All dependencies are installed!")
    return True

def run_app():
    """Run the AirPreQ Flask application."""
    print("=" * 60)
    print("🚀 AIRPREQ - ADVANCED AIR QUALITY INTELLIGENCE")
    print("=" * 60)
    print("✨ New Modern UI/UX Design Features:")
    print("   • Dark theme with glass morphism effects")
    print("   • Interactive animations and transitions")
    print("   • Modern gradient design system")
    print("   • Responsive mobile-first layout")
    print("   • Enhanced data visualizations")
    print("   • Real-time air quality predictions")
    print("=" * 60)
    
    if not check_dependencies():
        return
    
    print("\n🌐 Starting Flask development server...")
    print("📍 Website will be available at: http://127.0.0.1:5000")
    print("🔧 Debug mode: ON")
    print("\n⚡ Press Ctrl+C to stop the server")
    print("-" * 60)
    
    try:
        # Import and run the Flask app
        from app import app
        app.run(host='127.0.0.1', port=5000, debug=True)
    except KeyboardInterrupt:
        print("\n\n👋 AirPreQ server stopped. Thank you for using AirPreQ!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print("Please check the error message above and try again.")

if __name__ == "__main__":
    run_app()
