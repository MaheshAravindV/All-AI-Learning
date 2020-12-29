from NeuralNetwork import NeuralNetwork
from Matrix import Matrix
import random
from PIL import Image
import numpy
import os

brain = NeuralNetwork([1024,1024,1])

for i in range(100000):
    sqorc = random.randint(0,1)
    index = random.randint(0,999)
    if sqorc == 1:
        im = Image.open(os.getcwd()+'\\training data\\circles\\'+str(index)+'.jpg')
        op = [1]
    else:
        im = Image.open(os.getcwd()+'\\training data\\squares\\'+str(index)+'.jpg')
        op = [2]
    imgarr = numpy.array(im)
    input = []
    for i in imgarr:
        for j in i:
            if j[0] > 0:
                input.append(1)
            else:
                input.append(0)
    print('output')
    print(op)
    brain.train(input,op).display()
    print('error')
    brain.errors[-1].display()