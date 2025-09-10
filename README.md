# Handwriting to Text Converter

## About The Project

This project is a simple but powerful tool that converts handwritten notes into digital text. It uses Python and a technology called OCR (Optical Character Recognition) to "read" the text from an image and make it searchable and editable.

This project was developed as a backend for the "NEXATHON 2025" to demonstrate a working model of a handwriting recognition system.

### Built With

* Python
* Tesseract OCR
* PyTesseract
* Pillow
* OpenCV-Python

## Getting Started

To get a copy of this project up and running on your local machine, follow these steps.

### Prerequisites

You need to have Python and Tesseract OCR installed on your computer.

* Tesseract OCR: Download the installer from the official repository.
    

### Installation

1.  Clone the Repository
    
2.  Create a Virtual Environment
   
3.  Activate the Virtual Environment
    
4.  Install Required Libraries [Pip install pytesseract, pillow, opencv-python]
    
5.  Set the Tesseract Path
    Open the main.py file and make sure the pytesseract.pytesseract.tesseract_cmd line points to the correct location of your tesseract.exe file.

    
## Usage

1.  Place an image file of your handwritten notes in the same folder as the main.py script.[FILE NAME MUST BE "handwritten_notes.png"]

2.  Run the script from your terminal [Make sure to activate the "Virtual Enviroment"]
   
3.  The extracted text will be printed in your terminal. A preprocessed image will also be saved as preprocessed_image.png for you to see.

## License

This project is licensed under the *"All Rights Reserved"* license. Please see the LICENSE file for details.

## Contact

* *Imran Biswas* - [https://github.com/Diggajmanushya]
* Project Link: [https://github.com/Diggajmanushya/Handwriting-to-text-project]