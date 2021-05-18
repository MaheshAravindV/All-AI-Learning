import pygame,time,random
from NeuralNetwork import NeuralNetwork
obstacles = []
i = 149
pygame.init()
SIZE = [WIDTH,HEIGHT] = [700,700]
screen = pygame.display.set_mode(SIZE)
dist = 0
popSize = 200
mutationRate = 0.1
targetSize = 2*4 + 4 * 1 + 4 + 1


f = open('results.txt','w')
f.close()
genCount = 1
class creature:
    def __init__(self):
        self.genes = []
        self.score = 0
        self.coords = [60,HEIGHT//2]
        for j in range(targetSize):
            self.genes.append(random.random()*2-1)
        self.counter = 0
        self.state = 1 #Alive
        self.brain = NeuralNetwork([2,4,1])
        counter = 0
        for weight in self.brain.weights:
            for i in range(weight.rows):
                for j in range(weight.cols):
                    weight.data[i][j] = self.genes[counter]
                    counter += 1
        for bias in self.brain.biases[1:]:
            for i in range(bias.rows):
                bias.data[i][0] = self.genes[counter]
                counter += 1
        counter = 0
        
    def reset(self):
        self.score = 0
        self.coords = [60,HEIGHT//2]
        self.counter = 0
        self.state = 1

    def copy(self,parent):
        self.genes = parent.genes.copy()
        counter = 0
        for weight in self.brain.weights:
            for i in range(weight.rows):
                for j in range(weight.cols):
                    weight.data[i][j] = self.genes[counter]
                    counter += 1
        for bias in self.brain.biases[1:]:
            for i in range(bias.rows):
                bias.data[i][0] = self.genes[counter]
                counter += 1
        counter = 0
    
def createPopulationFromScratch(popSize):
    population = []
    for i in range(popSize):
        population.append(creature())
    return population

def pickParent(curGen,maxFitness):
    a = curGen[random.randint(0,popSize-1)]
    b = random.random()*maxFitness
    if a.score > b:
        c = creature()
        c.copy(a)
        return c
    else:
        return pickParent(curGen,maxFitness)

def mutate(c,rate):
    for i in range(len(c.genes)):
        a = random.random()*100
        if a < rate:
            c.genes[i] += random.random()*0.1-0.05

def evolve(curGen):
    f = open('results.txt','a+')
    global genCount
    nextGen = []
    maxScore = 1
    totScore = 0

    for c in curGen:
        totScore += c.score
        if c.score > maxScore:
            maxScore = c.score
            if maxScore > bestever.score:
                bestever.copy(c)
    genCount += 1
    maxScore /= totScore
    for i in curGen:
        i.score /= totScore
    for i in range(popSize):
        child = pickParent(curGen,maxScore)
        nextGen.append(child)
    return nextGen
    

bestever = creature()  
    
population = createPopulationFromScratch(popSize)
noOfDead = 0
while True:
    print(genCount)
    time.sleep(0.01)
    dist += 1
    if genCount%10 == 0:
        screen.fill([122,215,240])
    i += 1
    #Gravity
    if genCount%10 == 0:
        c = bestever
        if c.state == 1:
            c.coords[1] += 3
            if c.counter > 0:
                c.coords[1] -= 9
                c.counter += 1
                if c.counter == 10:
                    c.counter = 0
            #Displaying players
            pygame.draw.rect(screen,[0,0,255],[c.coords,[24,24]])    
            #Checking for collisions
            if c.coords[1] + 24 > HEIGHT or c.coords[1] < 0:
                c.score = dist
                c.state = 0
                noOfDead += 1
            for obstacle in obstacles:
                if c.coords[0] + 24 > obstacle[0][0] and c.coords[0] < obstacle[0][0] + 50 and (c.coords[1] < obstacle[0][1] + obstacle[0][3] or c.coords[1] + 24  > obstacle[1][1]):
                    c.score = dist
                    c.state = 0
                    noOfDead += 1
            
            #Controlling using AI
            inputs = [0,0]
            for obstacle in obstacles:
                if c.coords[0] < obstacle[0][0]:
                    inputs[0] = (obstacle[0][0]-c.coords[0])/WIDTH
                    inputs[1] = (obstacle[0][1]-c.coords[1])/HEIGHT
                    break
            if c.brain.feedForward(inputs) == 1:
                c.counter = 1
    for c in population:
        if c.state == 1:
            c.coords[1] += 3
            if c.counter > 0:
                c.coords[1] -= 9
                c.counter += 1
                if c.counter == 10:
                    c.counter = 0
            #Displaying players
            pygame.draw.rect(screen,[0,0,255],[c.coords,[24,24]])    
            #Checking for collisions
            if c.coords[1] + 24 > HEIGHT or c.coords[1] < 0:
                c.score = dist
                c.state = 0
                noOfDead += 1
            for obstacle in obstacles:
                if c.coords[0] + 24 > obstacle[0][0] and c.coords[0] < obstacle[0][0] + 50 and (c.coords[1] < obstacle[0][1] + obstacle[0][3] or c.coords[1] + 24  > obstacle[1][1]):
                    c.score = dist
                    c.state = 0
                    noOfDead += 1
            
            #Controlling using AI
            inputs = [0,0]
            for obstacle in obstacles:
                if c.coords[0] < obstacle[0][0]:
                    inputs[0] = (obstacle[0][0]-c.coords[0])/WIDTH
                    inputs[1] = (obstacle[0][1]-c.coords[1])/HEIGHT
                    break
            if c.brain.feedForward(inputs) == 1:
                c.counter = 1
    
    
    #Displaying and updating the obstacles
    for obstacle in obstacles:
        obstacle[0][0] -= 3
        obstacle[1][0] -= 3
        if genCount%10 == 0:
            pygame.draw.rect(screen,(0,255,0),pygame.Rect(obstacle[0]))
            pygame.draw.rect(screen,(0,255,0),pygame.Rect(obstacle[1]))
        if obstacle[0][0] < -100:
            obstacles = obstacles[1:]

    #Creating new obstacles
    if i == 150:
        h = 200
        r1 = [WIDTH-20,0,50,h]
        r2 = [WIDTH-20,h+100,50,HEIGHT-100-h]
        obstacles.append([r1,r2])
        i = 0
    if noOfDead == popSize:
        population = evolve(population)
        obstacles = []
        noOfDead = 0
        i = 149
        dist = 0
    
    
   
    pygame.display.flip()   
