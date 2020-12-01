import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 30)

pygame.display.set_caption("Scarlet the Flappy Cardinal")
icon = pygame.image.load('bird.png')
background = pygame.image.load("crimson.png")
pygame.display.set_icon(icon)
playerX = 0
playerY = 500
x_change = 0
y_change = 0
score = [3]
game_over = False
listy = []
rounds = []

xlist = [i for i in range(800)]
enemyXList = xlist[170:650:100]
enemyXListTop = xlist[220:700:100]
enemyYList = [random.randint(300, 500) for i in range(5)]
enemyYListTop = [random.randint(0, 200) for i in range(5)]
g = []
p = []

def endgame():
    go = ("Game Over")
    scorecard = ("Score: "+str(sum(score)))
    rendering = myfont.render(f"{go}", True, (255, 255, 255))
    rendering2 = myfont.render(f"{scorecard}", True, (255, 255, 255))
    screen.fill((184, 15, 10))
    screen.blit(rendering, (400,300))
    screen.blit(rendering2, (400,200))

def mains(xe, xet, ye, yet, screen):
    player(playerX, playerY, 70, 70)
    for m, n in zip(xe, ye):
        listy.append((m, n))
    for i in range(5):
        x = xe[i]
        y = ye[i]
        a = xet[i]
        b = yet[i]
        enemy(x, y, a, b)
        lines = pygame.draw.lines(screen, (0, 0, 0), points = [(x+35, 600), (x+35, y+50)], closed = True, width = 3)
        lines2 = pygame.draw.lines(screen, (0, 0, 0), points = [(a+35, 0), (a+35, b+35)], closed = True, width = 3)
        collided(playerX, playerY, x, y)

def player(x, y, o, z):
    playerImage = pygame.image.load("bird.png")
    playerImage = pygame.transform.scale(playerImage, (o, z))
    screen.blit(playerImage, (x, y))
    player_rect = playerImage.get_rect(topleft = (x, y))
    
def enemy(x, y, a, b):
    rose = pygame.image.load('rose.png')
    holly = pygame.image.load('holly.png')
    playerImage = pygame.transform.scale(rose, (70, 70))
    screen.blit(playerImage, (x, y))
    rose_rect = rose.get_rect(topleft = (x, y))
    playerImage2 = pygame.transform.scale(holly, (70, 70))
    screen.blit(playerImage2, (a, b))
    holly_rect = holly.get_rect(topleft = (x, y))

def collided(playerx, playery, enemyx, enemyy):
    distance = math.sqrt(math.pow(playerx-enemyx, 2)+math.pow(playery-enemyy, 2))
    if distance<27:
        return True
    else:
        return False
def delete():
    screen2 = pygame.display.set_mode((800,600))
    screen2.fill((184, 15, 10))
  

running = True
while running:
    screen.fill((184, 15, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()
          pygame.display.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change= 0
            elif event.key == pygame.K_RIGHT:
                x_change = 3
            elif event.key == pygame.K_SPACE:
                y_change= -5
            elif event.key == pygame.K_c:
                player(playerX, playerY, 70, 70)
        if event.type == pygame.KEYUP:
            x_change = 0
            y_change = 5

    playerX+=x_change
    playerY+=y_change
    if playerX<=0 or playerX>730:
        x_change = 0
    if playerY<=0 or playerY>500:
        y_change = 0
##    if playerX>=800:
##        player(0, 500, 70, 70)
##        for o in range(len(enemyXListTop)):
##            g.append(random.randint(300, 500))
##            p.append(random.randint(0, 200))
##        mains(enemyXList, enemyXListTop, g, p, screen)
    mains(enemyXList, enemyXListTop, enemyYList, enemyYListTop, screen)
    for i in range(len(enemyXListTop)):
        if collided(playerX, playerY, enemyXList[i], enemyYList[i]) == True or collided(playerX, playerY, enemyXListTop[i], enemyYListTop[i]) == True:
            playerX = 0
            playerY = 0
            score.append(-1)
##        if playerX==750:
##            rendering = myfont.render(f"You won!", True, (255, 255, 255))
##            screen.blit(rendering, (400, 300))
    scorecard = ("Tries Left: "+str(sum(score)))
    rendering = myfont.render(f"{scorecard}", True, (255, 255, 255))
    screen.blit(rendering, (10, 50))
    rendering3 = myfont.render(f"Round: {str(sum(rounds))}", True, (255, 255, 255))
    screen.blit(rendering3, (10, 100))
    if playerX>700:
        rounds.append(1)
        rendering4 = myfont.render(f"Round: {1}", True, (255, 255, 255))
        screen.blit(rendering4, (400, 300))
        playerX=0
        playerY = 0
        enemyYList = [random.randint(300, 500) for i in range(5)]
        enemyYListTop = [random.randint(0, 200) for i in range(5)]
    if sum(score) <= 0:
        rendering = myfont.render(f"Game Over", True, (255, 255, 255))
        screen.blit(rendering, (400, 300))
        x_change = 0
        y_change = 0
    pygame.display.update()
    


