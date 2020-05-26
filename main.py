import pygame
from pygame.locals import *

pygame.init()
walkRight = [pygame.image.load('Resources/R1.png'),
             pygame.image.load('Resources/R2.png'),
             pygame.image.load('Resources/R3.png'),
             pygame.image.load('Resources/R4.png'),
             pygame.image.load('Resources/R5.png'),
             pygame.image.load('Resources/R6.png'),
             pygame.image.load('Resources/R7.png'),
             pygame.image.load('Resources/R8.png'),
             pygame.image.load('Resources/R9.png')]
walkLeft = [pygame.image.load('Resources/L1.png'),
            pygame.image.load('Resources/L2.png'),
            pygame.image.load('Resources/L3.png'),
            pygame.image.load('Resources/L4.png'),
            pygame.image.load('Resources/L5.png'),
            pygame.image.load('Resources/L6.png'),
            pygame.image.load('Resources/L7.png'),
            pygame.image.load('Resources/L8.png'),
            pygame.image.load('Resources/L9.png')]
bg = pygame.image.load('Resources/bg.jpg')
character = pygame.image.load('Resources/standing.png')
clock = pygame.time.Clock()
shoot_right = pygame.image.load('Resources/shoot_right.png')
shoot_left = pygame.image.load('Resources/shoot_left.png')


class Bullet(object):
    def __init__(self, b_x, b_y):
        self.b_x = b_x
        self.b_y = b_y
        self.b_im_r = pygame.image.load('Resources/bullet_r')
        self.b_im_l = pygame.image.load('Resources/bullet_l')

    def shoot_b(self, win):
        pass



class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            if keys[pygame.K_LCTRL]:
                self.shoot_animation(win)
            else:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        elif self.right:
            if keys[pygame.K_LCTRL]:
                self.shoot_animation(win)
            else:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            win.blit(character, (self.x, self.y))

    def shoot_animation(self, win):
        if self.right:
            win.blit(shoot_right, (self.x, self.y))
        if self.left:
            win.blit(shoot_left, (self.x, self.y))

    def player_movement(self):
        if keys[pygame.K_LEFT] and self.x - self.vel > 0:  # left
            self.x -= self.vel
            self.left = True
            self.right = False
        elif keys[pygame.K_RIGHT] and self.x + self.width + self.vel < w_width:  # right
            self.x += self.vel
            self.right = True
            self.left = False
        else:
            self.right = False
            self.left = False
            self.walkCount = 0

        if not self.isJump:
            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    char.draw(win)

    pygame.display.update()


if __name__ == '__main__':

    char = Player(300, 410, 64, 64)  # player object
    size = w_width, w_height = 640, 480
    win = pygame.display.set_mode(size)
    pygame.display.set_caption('Game')

    run = True
    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        char.player_movement()

        redrawGameWindow()
    pygame.quit()
