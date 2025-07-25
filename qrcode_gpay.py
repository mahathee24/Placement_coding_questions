import qrcode

upi_id = "mahatheefiddle2004@okhdfcbank"
name = "Mahathee"
amount = "1"  ,
currency = "INR"

# Build UPI payment URL
upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"

# Create and save QR code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(upi_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("gpay_qr.png")

print(" Google Pay QR code saved as gpay_qr.png")
