import pytesseract
from PIL import Image

#print tesserocr.tesseract_version()  # print tesseract-ocr version
#print tesserocr.get_languages()  # prints tessdata path and list of available languages

image = Image.open('test6.png')
print(pytesseract.image_to_string(image))  # print ocr text from image
