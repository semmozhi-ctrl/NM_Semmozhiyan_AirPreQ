# 🚀 Deploy AirPreQ on Render.com - Step by Step Guide

## Why Render.com?
- ✅ **Free Tier Available** - Perfect for your project
- ✅ **Automatic Deployments** - Push to GitHub and deploy automatically
- ✅ **Built-in SSL** - HTTPS by default
- ✅ **Easy Setup** - No complex configuration needed
- ✅ **Great Performance** - Fast loading times

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure you have:
- ✅ GitHub account with your AirPreQ code
- ✅ All files committed and pushed to GitHub
- ✅ `render.yaml` file (already created!)
- ✅ `requirements.txt` with all dependencies
- ✅ Production-ready Flask app

---

## 🎯 Step-by-Step Deployment

### Step 1: Prepare Your GitHub Repository

1. **Ensure all files are committed**:
```bash
git add .
git commit -m "Ready for Render deployment - AirPreQ v1.0"
git push origin main
```

2. **Verify your repository has these files**:
- ✅ `app.py` (main Flask application)
- ✅ `requirements.txt` (dependencies)
- ✅ `render.yaml` (Render configuration)
- ✅ `templates/` folder (all HTML templates)
- ✅ `static/` folder (CSS, images, JS)
- ✅ `modules/` folder (Python modules)
- ✅ `data/` folder (sample dataset)

### Step 2: Create Render Account

1. **Go to**: [https://render.com](https://render.com)
2. **Sign up** using your GitHub account
3. **Authorize** Render to access your repositories

### Step 3: Create New Web Service

1. **Click** "New +" button in top right
2. **Select** "Web Service"
3. **Choose** "Build and deploy from a Git repository"
4. **Click** "Next"

### Step 4: Connect Your Repository

1. **Select** your GitHub account
2. **Find** your AirPreQ repository
3. **Click** "Connect" next to your repository

### Step 5: Configure Service Settings

Fill in these details:

**Basic Settings:**
- **Name**: `airpreq-app` (or your preferred name)
- **Region**: Choose closest to your users
- **Branch**: `main`
- **Root Directory**: Leave blank
- **Runtime**: `Python 3`

**Build & Deploy:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

**Instance Type:**
- **Free**: Select "Free" for $0/month
- **Memory**: 512 MB (included in free tier)

### Step 6: Environment Variables

Add these environment variables:
- **Key**: `FLASK_ENV` **Value**: `production`
- **Key**: `PORT` **Value**: `10000`

### Step 7: Deploy!

1. **Click** "Create Web Service"
2. **Wait** for the build process (5-10 minutes)
3. **Monitor** the build logs for any issues

---

## 📊 Build Process Monitoring

### What happens during build:
1. ✅ **Clone Repository** - Render downloads your code
2. ✅ **Install Dependencies** - `pip install -r requirements.txt`
3. ✅ **Build Application** - Prepare for production
4. ✅ **Start Server** - Launch with Gunicorn
5. ✅ **Health Check** - Verify app is running

### Build logs will show:
```
==> Cloning from https://github.com/your-username/your-repo...
==> Using Python version 3.11.9
==> Running build command 'pip install -r requirements.txt'...
==> Installing dependencies...
==> Build successful!
==> Starting server with 'gunicorn app:app'...
==> Your service is live at https://airpreq-app.onrender.com
```

---

## 🎉 Your App is Live!

### Access Your Deployed App:
Your AirPreQ application will be available at:
**`https://[your-app-name].onrender.com`**

Example: `https://airpreq-app.onrender.com`

### Test These Features:
1. ✅ **Home Page** - Check all sections load
2. ✅ **About Page** - Verify team profiles and social links
3. ✅ **Analysis Pages** - Test predefined, upload, and live analysis
4. ✅ **Contact Page** - Verify contact form
5. ✅ **Mobile View** - Test responsive design
6. ✅ **All Links** - Check navigation works

---

## 🔧 Post-Deployment Configuration

### Custom Domain (Optional):
1. **Go to** your service settings
2. **Add Custom Domain**
3. **Configure DNS** with your domain provider

### SSL Certificate:
- ✅ **Automatic** - Render provides free SSL
- ✅ **HTTPS** - Your app is secure by default

### Monitoring:
- **View Logs** - Real-time application logs
- **Metrics** - CPU, memory, and request metrics
- **Alerts** - Set up notifications for issues

---

## 🚨 Troubleshooting

### Build Failed?
1. **Check Build Logs** - Look for error messages
2. **Verify requirements.txt** - Ensure all dependencies are listed
3. **Python Version** - Ensure compatibility
4. **File Paths** - Check all imports work

### App Won't Start?
1. **Check Start Command** - Should be `gunicorn app:app`
2. **Port Configuration** - Ensure PORT environment variable is set
3. **Flask App** - Verify `app.py` runs locally

### 404 Errors?
1. **Check Routes** - Verify Flask routes are correct
2. **Static Files** - Ensure CSS/JS files load
3. **Templates** - Check template paths

### Common Solutions:
```bash
# If build fails, check these files:
- requirements.txt (all dependencies listed)
- app.py (Flask app runs without errors)
- templates/ (all HTML files present)
- static/ (CSS, JS, images present)
```

---

## 🔄 Automatic Deployments

### Enable Auto-Deploy:
1. **Settings** → **Build & Deploy**
2. **Auto-Deploy** → Enable
3. **Branch** → `main`

### How it works:
- ✅ Push to GitHub → Automatic deployment
- ✅ Real-time build logs
- ✅ Zero-downtime deployments
- ✅ Rollback capability

---

## 📈 Free Tier Limits

### What's Included:
- ✅ **750 hours/month** - More than enough for testing
- ✅ **512 MB RAM** - Sufficient for Flask apps
- ✅ **Free SSL** - HTTPS included
- ✅ **Custom Domains** - Use your own domain
- ✅ **Automatic Deploys** - GitHub integration

### Fair Use Policy:
- Apps sleep after 15 minutes of inactivity
- Wake up automatically when accessed
- First request may be slower (cold start)

---

## 🎯 Success Checklist

After deployment, verify:
- ✅ App loads at your Render URL
- ✅ All pages work correctly
- ✅ Mobile view is responsive
- ✅ Team profiles display properly
- ✅ Analysis features function
- ✅ No console errors
- ✅ Fast loading times

---

## 🌟 Next Steps

After successful deployment:
1. **Share Your URL** - Show off your deployed app!
2. **Test Thoroughly** - Check all features work
3. **Monitor Performance** - Watch logs and metrics
4. **Gather Feedback** - Get user input for improvements
5. **Plan Updates** - Continuous improvement

---

## 📞 Support

### If you need help:
- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **Community Forum**: [community.render.com](https://community.render.com)
- **GitHub Issues**: Check your repository issues
- **Build Logs**: Always check build logs for errors

---

## 🎉 Congratulations!

Your AirPreQ application is now live on the internet! 🌍

**Your professional air quality prediction platform is deployed and ready to help users worldwide make informed decisions about air quality!**

**Happy Deploying! 🚀**
