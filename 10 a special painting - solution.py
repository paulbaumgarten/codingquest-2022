# Sample solution for Coding Quest 2022 day 10
# Paul Baumgarten 2022
# codingquest.io

import requests
from PIL import Image
from io import BytesIO

# Download and open the image
res = requests.get("https://codingquest.io/may2022/010-inputdata-327485957345.png")
img = Image.open(BytesIO(res.content))  # Load the binary content returned into a PILLOW image
print(img.size, img.mode)
w,h = img.size

# Setup our variables
message = []            # Content of decoded message
current_byte = 0        # The value of the current byte we are creating bit by bit
bit_number = 0          # WHich bit number of the above byte we are up to
stop = False            # Flag to stop when we hit the appropriate marker

# Process the image data
for y in range(h):                      # For every row
    for x in range(w):                  # For every pixel in the row
        r,g,b = img.getpixel((x,y))     # Get the pixel
        if not stop:
            current_byte = (current_byte<<1) + (r & 0b00000001)
            bit_number = bit_number+1
            if bit_number == 8:         # Every 8 bits, determine what the byte is
                message.append(chr(current_byte)) # Add the byte to our message
                if current_byte == 0:   # Stop processing if we get a 00 byte
                    stop = True
                bit_number = 0
                current_byte = 0

# Let's see our message!
print("".join(message))
