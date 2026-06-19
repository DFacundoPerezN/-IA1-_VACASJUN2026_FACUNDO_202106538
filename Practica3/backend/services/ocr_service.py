import cv2
import pytesseract

from pdf2image import convert_from_path
import tempfile
import os

def extract_text_from_image(image_path):

    image = cv2.imread(image_path)

    text = pytesseract.image_to_string(image,
        lang="spa")

    return text

def extract_text_from_pdf(pdf_path):

    pages = convert_from_path( pdf_path)

    full_text = ""

    for page in pages:

        with tempfile.NamedTemporaryFile(suffix=".jpg",delete=False) as temp:

            page.save(temp.name, "JPEG" )

            full_text += (extract_text_from_image(temp.name))

            os.remove(temp.name)

    return full_text

