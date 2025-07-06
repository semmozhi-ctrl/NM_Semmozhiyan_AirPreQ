#!/usr/bin/env python3
"""
Simple test script to verify all imports work correctly
"""
try:
    print("Testing imports...")
    
    print("✓ Testing Flask import...")
    from flask import Flask
    
    print("✓ Testing pandas import...")
    import pandas as pd
    
    print("✓ Testing modules import...")
    from modules import data_preprocessing, model_training, model_evaluation, api_fetcher, visualizations
    
    print("✓ Testing data loading...")
    import os
    DATA_PATH = os.path.join('data', 'sample_dataset.csv')
    if os.path.exists(DATA_PATH):
        df = data_preprocessing.load_data(DATA_PATH)
        print(f"✓ Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
    else:
        print("✗ Data file not found!")
    
    print("\n🎉 All imports successful! Your Flask app should run correctly.")
    print("📍 You can now run: python app.py")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
except Exception as e:
    print(f"✗ Error: {e}")
