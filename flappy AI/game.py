import pygame,time,random

obstacles = []
i = 149
pygame.init()
SIZE = [WIDTH,HEIGHT] = [700,700]
screen = pygame.display.set_mode(SIZE)

PLAYER  = [60,HEIGHT//2]
vel = 0
counter = 0
dist = 0
def gameover(x):
    print(x)
    quit()

while True:
    dist += 1
    time.sleep(0.033)
    screen.fill([122,215,240])
    i += 1

    #Gravity
    PLAYER[1] += 3
    if counter > 0:
        PLAYER[1] -= 9
        counter += 1
        if counter == 10:
            counter = 0
    #User input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                counter = 1
                
    #Displaying player
    pygame.draw.rect(screen,[0,0,255],[PLAYER,[24,24]])
    
    #Displaying and updating the obstacles
    for obstacle in obstacles:
        obstacle[0][0] -= 3
        obstacle[1][0] -= 3
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(obstacle[0]))
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(obstacle[1]))
        if obstacle[0][0] < -100:
            obstacles = obstacles[1:]

    #Creating new obstacles
    if i == 150:
        h = random.randint(50,400)
        r1 = [WIDTH-20,0,50,h]
        r2 = [WIDTH-20,h+100,50,HEIGHT-100-h]
        obstacles.append([r1,r2])
        i = 0
    pygame.display.flip()   

    #Checking for collisions
    if PLAYER[1] + 24 > HEIGHT:
        gameover(dist//10)
    for obstacle in obstacles:
        if PLAYER[0] + 24 > obstacle[0][0] and PLAYER[0] < obstacle[0][0] + 50 and (PLAYER[1] < obstacle[0][1] + obstacle[0][3] or PLAYER[1] + 24  > obstacle[1][1]):
            gameover(dist/10)