#=========================================================
#             DISPLAY TEXT ON TFT
#             ===================
#
# Author: Dogan Ibrahim
# File  : TFTexample.py
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

draw.text((5,60),msg, font=font)
disp.display(img)


