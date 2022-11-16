import cv2
from pytesseract import pytesseract
image=cv2.imread(r"C:\Users\hegde\Downloads\assignment_img_vrf\images\result_Page_7.jpg",0)
thresh=cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
pytesseract.tesseract_cmd=r"C:\Users\hegde\Tesseract-OCR\tesseract.exe"
data=pytesseract.image_to_string(thresh,lang='eng',config='--psm 6')
print(data)
# import easyocr
# import numpy as np
# reader=easyocr.Reader(['th','en'])
# bounds = reader.readtext(r"C:\Users\hegde\Downloads\assignment_img_vrf\images\result_Page_5.jpg")
# print(bounds)