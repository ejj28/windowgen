import os

from PIL import Image

files = [
  '/Users/Erik/localCoding/windowgen/assets/upperrightcorner.png',
  '/Users/Erik/localCoding/windowgen/assets/bottomrightcorner.png',
  '/Users/Erik/localCoding/windowgen/assets/upperleftcorner.png',
  '/Users/Erik/localCoding/windowgen/assets/bottomleftcorner.png'
  ]
  
result = Image.new("RGB", (50, 50))
img1 = Image.open(files[2])
img2 = Image.open(files[3])
img3 = Image.open(files[0])
img4 = Image.open(files[1])

w1, h1 = img1.size
w2, h2 = img2.size
w3, h3 = img3.size
w4, h4 = img4.size
result.paste(img1, (0, 0))
result.paste(img2, (0, h1 + 1))
result.paste(img3, (w1 + 1, 0))
result.paste(img4, (w1 + 1, h1 + 1))

result.save('/Users/Erik/localCoding/windowgen/image.jpg', dither=Image.NONE)
