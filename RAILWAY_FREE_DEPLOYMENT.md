# Railway.app Free Deployment Guide (No Credit Card)

## Why Railway?
- ✅ **No credit card required** to start
- ✅ **$5 free credit monthly** (lasts ~30 days)
- ✅ **No app sleeping**
- ✅ **Automatic deployments from GitHub**
- ✅ **Custom domains**
- ✅ **Built-in databases**

## Step-by-Step Deployment

### 1. Push Your Code to GitHub

```bash
cd d:\NM_Semmozhiyan_AirPreQ

# Initialize git (if not done)
git init
git add .
git commit -m "Initial commit for Railway deployment"

# Create GitHub repo and push
git remote add origin https://github.com/yourusername/airpreq.git
git branch -M main
git push -u origin main
```

### 2. Sign Up for Railway (No Credit Card!)

1. Go to: https://railway.app/
2. Click "Start a New Project"
3. Sign up with GitHub (recommended)
4. **No credit card required!**

### 3. Deploy from GitHub

1. **Connect Repository**:
   - Click "Deploy from GitHub repo"
   - Select your AirPreQ repository
   - Railway will auto-detect it's a Python app

2. **Configure Build**:
   - Railway automatically detects `requirements.txt`
   - Uses your existing `Procfile` if present
   - Auto-configures Python environment

3. **Environment Variables** (Optional):
   ```
   FLASK_ENV=production
   SECRET_KEY=your-secret-key-here
   ```

4. **Deploy**:
   - Click "Deploy"
   - Wait 2-3 minutes for build
   - Get your live URL!

### 4. Access Your App

Railway provides a URL like:
```
https://airpreq-production.up.railway.app/
```

## Alternative: Deploy via Railway CLI

### Install Railway CLI
```bash
# Using npm (if you have Node.js)
npm install -g @railway/cli

# Or download from: https://github.com/railwayapp/cli/releases
```

### Deploy via CLI
```bash
cd d:\NM_Semmozhiyan_AirPreQ

# Login to Railway
railway login

# Initialize project
railway init

# Deploy
railway up
```

## Railway Configuration Files

### railway.json (Optional)
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "restartPolicyType": "ON_FAILURE",
    "startCommand": "gunicorn app:app"
  }
}
```

### nixpacks.toml (Optional)
```toml
[phases.build]
cmds = ["pip install -r requirements.txt"]

[phases.deploy]
cmd = "gunicorn app:app"
```

## Managing Your Railway App

### View Logs
```bash
railway logs
```

### Add Environment Variables
```bash
railway variables set FLASK_ENV=production
railway variables set SECRET_KEY=your-secret-key
```

### Connect Custom Domain
1. Go to Railway dashboard
2. Click your project → Settings → Domains
3. Add your custom domain
4. Update DNS records as shown

### Database (Optional)
```bash
# Add PostgreSQL
railway add postgresql

# Add MySQL
railway add mysql

# Add Redis
railway add redis
```

## Railway Free Limits

- **$5 credit per month** (auto-renewed)
- **750 hours execution time** (~30 days)
- **100GB outbound bandwidth**
- **1GB memory per service**
- **1 vCPU per service**
- **Unlimited projects**

## Project Structure for Railway

Your current structure is perfect:
```
airpreq/
├── app.py              # Main Flask app
├── requirements.txt    # Dependencies
├── Procfile           # Process configuration
├── runtime.txt        # Python version
├── templates/         # HTML templates
├── static/           # CSS, JS, images
└── modules/          # Python modules
```

## Troubleshooting

### Build Failures
1. **Check requirements.txt**:
   ```bash
   # Ensure all dependencies are listed
   pip freeze > requirements.txt
   ```

2. **Python version**:
   ```bash
   # Update runtime.txt
   echo "python-3.11.0" > runtime.txt
   ```

3. **Port configuration**:
   ```python
   # In app.py, use PORT environment variable
   import os
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0', port=port)
   ```

### Deployment Issues
```bash
# Check logs
railway logs

# Restart service
railway restart

# Check variables
railway variables
```

### Memory Issues
```bash
# Optimize your app for limited memory
# Use gunicorn with fewer workers
gunicorn --workers 1 --threads 2 app:app
```

## Monitoring Your Usage

1. **Dashboard**: Check credit usage at railway.app
2. **Alerts**: Set up usage alerts
3. **Metrics**: Monitor memory and CPU usage

## After Free Credit Expires

### Option 1: Add Payment Method
- Add credit card to continue
- Pay only for usage above free tier

### Option 2: Switch Platforms
- Move to Render.com
- Convert to Streamlit Cloud
- Use multiple free platforms

### Option 3: Optimize Usage
- Scale down during low usage
- Optimize code for efficiency
- Use caching to reduce CPU

## Pro Tips

1. **Enable GitHub Auto-Deploy**:
   - Connects to your GitHub repo
   - Auto-deploys on git push

2. **Use Environment Variables**:
   - Store secrets safely
   - Different configs for dev/prod

3. **Monitor Usage**:
   - Check dashboard regularly
   - Set up usage alerts

4. **Optimize for Railway**:
   - Use gunicorn for production
   - Implement health checks
   - Add logging

Your AirPreQ app should be live on Railway in minutes! 🚂

**Live URL**: https://your-app-name.up.railway.app/
