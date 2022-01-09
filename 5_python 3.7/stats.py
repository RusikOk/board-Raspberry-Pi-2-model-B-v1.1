# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import time
import subprocess
import board
from board import SCL, SDA
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Input pins:
scrollBTN = DigitalInOut(board.D13)
scrollBTN.direction = Direction.INPUT
scrollBTN.pull = Pull.UP

okBTN = DigitalInOut(board.D26)
okBTN.direction = Direction.INPUT
okBTN.pull = Pull.UP

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

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()

# rusikok
i = 0; # счетчик для анимации в последнем столбце дисплея
scrollIndex = 1; # счетчик для хранения текущего экрана с параметрами
sleepIndex = 0; # счетчик для хранения текущего пункта меню

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)

while True:

    # очистка всего поля дисплея
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    # обработка нажатий кнопки меню
    if scrollBTN.value == 0:
        scrollIndex = scrollIndex + 1 # шагаем по пунктам меню
        sleepIndex = 0 # при нажатии на кнопку начинаем отображение данных
        time.sleep(0.3)
        if scrollIndex > 6:
            scrollIndex = 1

    # активация хранителя экрана после 1000 циклов обновления. не точно но это не принципиально
    sleepIndex = sleepIndex + 1
    if sleepIndex > 10000:
    	scrollIndex = 0

    # отображаем страницы с различной системной информацией
    if scrollIndex == 0:
    	text0 = ""
    	text1 = ""
    	text2 = ""
    	text3 = ""
    elif scrollIndex == 1:
    	# Shell scripts for system monitoring from here:
    	# https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    	cmd = "hostname -I | cut -d' ' -f1"
    	text0 = "IP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
    	cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    	text1 = subprocess.check_output(cmd, shell=True).decode("utf-8")
    	cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB %.0f%%\", $3,$2,$3*100/$2 }'"
    	text2 = subprocess.check_output(cmd, shell=True).decode("utf-8")
    	cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %.2f/%.1f GB %s", $3,$2,$5}\''
    	text3 = subprocess.check_output(cmd, shell=True).decode("utf-8")
    elif scrollIndex == 2:
        cmd = "vcgencmd measure_temp | cut -f2 -d= | sed 's/000//'"
        text0 = "TCPU: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "vcgencmd measure_clock arm | awk -F\"=\" '{printf (\"%0.0f\",$2/1000000); }'"
        text1 = "FCPU: " + subprocess.check_output(cmd, shell=True).decode("utf-8") + " MHz"
        cmd = "vcgencmd measure_volts | cut -f2 -d= | sed 's/000//'"
        text2 = "VCPU: " + subprocess.check_output(cmd, shell=True).decode("utf-8") + " V"
        cmd = "vcgencmd get_throttled | cut -f2 -d="
        text3 = "throttled: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
    elif scrollIndex == 3:
        cmd = "ip a | grep \"  inet \" | head -n 4 | cut -d \" \" -f 6 | cut -d / -f 1"
        str = subprocess.check_output(cmd, shell=True).decode("utf-8")
        # разбиваем полученные из консоли данные на список построчно
        list = []
        for line in str.split("\n"):
            if not line.strip():
                continue
            list.append(line.lstrip())
            #print(list)
        # костыль, чтобы избежать попытки доступа к несуществующему элементу списка
        list.append(" -- // -- ")
        list.append(" -- // -- ")
        list.append(" -- // -- ")
        list.append(" -- // -- ")
        # тасуем список по переменным для вывода
        text0 = "IP0: " + list[0]
        text1 = "IP1: " + list[1]
        text2 = "IP2: " + list[2]
        text3 = "IP3: " + list[3]
    elif scrollIndex == 4:
    	text0 = "S H U T D O W N"
    	text1 = "S H U T D O W N"
    	text2 = "S H U T D O W N"
    	text3 = "S H U T D O W N"
    elif scrollIndex == 5:
    	text0 = "R E B O O T"
    	text1 = "R E B O O T"
    	text2 = "R E B O O T"
    	text3 = "R E B O O T"
    elif scrollIndex == 6:
        cmd = "date +\"%F\""
        text0 = "DATE: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "date +\"%T\""
        text1 = "TIME: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "uptime | awk -F'( |,|:)+' '{d=h=m=0; if($7==\"min\") m=$6; else { if($7~/^day/) { d=$6; h=$8; m=$9 } else if($9==\"min\") { h=0; m=$8 } else { h=$6; m=$7 }}} {printf(\"%03u days, %02u:%02u\", d, h, m)}'"
        text2 = "UP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "uptime -p"
        text3 = "" + subprocess.check_output(cmd, shell=True).decode("utf-8")

    # вывод текста на дисплей
    draw.text((x, top + 0),  text0, font=font, fill=255)
    draw.text((x, top + 8),  text1, font=font, fill=255)
    draw.text((x, top + 16), text2, font=font, fill=255)
    draw.text((x, top + 25), text3, font=font, fill=255)
    
    # обработка нажатий кнопки OK
    if okBTN.value == 0:
        sleepIndex = 0 # при нажатии на кнопку начинаем отображение данных
        if scrollIndex == 4:
            cmd = "sudo shutdown -h now"
            subprocess.check_output(cmd, shell=True).decode("utf-8")
        elif scrollIndex == 5:
            cmd = "sudo shutdown -r now"
            subprocess.check_output(cmd, shell=True).decode("utf-8")

    # отображаем падающий пиксель, чтобы можно было понять состояние RPI (завис, нет)
    disp.image(image)
    i = i + 1
    if i > height:
    	i = 0
    disp.pixel(127, i, 1) # вывод падающего пикселя в конце дисплея
    disp.show()
    time.sleep(0.1)
