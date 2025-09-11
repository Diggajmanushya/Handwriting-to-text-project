# Deployment Steps for Render

## Completed
- [x] Updated main.py for production (removed Windows tesseract path, set host/port)
- [x] Created render.yaml for build and start commands

## Next Steps
- [ ] Commit and push the changes to your GitHub repository
- [ ] Go to [Render.com](https://render.com) and sign in
- [ ] Click "New" and select "Web Service"
- [ ] Connect your GitHub repository: https://github.com/Diggajmanushya/Handwriting-to-text-project
- [ ] Configure the service:
  - Name: handwriting-to-text
  - Environment: Python
  - Build Command: apt-get update && apt-get install -y tesseract-ocr
  - Start Command: python main.py
- [ ] Click "Create Web Service"
- [ ] Wait for the build and deployment to complete
- [ ] Access your app at the provided URL

## Notes
- Render will automatically install dependencies from requirements.txt
- Tesseract OCR will be installed during the build process
- The app is configured to run on the port provided by Render
