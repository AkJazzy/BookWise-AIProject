import pandas as pd
import pytesseract
from PIL import Image
import pdfplumber

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    return pytesseract.image_to_string(image)

def load_txt(file):
    return file.read().decode("utf-8")