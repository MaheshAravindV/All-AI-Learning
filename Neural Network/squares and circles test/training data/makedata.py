from PIL import ImageDraw,Image
import os
import random
for i in range(1000):
    im = Image.new('RGB',(32,32))
    x,y = random.randint(5,18),random.randint(5,18)
    r = random.randint(10,min(28-x,28-y))
    ImageDraw.Draw(im).ellipse((x,y,x+r,y+r),outline="#ffffff")
    im.save(os.getcwd()+'\\training data\\circles\\'+str(i)+'.jpg')
    im = Image.new('RGB',(32,32))
    x,y = random.randint(5,23),random.randint(5,23)
    r = random.randint(5,min(28-x,28-y))
    ImageDraw.Draw(im).rectangle((x,y,x+r,y+r),outline="#ffffff")
    im.save(os.getcwd()+'\\training data\\squares\\'+str(i)+'.jpg')

