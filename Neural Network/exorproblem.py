from NeuralNetwork import NeuralNetwork
from Matrix import Matrix
import random

brain = NeuralNetwork([2,2,1])
train_data = [[[0,0],[0]],[[0,1],[1]],[[1,0],[1]],[[1,1],[0]]]


for j in range(100000):
    tcase = train_data[random.randint(0,3)]
    ip = tcase[0]
    op = tcase[1]
    brain.train(ip,op)
for i in train_data:
    brain.feedForward(i[0]).display()