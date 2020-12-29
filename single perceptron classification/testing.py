import random,math,norm
for test in range(10):
    w1,w2 = random.random(),random.random()
    f = open('results.txt','r')
    i = 0
    c = 0
    for l in f:
        i += 1
        line = l.split()
        w,h = map(float,line[1:])
        op = math.floor(w1*w + w2*h)
        if i < 9900:
            w1 += 0.005*(int(line[0])-op)
            w2 += 0.005*(int(line[0])-op)
        else:
            if int(line[0]) != op:
                c += 1
    print(100-(c/(i-1000)))
def guess(w,h):
    w,h = norm.normalize(w,h)
    op = math.floor(w1*w + w2*h)
    if op == 0:
        return 'Female'
    else:
        return 'Male'


    
    
    
