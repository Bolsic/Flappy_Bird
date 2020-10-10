import pygame
import math
import random
pygame.init()

win = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("Flappy Bird")

def collision_bird_stub (bird, stub):
    if bird.x + bird.r < stub.x:
        return False
    if bird.x - bird.r > stub.x + stub.width:
        return False
    if bird.y - bird.r > stub.y_hole - (stub.hole_size // 2):
        if bird.y + bird.r < stub.y_hole + (stub.hole_size // 2):
            return False
    if bird.x > stub.x and bird.x < stub.x + stub.width:
        if bird.y - bird.r > stub.y_hole - stub.hole_size // 2:
            if bird.y + bird.r < stub.y_hole + stub.hole_size // 2:
                return False
    return True

class Player(object):
    def __init__(self, vely, x, y, r):
        self.vely = vely
        self.y = y
        self.x = x
        self.isJump = False
        self.r = r
    def reset(self):
        self.y = 300
    def move(self):
        self.y += self.vely

class Stub(object):
    def __init__(self, x0, x, velx, width, hole_size, y_hole):
        self.velx = velx
        self.x = x
        self.vel = velx
        self.width = width
        self.hole_size = hole_size
        self.y_hole = y_hole
        self.x0 = x0
    def reset(self):
        self.x = self.x0
        self.y_hole = random.randint(self.hole_size * 0.7, 600 - self.hole_size * 0.7)
    def move(self):
        self.x += self.velx



ubrzanje = 1
delay_counter = 0
brojac = 1
length = 110
k = 4

Bird = Player(0, 300, 300, 22)
Stub1 = Stub(1000 ,1000, 5, 100, 150, 300)
Stub2 = Stub(1500, 1500, 5, 100, 150, 300)
velx0 = Stub1.velx
Stub1.y_hole = random.randint(Stub1.hole_size * 0.7, 600 - Stub1.hole_size * 0.7)
Stub2.y_hole = random.randint(Stub2.hole_size * 0.7, 600 - Stub2.hole_size * 0.7)

Ptica = [pygame.image.load('sprites/bird_gore.png'), pygame.image.load('sprites/bird_sredina_gore.png'), pygame.image.load('sprites/bird_sredina.png'), pygame.image.load('sprites/bird_sredina_dole.png'), pygame.image.load('sprites/bird_dole.png ')]
Ptica[0] = pygame.transform.scale(Ptica[0], (Bird.r * 2 + k, Bird.r * 2 + k))
Ptica[1] = pygame.transform.scale(Ptica[1], (Bird.r * 2 + k, Bird.r * 2 + k))
Ptica[2] = pygame.transform.scale(Ptica[2], (Bird.r * 2 + k, Bird.r * 2 + k))
Ptica[3] = pygame.transform.scale(Ptica[3], (Bird.r * 2 + k, Bird.r * 2 + k))
Ptica[4] = pygame.transform.scale(Ptica[4], (Bird.r * 2 + k, Bird.r * 2 + k))

Pipe = [pygame.image.load('sprites/pipe_gore.png'), pygame.image.load('sprites/pipe_dole.png'), pygame.image.load('sprites/stub_sredina.png')]
Pipe[0] = pygame.transform.scale(Pipe[0], (Stub1.width, length))
Pipe[1] = pygame.transform.scale(Pipe[1], (Stub1.width, length))
Pipe[2] = pygame.transform.scale(Pipe[2], (Stub1.width, length))

#Backround = pygame.image.load('Backround7.png')
#         Backround = pygame.transform.scale(Backround, (1000, 600))

dead = False

run = True
while run:
    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE] and delay_counter < 0 and not dead:
        Bird.vely = -14
        delay_counter = 15
        brojac = 14

    if brojac > 0:
        brojac -= 1

    delay_counter -= 1

    if Bird.vely < 15:
        Bird.vely += ubrzanje

    if Stub1.x == 0 - Stub1.width:
        Stub1.x = 1000
        Stub1.y_hole = random.randint(Stub1.hole_size * 1.5, 600 - Stub1.hole_size * 1.5)

    if Stub2.x == 0 - Stub2.width:
        Stub2.x = 1000
        Stub2.y_hole = random.randint(Stub2.hole_size * 1.3, 600 - Stub2.hole_size * 1.3)

    Bird.move()
    Stub1.x -= Stub1.velx
    Stub2.x -= Stub2.velx

    if collision_bird_stub(Bird, Stub1):
        Stub1.velx = 0
        Stub2.velx = 0
        if not dead:
            pygame.draw.rect(win, (255, 255, 255), (0, 0, 2000, 2000))
            pygame.display.update()
            pygame.time.delay(15)
        dead = True

    if Bird.y + Bird.r >= 600:
        Bird.reset()
        Stub1.reset()
        Stub2.reset()
        Stub1.velx = velx0
        Stub2.velx = velx0
        dead = False
        pygame.time.delay(500)

    # win.blit(Backround, (0, 0))

    win.fill((0, 0, 0))

    # pygame.draw.rect(win, (200, 0, 0), (Stub1.x, 0, Stub1.width, (Stub1.y_hole - Stub1.hole_size // 2)))
    # pygame.draw.rect(win, (200, 0, 0), (Stub1.x, (Stub1.y_hole + Stub1.hole_size // 2), Stub1.width, 600))

    win.blit(Pipe[1], (Stub1.x, Stub1.y_hole - Stub1.hole_size // 2 - length))
    win.blit(Pipe[0], (Stub1.x, Stub1.y_hole + Stub1.hole_size // 2))

    win.blit(Pipe[2], (Stub1.x, Stub1.y_hole - Stub1.hole_size // 2 - length - 100))
    win.blit(Pipe[2], (Stub1.x, Stub1.y_hole - Stub1.hole_size // 2 - length - 200))
    win.blit(Pipe[2], (Stub1.x, Stub1.y_hole - Stub1.hole_size // 2 - length - 300))
    win.blit(Pipe[2], (Stub1.x, Stub1.y_hole - Stub1.hole_size // 2 - length - 400))

    win.blit(Pipe[2], (Stub1.x, Stub1.y_hole + Stub1.hole_size // 2 + 100))
    win.blit(Pipe[2], (Stub1.x, Stub1.y_hole + Stub1.hole_size // 2 + 200))
    win.blit(Pipe[2], (Stub1.x, Stub1.y_hole + Stub1.hole_size // 2 + 300))
    win.blit(Pipe[2], (Stub1.x, Stub1.y_hole + Stub1.hole_size // 2 + 400))

    #pygame.draw.rect(win, (200, 0, 0), (Stub2.x, 0, Stub2.width, (Stub2.y_hole - Stub2.hole_size // 2)))
    #pygame.draw.rect(win, (200, 0, 0), (Stub2.x, (Stub2.y_hole + Stub2.hole_size // 2), Stub2.width, 600))

    win.blit(Pipe[1], (Stub2.x, Stub2.y_hole - Stub2.hole_size // 2 - length))
    win.blit(Pipe[0], (Stub2.x, Stub2.y_hole + Stub2.hole_size // 2))

    win.blit(Pipe[2], (Stub2.x, Stub2.y_hole - Stub2.hole_size // 2 - length - 100))
    win.blit(Pipe[2], (Stub2.x, Stub2.y_hole - Stub2.hole_size // 2 - length - 200))
    win.blit(Pipe[2], (Stub2.x, Stub2.y_hole - Stub2.hole_size // 2 - length - 300))

    win.blit(Pipe[2], (Stub2.x, Stub2.y_hole + Stub2.hole_size // 2 + 100))
    win.blit(Pipe[2], (Stub2.x, Stub2.y_hole + Stub2.hole_size // 2 + 200))
    win.blit(Pipe[2], (Stub2.x, Stub2.y_hole + Stub2      .hole_size // 2 + 300))

    #pygame.draw.circle(win, (0, 0, 0), (300, Bird.y), Bird.r)
    win.blit(Ptica[brojac // 3], (Bird.x - Bird.r, Bird.y - Bird.r))

    pygame.display.update()
pygame.quit()