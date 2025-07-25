import qrcode  

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data("https://www.google.com")

qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("my_qrcode.png")
