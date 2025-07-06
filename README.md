# AirPreQ - Advanced Air Quality Intelligence ✨

> **NEW**: Complete UI/UX redesign with modern dark theme, glass morphism effects, and interactive animations!

![AirPreQ Logo](static/images/logo.png)

## 🌟 What's New in the UI/UX Redesign

### Modern Design Features
- **🎨 Dark Theme**: Sophisticated dark color scheme with gradient accents
- **💎 Glass Morphism**: Translucent glass effects with backdrop blur
- **🎭 Interactive Animations**: Smooth transitions and hover effects
- **📱 Mobile-First**: Fully responsive design for all devices
- **⚡ Performance**: Optimized loading and smooth interactions

### Enhanced User Experience
- **🚀 Hero Sections**: Engaging landing pages with statistics
- **📊 Better Charts**: Dark-themed visualizations with download options
- **📤 Drag & Drop**: Modern file upload interface
- **🎯 Real-time Dashboard**: Live AQI monitoring with health recommendations
- **💫 Micro-interactions**: Delightful animations throughout

## 🚀 Quick Start

### Option 1: Windows Batch File (Easiest)
```bash
# Simply double-click the file:
start_airpreq.bat
```

### Option 2: Python Launcher
```bash
python run_airpreq.py
```

### Option 3: Direct Flask Run
```bash
# Install dependencies first
pip install -r requirements.txt

# Run the application
python app.py
```

## 📱 Access the Website

Once running, open your browser and go to:
**http://127.0.0.1:5000**

## 🛠️ Features

### 🏠 Home Page
- Modern hero section with animated background
- Feature cards with interactive hover effects
- Statistics dashboard
- Call-to-action sections with gradients

### 📊 Analysis Pages
- **Predefined Dataset**: Enhanced chart containers with dark theme
- **Upload Dataset**: Drag & drop file upload with progress indicators
- **Live Analysis**: Real-time AQI predictions with health recommendations

### 👥 About Page
- Professional team member presentations
- Animated social media links
- Technology stack showcase
- Mission and vision sections

### 📧 Contact Page
- Modern contact form with floating labels
- Interactive FAQ section
- Social media integration
- Quick contact information

## 🎨 Design System

### Color Palette
- **Primary**: Purple-blue gradients (#667eea → #764ba2)
- **Background**: Dark slate (#0f172a, #1e293b)
- **Text**: Light grays (#f8fafc, #cbd5e1)
- **Accents**: Blue (#3b82f6), Green (#10b981), Orange (#f59e0b)

### Typography
- **Headings**: Plus Jakarta Sans (600-700 weight)
- **Body**: Inter (300-500 weight)
- **Gradients**: Text with gradient overlays for emphasis

### Components
- **Cards**: Glass morphism with blur effects
- **Buttons**: Gradient backgrounds with hover animations
- **Navigation**: Fixed navbar with scroll effects
- **Forms**: Floating labels with focus states

## 📋 Requirements

```
Flask==3.1.0
pandas==2.2.3
scikit-learn==1.6.1
matplotlib==3.9.2
seaborn==0.13.2
plotly==6.1.0
requests==2.32.3
```

## 🏗️ Project Structure

```
NM_Semmozhiyan_AirPreQ/
├── app.py                 # Main Flask application
├── run_airpreq.py        # Launch script with dependency checks
├── start_airpreq.bat     # Windows batch launcher
├── requirements.txt      # Python dependencies
├── data/
│   └── sample_dataset.csv
├── modules/
│   ├── api_fetcher.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   ├── utils.py
│   └── visualizations.py
├── static/
│   ├── css/
│   │   └── styles.css    # Additional custom styles
│   ├── images/          # Team photos and assets
│   └── js/
│       └── scripts.js
└── templates/
    ├── base.html         # Modern base template with dark theme
    ├── home.html         # Redesigned homepage
    ├── about.html        # Team page with animations
    ├── contact.html      # Modern contact form
    ├── analysis_predefined.html
    ├── analysis_upload.html
    └── analysis_live.html
```

## 👨‍💻 Team

- **Sivabalan V** - Project Manager & QA Engineer
- **Dhyanesh V** - Backend Developer & Deployment Engineer  
- **Semmozhiyan NS** - Machine Learning Engineer & AI Specialist
- **Sri Sabarish U** - Data Collection & Preprocessing Lead
- **Chandru M** - UI/UX Designer & Documentation Lead

## 🌐 Technologies Used

- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript, AOS Animations
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, numpy
- **Visualization**: Plotly, matplotlib, seaborn
- **APIs**: IQAir AirVisual API
- **Deployment**: Gunicorn, Render

## 📄 License

MIT License - feel free to use this project for learning and development!

---

**✨ Experience the new modern AirPreQ interface - where air quality meets beautiful design! ✨**