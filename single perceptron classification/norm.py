import random
f = open("weight-height.csv",'r')
fr = open('results.txt','w')
wm,wM = 0,0
hm,hM = 0,0
for line in f:
    l = line.split(',')
    w,h = map(float,l[1:])
    if w < wm or wm == 0:
        wm = w
    if w > wM or wM == 0:
        wM = w
    if h > hM or hM == 0:
        hM = h
    if h < hm or hm == 0:
        hm = h
f = open("weight-height.csv",'r')
print(hm,hM,wm,wM)

def normalize(w,h):
    return [(w-wm)/(wM-wm),(h-hm)/(hM-hm)]
for line in f:
    l = line.split(',')
    w,h = map(float,l[1:])
    r = []
    if l[0] == '"Female"':
        fr.write('0')
    else:
        fr.write('1')
    fr.write(' ')
    fr.write(str((w-wm)/(wM-wm)))
    fr.write(' ')
    fr.write(str((h-hm)/(hM-hm)))
    fr.write('\n')
fr.close()
    
    
    
    
    
    
