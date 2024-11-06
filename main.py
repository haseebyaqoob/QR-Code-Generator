import qrcode
a = input("Enter the URL to generate QR Code:\n")

img = qrcode.make(f'{a}')
type(img)  
img.save("qrcode.png")