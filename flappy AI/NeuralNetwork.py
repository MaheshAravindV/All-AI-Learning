from Matrix import Matrix
import random
import math

def sigmoid(x):
    return 1/(1+math.exp(-x))

class NeuralNetwork:
    def __init__(self,a):
        self.layers = a
        self.layerCount = len(self.layers)
        self.inputs = Matrix(a[0],1)
        self.outputs = Matrix(a[-1],1)
        self.weights = []
        for i in range(self.layerCount-1):
            curr_weights = Matrix(a[i+1],a[i])
            curr_weights.random()
            self.weights.append(curr_weights)
        self.net = []
        for i in range(self.layerCount):
            self.net.append(Matrix(a[i],1))
        self.errors = []
        for i in range(self.layerCount):
            self.errors.append(Matrix(a[i],1))
        self.biases = []
        for i in range(self.layerCount):
            curr_bias = Matrix(a[i],1)
            curr_bias.random()
            self.biases.append(curr_bias)
            
        self.learningRate = 1000

    def feedForward(self,input):
        self.inputs.setArray(input)
        self.net[0] = self.inputs
        for i in range(1,self.layerCount):
            self.net[i] = Matrix.multiply(self.weights[i-1],self.net[i-1])
            self.net[i] = Matrix.map(self.net[i],sigmoid)
        self.outputs = self.net[-1]
        return self.outputs

    def train(self,input,output):
        self.feedForward(input)
        expected_output = Matrix(self.layers[-1],1)
        expected_output.setArray(output)
        self.errors[-1] = Matrix.add(expected_output,Matrix.map(self.outputs,lambda x : -x))
        for i in range(self.layerCount-2,0,-1):
            self.errors[i] = Matrix.multiply(self.weights[i].transpose(),self.errors[i+1])
        for i in range(self.layerCount-1):
            gradient = Matrix.map(self.net[i+1],lambda x : x*(1-x))
            gradient.multiplyElementWise(self.errors[i+1])
            gradient.mulScalar(self.learningRate)
            self.biases[i+1] = Matrix.add(self.biases[i+1],gradient)
            del_weight = Matrix.multiply(gradient,self.net[i].transpose())
            self.weights[i] = Matrix.add(self.weights[i],del_weight)
        return self.net[-1]

    def saveModel(self,name):
        f = open((name+'.txt'),'w')
        for i in self.weights:
            f.write(str(i.data))
            f.write('\n')
        for i in self.biases:
            f.write(str(i.data))
            f.write('\n')
        f.close()

    # def loadFromSave(self,file):
    #     f = open(file,'r')
    #     for i in range(len(self.weights)):

    def debugNet(self):
        for i in range(self.layerCount):
            self.net[i].display()

