import random

target = 'pog'
popSize = 2000
mutationRate = 1
targetSize = len(target)

def createPopulationFromScratch(popSize):
    population = []
    for i in range(popSize):
        population.append([])
        s = ''
        score = 0
        for j in range(targetSize):
            s += chr(random.randint(65,123))
        for k in range(targetSize):
            if s[k] == target[k]:
                score += 1
        population[i] = [s,score**2]
    return population

def pickParent(curGen,maxFitness):
    a = random.randint(0,popSize-1)
    b = random.random()*maxFitness
    if b < curGen[a][1]:
        return curGen[a]
    else:
        return pickParent(curGen,maxFitness)

def mutate(s,rate):
    for i in range(len(s)):
        a = random.random()*100
        if a < rate:
            s = s[:i]+chr(random.randint(96,123))+s[i+1:]
    return s

def avgscore(population):
    totScore = 0
    for i in population:
        totScore += i[1]
    return ((totScore/popSize)/(targetSize**2))*100

def create(curGen):
    cm = 0
    for member in curGen:
        if member[1] > cm:
            cm = member[1]
            bestCandidate = member
    nextGen = []
    for i in range(popSize):
        parentA = pickParent(curGen,cm)
        parentB = pickParent(curGen,cm)
        while parentA == parentB:
            parentB = pickParent(curGen,cm)
        child = ['',0]
        midPt = random.randint(0,targetSize)
        for i in range(midPt):
            child[0] += parentA[0][i]
            if parentA[0][i] == target[i]:
                child[1] += 1
        for i in range(midPt,targetSize):
            child[0] += parentB[0][i]
            if parentB[0][i] == target[i]:
                child[1] += 1
        child[0] = mutate(child[0],mutationRate)
        child[1]*= child[1]
        nextGen += [child]
    return [nextGen,bestCandidate]

population = createPopulationFromScratch(popSize)

i = 0
while True:
    i += 1
    population,bestCandidate = create(population)
    if bestCandidate[1] == 0:
        population = createPopulationFromScratch(popSize)
    print(bestCandidate[0])
    print(avgscore(population),'%')
    if bestCandidate[1] == targetSize**2:
        print('tadaaaa!',i)
        print((bestCandidate[1]/targetSize**2)*100)
        break  