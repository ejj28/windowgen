import os

from PIL import Image, ImageDraw
counter = 7
counter2 = 22
counter3 = 7
width = int(raw_input("Enter the desired width\n"))
height = int(raw_input("Enter the desired height\n"))

files = [
  'assets/upperrightcorner.png',
  'assets/bottomrightcorner.png',
  'assets/upperleftcorner.png',
  'assets/bottomleftcorner.png',
  'assets/testbackground.png',
  'assets/topbar.png',
  'assets/bottomedge.png',
  'assets/leftedge.png',
  'assets/rightedge.png'
  ]
  
result = Image.new("RGB", (width, height))
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
dr = ImageDraw.Draw(result)
dr.rectangle([0,0,width,height],fill="blue")
#result.paste(img0, (0, 0))
result.paste(img1, (0, 0), img1)

for i in range(1,((width - 6) - 7) - 1):
    result.paste(img5, (counter, 0))
    
    counter += 1
for i in range (1,((height - 22) - 7)):
    result.paste(img8, (counter, counter2))
    result.paste(img7, (0, counter2))
    counter2 += 1
for i in range(1,((width - 6) - 7) - 1):
    
    result.paste(img6, (counter3, counter2))
    counter3 += 1
result.paste(img3, (counter, 0), img3)
result.paste(img4, (counter, counter2), img4)
result.paste(img2, (0, counter2), img2)

dr.rectangle([7,22,counter,counter2],fill="#dedede")
result.save('image.png')
