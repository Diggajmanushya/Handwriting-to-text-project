#
# Copyright (c) 2025 Imran Biswas. All rights reserved.
# This code is the intellectual property of Imran Biswas for the
# purpose of the first hackathon. Unauthorized copying or distribution is prohibited.
#
import pytesseract
from PIL import Image
import cv2

# IMPORTANT: If Tesseract is not in your system PATH, you need to set the path here.
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract' # Update this path as necessary

# --- Step 1: Preprocess the Image ---
# Put an image of a handwritten note in the same folder as this script.
image_path = 'handwritten_note.png'

try:
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    # Check if the image was loaded correctly
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please make sure you have an image file in the same directory as your script.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to get a clean black and white image
thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
# Optional: Save the preprocessed image to see what it looks like
cv2.imwrite('preprocessed_image.png', thresh_image)

# --- Step 2: Perform OCR ---
# Now, use pytesseract on the preprocessed image
extracted_text = pytesseract.image_to_string(thresh_image)

# --- Step 3: Display the Output ---
print("--------------------")
print("Extracted Text:")
print("--------------------")
print(extracted_text)