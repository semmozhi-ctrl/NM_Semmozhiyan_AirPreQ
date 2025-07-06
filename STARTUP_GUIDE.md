# 🚀 AirPreQ - Quick Start Guide

## Prerequisites Check ✅

Before running the application, make sure you have:
- Python 3.8+ installed
- All required packages installed (see requirements.txt)

## Installation Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Installation**
   ```bash
   python test_imports.py
   ```

## Running the Application

### Option 1: Direct Python Command
```bash
python app.py
```

### Option 2: Using Batch File (Windows)
```bash
run_app.bat
```

### Option 3: Using the Run Script
```bash
python run_airpreq.py
```

## Accessing the Application

Once running, open your web browser and navigate to:
**http://127.0.0.1:5000**

## Troubleshooting 🔧

### Common Issues & Solutions:

1. **Import Errors**
   - Run: `pip install -r requirements.txt`
   - Check: `python test_imports.py`

2. **Port Already in Use**
   - Change port in app.py: `app.run(port=5001)`
   
3. **File Upload Issues**
   - Ensure CSV files have proper headers
   - Check file permissions

4. **Module Not Found**
   - Verify you're in the correct directory
   - Check that `modules/__init__.py` exists

### File Structure Verification:
```
AirPreQ/
├── app.py              # Main Flask application
├── requirements.txt    # Dependencies
├── test_imports.py     # Import verification
├── run_app.bat        # Windows batch file
├── data/
│   └── sample_dataset.csv
├── modules/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   ├── api_fetcher.py
│   └── visualizations.py
├── templates/          # HTML templates
└── static/            # CSS, JS, images
```

## Features 🌟

✨ **Modern UI/UX Design**
- Dark theme with glass morphism effects
- Responsive design for all devices
- Interactive data visualizations
- Smooth animations and transitions

📊 **Analysis Options**
1. **Predefined Dataset**: Analyze built-in air quality data
2. **Upload Dataset**: Upload your own CSV files for analysis
3. **Live Data**: Real-time air quality predictions

🔬 **Machine Learning Models**
- Linear Regression
- Random Forest
- Model evaluation metrics (RMSE, R²)
- Feature importance analysis

## Support

If you encounter any issues:
1. Check this troubleshooting guide
2. Verify all dependencies are installed
3. Run the test_imports.py script
4. Ensure you're using the correct Python version

Happy analyzing! 🌍💨
