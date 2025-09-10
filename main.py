from flask import Flask, render_template, request, redirect, url_for
import pytesseract
import cv2
import os
from werkzeug.utils import secure_filename

# IMPORTANT: If Tesseract is not in your system PATH, you need to set the path here.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
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
            thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

            # Perform OCR
            extracted_text = pytesseract.image_to_string(thresh_image)

            # Optionally delete the uploaded file after processing
            os.remove(filepath)

            return render_template('result.html', extracted_text=extracted_text)
        else:
            return render_template('index.html', error='Unsupported file type')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
