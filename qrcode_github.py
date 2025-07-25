import qrcode

# Replace this with your GitHub repo URL
github_url = "https://github.com/mahathee24"

# Create QR code object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

# Add GitHub URL to QR
qr.add_data(github_url)
qr.make(fit=True)

# Generate and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("github_qr.png")

print(" QR Code saved as github_qr.png")
