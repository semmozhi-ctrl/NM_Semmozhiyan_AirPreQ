# DigitalOcean App Platform Deployment Guide for AirPreQ

## Prerequisites
- DigitalOcean account: https://cloud.digitalocean.com/registrations/new
- GitHub repository with your code
- Credit card (required even for free trials)

## Step-by-Step Deployment

### 1. Create DigitalOcean Account
- Sign up at https://cloud.digitalocean.com/
- Verify your email and add payment method

### 2. Push Code to GitHub
```bash
cd d:\NM_Semmozhiyan_AirPreQ
git init
git add .
git commit -m "Initial commit for DigitalOcean deployment"
git remote add origin https://github.com/yourusername/airpreq.git
git push -u origin main
```

### 3. Create App on DigitalOcean

1. Go to DigitalOcean Dashboard
2. Click "Create" → "Apps"
3. Choose "GitHub" as source
4. Connect your GitHub account
5. Select your AirPreQ repository
6. Choose branch (main/master)

### 4. Configure App Settings

#### App Specification:
- **Name**: airpreq-app
- **Region**: Choose closest to your users
- **Plan**: Basic ($5/month) or Development ($0 for static sites)

#### Environment Settings:
- **Environment Type**: Production
- **Build Command**: `pip install -r requirements.txt`
- **Run Command**: `gunicorn app:app`
- **Port**: 8080 (auto-detected)

### 5. Environment Variables
Add these if needed:
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

### 6. Deploy
- Review settings
- Click "Create Resources"
- Wait for deployment (usually 2-5 minutes)

## DigitalOcean App Spec File (Optional)

Create `.do/app.yaml` for infrastructure as code:

```yaml
name: airpreq-app
services:
- environment_slug: python
  github:
    branch: main
    deploy_on_push: true
    repo: yourusername/airpreq
  name: web
  run_command: gunicorn app:app
  environment_variables:
  - key: FLASK_ENV
    value: production
  instance_count: 1
  instance_size_slug: basic-xxs
  routes:
  - path: /
```

## Configuration Details

### Build Settings
- **Build Phase**: Automatic detection of Python app
- **Dependencies**: Installed from `requirements.txt`
- **Build Command**: `pip install -r requirements.txt`

### Runtime Settings
- **Start Command**: `gunicorn app:app`
- **Port**: 8080 (default for DigitalOcean Apps)
- **Health Check**: Automatic HTTP checks

## Monitoring and Management

### View Logs
1. Go to your app dashboard
2. Click "Runtime Logs"
3. Monitor real-time application logs

### View Metrics
- CPU usage
- Memory usage
- Request rates
- Response times

### Scaling
- Vertical scaling: Change instance size
- Horizontal scaling: Increase instance count

## Pricing
- **Basic Plan**: $5/month
- **Professional**: $12/month
- **Development**: Free for static sites only

## Benefits of DigitalOcean App Platform
- ✅ Affordable pricing
- ✅ Built-in monitoring
- ✅ Automatic SSL certificates
- ✅ Global CDN
- ✅ Easy scaling
- ✅ Great performance

## Custom Domain Setup
1. Go to app settings
2. Click "Domains"
3. Add your custom domain
4. Update DNS records as instructed

## Troubleshooting

### Common Issues:

1. **Build Failures**
   - Check `requirements.txt` format
   - Ensure Python version compatibility
   - Review build logs

2. **Runtime Errors**
   - Check runtime logs
   - Verify environment variables
   - Test locally first

3. **Port Issues**
   - DigitalOcean expects port 8080
   - Gunicorn should bind to 0.0.0.0:8080

### Useful Commands:
```bash
# Install DigitalOcean CLI (optional)
snap install doctl

# Configure doctl
doctl auth init

# List apps
doctl apps list

# Get app info
doctl apps get <app-id>
```

## Comparison with Other Platforms

| Feature | DigitalOcean | Heroku | Render |
|---------|--------------|--------|--------|
| Free Tier | No | Yes | Yes |
| Starting Price | $5/month | $7/month | Free |
| Performance | Excellent | Good | Good |
| Ease of Use | Good | Excellent | Excellent |

## Next Steps
1. Set up monitoring alerts
2. Configure custom domain
3. Set up staging environment
4. Implement CI/CD pipeline
5. Add database if needed

Your AirPreQ app should now be running on DigitalOcean! 🚀
