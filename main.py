import qrcode as qr
from PIL import Image
import cv2
import webbrowser

choice = input("Enter 1 to generate QR code from URL and 2 for URL from QR code \n(for choice 2, make sure the input QR code is present in the directory as 'QR-input.jpg') :\n")
if(choice == "1"):
    link = input("Enter the URL to generate QR code for:")
    image = qr.make(link)
    image.save("QR-output.jpg")
    print("Generating QR...")
    qr_gen = Image.open(r'QR-output.jpg')
    qr_gen.show()
elif(choice == "2"):
    det = cv2.QRCodeDetector()
    val, points, straight_qrcode = det.detectAndDecode(cv2.imread("QR-input.jpg"))
    print("Opening URL...")
    webbrowser.open(val)
else:
    print("ERROR...invalid option chosen")

