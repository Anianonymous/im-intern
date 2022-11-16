import cv2
from pytesseract import pytesseract
image=cv2.imread(r"C:\Users\hegde\Downloads\assignment_img_vrf\images\result_Page_1.jpg",0)
thresh=cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
pytesseract.tesseract_cmd=r"C:\Users\hegde\Tesseract-OCR\tesseract.exe"
data=pytesseract.image_to_string(thresh,lang='eng',config='--psm 6')
print(data)