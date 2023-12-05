#=========================================================
#             DISPLAY VARIOUS SHAPES ON TFT
#             =============================
#
# Author: Dogan Ibrahim
# File  : TFTshapes.py
# Date  : January, 2023
#=========================================================
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7735

msg = "RASPBERRY PI ZERO 2 W"
disp = ST7735.ST7735(port=0,cs=0,rst=27,dc=17,width=128,height=160,
rotation=90,invert=False,offset_left=0,offset_top=0)
disp.begin()

width = disp.width
height =disp.height
img=Image.new('RGB', (160,128),color=(0,0,0))
draw=ImageDraw.Draw(img)
font=ImageFont.load_default()

draw.rectangle((5, 5, 150, 120), outline = (0, 255, 0))
draw.ellipse((20, 20, 100, 80), outline = (0, 0, 255))
draw.line((10, 100, 60, 100), fill = (0, 255, 0))
draw.polygon([(100, 80), (100, 110), (130, 90), (145, 80)], outline = (0, 255, 255),
fill = (0, 255, 0))
draw.text((7,7),msg, font=font,fill=(0,255,0))
disp.display(img)


