__import__("os").system("pip install pyqrcode")
__import__("os").system("pip install pypng")

import pyqrcode

# String which represents the QR code
s = "https://github.com/SanCody"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 8)
