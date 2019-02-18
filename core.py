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
  'assets/rightedge.png',
  'assets/exitbutton.png',
  'assets/minimizebutton.png',
  'assets/smallerbutton.png'
  ]
  
result = Image.new("RGB", (width, height))
bg = Image.open(files[4])
ulc = Image.open(files[2])
blc = Image.open(files[3])
urc = Image.open(files[0])
brc = Image.open(files[1])
te = Image.open(files[5])
be = Image.open(files[6])
le = Image.open(files[7])
re = Image.open(files[8])
eb = Image.open(files[9])
mb = Image.open(files[10])
sb = Image.open(files[11])

w1, h1 = ulc.size
w2, h2 = blc.size
w3, h3 = urc.size
w4, h4 = brc.size
dr = ImageDraw.Draw(result)
dr.rectangle([0,0,width,height],fill="blue")
#result.paste(bg, (0, 0))
result.paste(ulc, (0, 0), ulc)

for i in range(1,((width - 6) - 7) - 1):
    result.paste(te, (counter, 0))
    
    counter += 1
for i in range (1,((height - 22) - 7)):
    result.paste(re, (counter, counter2))
    result.paste(le, (0, counter2))
    counter2 += 1
for i in range(1,((width - 6) - 7) - 1):
    
    result.paste(be, (counter3, counter2))
    counter3 += 1
result.paste(urc, (counter, 0), urc)
result.paste(brc, (counter, counter2), brc)
result.paste(blc, (0, counter2), blc)
result.paste(eb, (4, 5))
result.paste(mb, (width - 18, 5))
result.paste(sb, (width - 34, 5))
dr.rectangle([7,22,counter,counter2],fill="#dedede")
result.save('output/image.png')
