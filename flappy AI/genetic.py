import random

popSize = 2000
mutationRate = 1
targetSize = 3*4 + 4 * 1 + 4 + 1

def fitness(organism):
    score = 0
    for i in range(targetSize):
        if organism[i] == target[i]:
            score += 1
    return score
    
def createPopulationFromScratch(popSize):
    population = []
    for i in range(popSize):
        population.append([])
        genes = []
        score = 0
        for j in range(targetSize):
            genes.append(random.random()*2-1)
        score = fitness(genes)
        population[i] = [genes,score**2]
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
            s[i] = chr(random.randint(63,122))
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
        child = [[],0]
        midPt = random.randint(0,targetSize)
        for i in range(midPt):
            child[0].append(parentA[0][i])
        
        for i in range(midPt,targetSize):
            child[0].append(parentB[0][i])
        child[0] = mutate(child[0],mutationRate)
        child[1] = fitness(child[0])**2
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