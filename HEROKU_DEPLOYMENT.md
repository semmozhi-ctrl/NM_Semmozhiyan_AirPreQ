# Heroku Deployment Guide for AirPreQ

## Prerequisites
- Heroku account (free): https://signup.heroku.com/
- Heroku CLI installed: https://devcenter.heroku.com/articles/heroku-cli
- Git installed

## Files Already Prepared
Your project already has the necessary Heroku files:
- `Procfile` - Tells Heroku how to run your app
- `runtime.txt` - Specifies Python version
- `requirements.txt` - Lists all dependencies

## Step-by-Step Deployment

### 1. Install Heroku CLI
Download and install from: https://devcenter.heroku.com/articles/heroku-cli

### 2. Login to Heroku
```bash
heroku login
```

### 3. Navigate to Your Project
```bash
cd d:\NM_Semmozhiyan_AirPreQ
```

### 4. Initialize Git Repository (if not already done)
```bash
git init
git add .
git commit -m "Initial commit for Heroku deployment"
```

### 5. Create Heroku App
```bash
heroku create airpreq-app
# Or use a custom name:
# heroku create your-custom-app-name
```

### 6. Deploy to Heroku
```bash
git push heroku main
# If your branch is master, use:
# git push heroku master
```

### 7. Open Your App
```bash
heroku open
```

## Heroku Configuration

### Environment Variables (if needed)
```bash
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secret-key-here
```

### View Logs
```bash
heroku logs --tail
```

### Scale Your App
```bash
heroku ps:scale web=1
```

## Heroku File Contents

### Procfile
```
web: gunicorn app:app
```

### runtime.txt
```
python-3.11.0
```

## Troubleshooting

### Common Issues:

1. **Build Failed**
   - Check that all dependencies are in `requirements.txt`
   - Ensure `Procfile` is correctly formatted

2. **App Crashes**
   - Check logs: `heroku logs --tail`
   - Verify your app runs locally first

3. **Module Not Found**
   - Add missing packages to `requirements.txt`
   - Redeploy: `git push heroku main`

### Useful Heroku Commands:
```bash
heroku apps                    # List your apps
heroku logs --tail            # View real-time logs
heroku restart                # Restart your app
heroku config                 # View environment variables
heroku releases               # View deployment history
```

## Heroku Pricing
- **Free Tier**: App sleeps after 30 min of inactivity
- **Hobby ($7/month)**: No sleeping, custom domains
- **Standard ($25/month)**: Auto-scaling, metrics

## Benefits of Heroku
- ✅ Industry standard platform
- ✅ Excellent documentation
- ✅ Git-based deployment
- ✅ Add-ons ecosystem
- ✅ Easy scaling

## Next Steps
1. Set up custom domain (paid plans)
2. Add monitoring with Heroku metrics
3. Set up CI/CD with GitHub integration
4. Configure database add-ons if needed

Your AirPreQ app should now be live on Heroku! 🎉
