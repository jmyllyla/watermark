from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

def watermark(imageName, wmtext, fontName):
  image = Image.open(imageName)
  watermark_image = image.copy()
  draw = ImageDraw.Draw(watermark_image)
  w, h = image.size
  x, y = int(w / 2), int(h - min(w/30, h/30))
  if x > y:
    font_size = y
  elif y > x:
    font_size = x
  else:
    font_size = x
  font = ImageFont.truetype(fontName, int(font_size/15))

  # add watermark
  draw.text((x, y), wmtext, fill=(105,105,105), font=font, anchor='ms')
  watermark_image.save(imageName.replace(".", "_vl."))


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("No files given")
    exit(1)
  watermark(sys.argv[1], "Copyright Irina Rebnitskaya", sys.argv[2])
  
