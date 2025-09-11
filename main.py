from flask import Flask, render_template, request, redirect, url_for, session
import pytesseract
import cv2
import os
from werkzeug.utils import secure_filename



app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure secret key
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max 16MB upload

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp', 'tiff'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('index.html', error='No file part')
        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Read and preprocess the image
            image = cv2.imread(filepath)
            if image is None:
                return render_template('index.html', error='Invalid image file')

            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Resize image to improve OCR accuracy (scale up by 2x)
            scale_percent = 200  # percent of original size
            width = int(gray_image.shape[1] * scale_percent / 100)
            height = int(gray_image.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized_image = cv2.resize(gray_image, dim, interpolation=cv2.INTER_LINEAR)

            # Apply Gaussian blur to reduce noise
            blurred_image = cv2.GaussianBlur(resized_image, (5, 5), 0)

            # Apply binary thresholding for better OCR on handwritten text
            thresh_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

            # Perform OCR with fine-tuned config to improve handwritten text recognition
            # --oem 1: LSTM OCR Engine, --psm 6: Assume a single uniform block of text
            custom_config = r'--oem 1 --psm 6'
            extracted_text = pytesseract.image_to_string(thresh_image, config=custom_config)

            # Manage history in session
            history = session.get('history', [])
            history.insert(0, extracted_text)
            history = history[:10]  # Keep only last 10
            session['history'] = history

            # Optionally delete the uploaded file after processing
            os.remove(filepath)

            return render_template('result.html', extracted_text=extracted_text, history=history)
        else:
            return render_template('index.html', error='Unsupported file type')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
