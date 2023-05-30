import cv2
from pyzbar import pyzbar

def detect_barcode(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Decode the barcode
    barcodes = pyzbar.decode(gray)

    if barcodes:
        for barcode in barcodes:
            barcode_data = barcode.data.decode("utf-8")
            print("Barcode Data:", barcode_data)
    else:
        print("No barcode detected.")

# Specify the path to your image
image_path = r"C:\Users\taave\Desktop\SDA\barcode.jpg"

# Call the function to detect the barcode
detect_barcode(image_path)
