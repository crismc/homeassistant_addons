# Copyright (c) 2017 Adafruit Industries
# Author: Tony DiCola & James DeVito
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import math
import time
import pathlib

import Adafruit_GPIO.SPI as SPI
import SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

RENDER_VIEW_SECONDS = 20

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
# disp = SSD1306.SSD1306_128_64(rst=RST)

# Note you can change the I2C address by passing an i2c_address parameter like:
# disp = SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Alternatively you can specify an explicit I2C bus number, for example
# with the 128x32 display you would use:
# disp = SSD1306.SSD1306_128_32(rst=RST, i2c_bus=2)

# 128x32 display with hardware SPI:
# disp = SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Alternatively you can specify a software SPI implementation by providing
# digital GPIO pin numbers for all the required display pins.  For example
# on a Raspberry Pi with the 128x32 display you might use:
# disp = SSD1306.SSD1306_128_32(rst=RST, dc=DC, sclk=18, din=25, cs=22)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

lineY = [
    top, top, top+8, top+16, top+25
]

lineY_large = [
    top, top, top+10, top+24, top+32
]

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
current_dir = pathlib.Path(__file__).parent.resolve()
font_large = ImageFont.truetype(str(current_dir) + '/fonts/vcr_osd_mono.ttf', 14)

def text(txt, line, is_large = False):
    if (is_large):
        pos = lineY_large[line]
        display_font = font_large
    else:
        pos = lineY[line]
        display_font = font

    draw.text((x, pos), txt,  font=display_font, fill=255)

def get_cmd(cmd):
    return subprocess.check_output(cmd, shell = True, encoding='utf-8').strip()

def reset_clock():
    return time.time() + RENDER_VIEW_SECONDS

def renderTimeBreak():
    return time.time() < timer

class Scroller:
    def __init__(self, text, offset = lineY[1], startpos = width, amplitude = 0, font = font, velocity = -2, draw_obj = draw, width = width):
        self.text = text
        self.draw = draw_obj
        self.amplitude = amplitude
        self.offset = offset
        self.velocity = velocity
        self.width = width
        self.startpos = startpos
        self.pos = startpos
        self.font = font
        self.maxwidth, unused = self.draw.textsize(self.text, font=self.font)

    def render(self):
        # Enumerate characters and draw them offset vertically based on a sine wave.
        x = self.pos
        
        for i, c in enumerate(self.text):
            # Stop drawing if off the right side of screen.
            if x > self.width:
                break

            # Calculate width but skip drawing if off the left side of screen.
            if x < -10:
                char_width, char_height = self.draw.textsize(c, font=self.font)
                x += char_width
                continue

            # Calculate offset from sine wave.
            y = self.offset + math.floor(self.amplitude * math.sin(x / float(self.width) * 2.0 * math.pi))

            # Draw text.
            self.draw.text((x, y), c, font=self.font, fill=255)

            # Increment x position based on chacacter width.
            char_width, char_height = self.draw.textsize(c, font=self.font)
            x += char_width

    def move_for_next_frame(self, allow_startover):
        self.pos += self.velocity
        # Start over if text has scrolled completely off left side of screen.
        if self.has_completed():
            if allow_startover:
                self.start_over()
                return True
            else:
                return False
        return True

    def start_over(self):
        self.pos = self.startpos

    def has_completed(self):
        return self.pos < -self.maxwidth


timer = reset_clock()
index = 0

def render_hostinfo():
    VERSION = get_cmd("cat /etc/os-release | grep PRETTY_NAME | awk -F= '/PRETTY/ {print $2}'").strip("\"")
    scroller = Scroller(VERSION, lineY[4], 0)
    while renderTimeBreak():
        HOST = get_cmd("hostname | cut -d\' \' -f1")
        IP = get_cmd("hostname -I | cut -d\' \' -f1")
        
        # Clear image buffer by drawing a black filled box.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        # Write two lines of text.
        text("HOST: " + str(HOST), 1)
        text("IP: " + str(IP), 2, font_large)
        scroller.render()

        # Display image.
        disp.image(image)
        disp.display()

        if not scroller.move_for_next_frame(renderTimeBreak()):
            break

        time.sleep(0.001)

def render_stats():
    while renderTimeBreak():
        # IP = get_cmd("hostname -I | cut -d\' \' -f1")
        CPU = get_cmd("top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'")
        MemUsage = get_cmd("free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'")
        Disk = get_cmd("df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'")

        # Clear image buffer by drawing a black filled box.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        # Write two lines of text.
        # text("IP: " + str(IP), 1)
        text(CPU, 2)
        text(MemUsage, 3)
        text(Disk, 4)

        # Display image.
        disp.image(image)
        disp.display()

        time.sleep(0.1)

def render_scroller():
    hostname = get_cmd("hostname | cut -d\' \' -f1")
    scroller = Scroller('Welcome to ' + hostname, height/2 - 4, width, height/4, font_large)

    while True:
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        scroller.render()
        disp.image(image)
        disp.display()

        if not scroller.move_for_next_frame(renderTimeBreak()):
            break

        time.sleep(0.001)

render_funcs = [
    "render_scroller",
    "render_hostinfo",
    "render_stats"
]

while True:
    render_func = render_funcs[index]
    func_to_run = globals()[render_func]

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    func_to_run()

    if (index < (len(render_funcs) - 1)):
        index = index + 1
    else:
        index = 0

    timer = reset_clock()

    time.sleep(.1)
