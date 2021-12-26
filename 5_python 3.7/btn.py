import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
# Create the SSD1306 OLED class.
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Input pins:
scrollBTN = DigitalInOut(board.D13)
scrollBTN.direction = Direction.INPUT
scrollBTN.pull = Pull.UP

menuBTN = DigitalInOut(board.D26)
menuBTN.direction = Direction.INPUT
menuBTN.pull = Pull.UP

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)


while True:

    if scrollBTN.value:  # button is released
        draw.ellipse((70, 40, 90, 60), outline=255, fill=0)  # scroll button
    else:  # button is pressed:
        draw.ellipse((70, 40, 90, 60), outline=255, fill=1)  # scroll button filled

    if menuBTN.value:  # button is released
        draw.ellipse((100, 20, 120, 40), outline=255, fill=0)  # menu button
    else:  # button is pressed:
        draw.ellipse((100, 20, 120, 40), outline=255, fill=1)  # menu button filled
    
    disp.image(image)
    disp.show()