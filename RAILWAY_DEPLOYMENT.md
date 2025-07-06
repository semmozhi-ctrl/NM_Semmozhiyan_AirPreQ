# Railway.app Deployment Guide for AirPreQ

Railway is an excellent platform for deploying Flask applications with ML models. It offers automatic deployments, built-in databases, and excellent performance.

## Prerequisites
- GitHub repository with your AirPreQ code
- Railway account (free tier available)

## Step 1: Prepare Your Project

### 1.1 Create railway.json (Railway-specific config)
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn --bind 0.0.0.0:$PORT app:app",
    "healthcheckPath": "/",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### 1.2 Update requirements.txt (if needed)
Your current requirements.txt should work perfectly with Railway.

## Step 2: Deploy to Railway

### Method 1: Deploy from GitHub (Recommended)

1. **Connect Repository**:
   - Go to [railway.app](https://railway.app)
   - Sign in with GitHub
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your AirPreQ repository

2. **Configure Environment**:
   - Railway will auto-detect it's a Python project
   - Set environment variables in the Railway dashboard:
     ```
     IQAIR_API_KEY=your_api_key_here
     FLASK_ENV=production
     ```

3. **Deploy**:
   - Railway automatically builds and deploys
   - You'll get a URL like: `https://your-project.railway.app`

### Method 2: Deploy with Railway CLI

1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and Initialize**:
   ```bash
   railway login
   cd d:\NM_Semmozhiyan_AirPreQ
   railway init
   ```

3. **Deploy**:
   ```bash
   railway up
   ```

## Step 3: Configure Domain (Optional)

1. Go to your project settings in Railway dashboard
2. Click "Domains"
3. Add custom domain or use the provided railway.app subdomain

## Step 4: Environment Variables

Set these in Railway dashboard > Variables:
```
IQAIR_API_KEY=your_api_key_here
FLASK_ENV=production
PORT=8080
```

## Step 5: Monitor and Scale

Railway provides:
- Real-time logs
- Metrics dashboard
- Auto-scaling
- Database integration

## Advantages of Railway:
- ✅ Excellent for Python/Flask apps
- ✅ Built-in PostgreSQL if needed
- ✅ Great performance and speed
- ✅ Simple deployment process
- ✅ Good free tier
- ✅ Automatic HTTPS
- ✅ Git-based deployments

## Troubleshooting:

### Build Issues:
```bash
# Check build logs in Railway dashboard
# Ensure all dependencies are in requirements.txt
```

### Runtime Issues:
```bash
# Check application logs in Railway dashboard
# Verify environment variables are set
```

## Estimated Costs:
- **Free Tier**: $5 credit/month, good for development
- **Pro Plan**: $20/month for production apps
- **Pay-as-you-go**: Beyond free tier usage

Railway is highly recommended for Flask + ML applications due to its simplicity and performance!
