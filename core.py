import os

from PIL import Image, ImageDraw
counter = 7
counter2 = 22
counter3 = 7
files = [
  '/Users/Erik/localCoding/windowgen/assets/upperrightcorner.png',
  '/Users/Erik/localCoding/windowgen/assets/bottomrightcorner.png',
  '/Users/Erik/localCoding/windowgen/assets/upperleftcorner.png',
  '/Users/Erik/localCoding/windowgen/assets/bottomleftcorner.png',
  '/Users/Erik/localCoding/windowgen/assets/testbackground.png',
  '/Users/Erik/localCoding/windowgen/assets/topbar.png',
  '/Users/Erik/localCoding/windowgen/assets/bottomedge.png',
  '/Users/Erik/localCoding/windowgen/assets/leftedge.png',
  '/Users/Erik/localCoding/windowgen/assets/rightedge.png'
  ]
  
result = Image.new("RGB", (50, 50))
img0 = Image.open(files[4])
img1 = Image.open(files[2])
img2 = Image.open(files[3])
img3 = Image.open(files[0])
img4 = Image.open(files[1])
img5 = Image.open(files[5])
img6 = Image.open(files[6])
img7 = Image.open(files[7])
img8 = Image.open(files[8])

w1, h1 = img1.size
w2, h2 = img2.size
w3, h3 = img3.size
w4, h4 = img4.size
result.paste(img0, (0, 0))
result.paste(img1, (0, 0), img1)

for i in range(1,35):
    result.paste(img5, (counter, 0))
    
    counter += 1
for i in range (1,15):
    result.paste(img8, (counter, counter2))
    result.paste(img7, (0, counter2))
    counter2 += 1
for i in range(1,35):
    
    result.paste(img6, (counter3, counter2))
    counter3 += 1
result.paste(img3, (counter, 0), img3)
result.paste(img4, (counter, counter2), img4)
result.paste(img2, (0, counter2), img2)
dr = ImageDraw.Draw(result)
dr.rectangle([7,22,counter,counter2],fill="#dedede")
result.save('/Users/Erik/localCoding/windowgen/image.jpg', dither=Image.NONE)
