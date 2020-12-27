from pytesseract import Output
import pdf2image
import cv2




try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
#pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
#print(pytesseract.image_to_string(Image.open('/home/moshe/Downloads/test.png')))

# List of available languages
def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(file):
    text = pytesseract.image_to_string(file,lang='eng')
    #print(pytesseract.image_to_string(Image.open('/home/moshe/Downloads/test.png'), lang='heb'))
    return text

def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        print(ocr_core(img))

#print_pages("/home/moshe/workspace/projects/Automation/mail_server/electric_bill/2020-471639834_20201112_174309.pdf")


#print(pytesseract.get_languages(config=''))

# French text image to string
print(pytesseract.image_to_string(Image.open('/home/moshe/Downloads/test.png'), lang='heb'))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
#print(pytesseract.image_to_string('test.png'))

# Batch processing with a single file containing the list of multiple image file paths
#print(pytesseract.image_to_string('images.txt'))

'''
# Timeout/terminate the tesseract job after a period of time
try:
    print(pytesseract.image_to_string('/home/moshe/Downloads/test.png', timeout=2)) # Timeout after 2 seconds
    print(pytesseract.image_to_string('/home/moshe/Downloads/test.png', timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass
'''


# Get bounding box estimates
#boxes = pytesseract.image_to_boxes(Image.open('/home/moshe/Downloads/test.png'))

# Get verbose data including boxes, confidences, line and page numbers

img = cv2.imread('/home/moshe/Downloads/test.png')
d = pytesseract.image_to_data(img,lang="heb",output_type=Output.DICT)
print (d)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open('/home/moshe/Downloads/test.png')))

# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('/home/moshe/Downloads/test.png', extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default

# Get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr('/home/moshe/Downloads/test.png', extension='hocr')

# Get ALTO XML output
xml = pytesseract.image_to_alto_xml('/home/moshe/Downloads/test.png')