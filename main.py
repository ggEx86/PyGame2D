import pygame

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
char = pygame.image.load('Resources/standing.png')
clock = pygame.time.Clock()
shoot_right = pygame.image.load('Resources/shoot_right.png')
shoot_left = pygame.image.load('Resources/shoot_left.png')
bulletL = pygame.image.load('Resources/bullet_l.png')
bulletR = pygame.image.load('Resources/bullet_r.png')


class Game:
    def __init__(self):
        pygame.init()
        self.keys = pygame.key.get_pressed()
        self.run = True
        self.win = pygame.display.set_mode((500, 480))
        pygame.display.set_caption("Game")

    def gameLoop(self, _player):
        self.run = True
        while self.run:
            clock.tick(27)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.keys = pygame.key.get_pressed()
            _player.player_movement(self)

            self.redrawGameWindow(_player)

    def redrawGameWindow(self, _player):
        self.win.blit(bg, (0, 0))
        _player.draw(self.win)

        pygame.display.update()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hold_gun = False

    def draw(self, win):                    #DRAW PLAYER ANIMATIONS
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            if _game.keys[pygame.K_LCTRL]:
                self.gun_animation(win, _game)
                self.hold_gun = True
            else:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hold_gun = False
        elif self.right:
            if _game.keys[pygame.K_LCTRL]:
                self.hold_gun = True
                self.gun_animation(win, _game)
            else:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hold_gun = False
        else:
            win.blit(char, (self.x, self.y))

    def player_movement(self, _game):
        if _game.keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
        elif _game.keys[pygame.K_RIGHT] and self.x < 500 - self.width - self.vel:
            self.x += self.vel
            self.right = True
            self.left = False
        else:
            self.right = False
            self.left = False
            self.walkCount = 0

        if not self.isJump:
            if _game.keys[pygame.K_SPACE]:
                self.isJump = True
                self.right = False
                self.left = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

    def gun_animation(self, win, _game):
        if self.right and not self.left:
            win.blit(shoot_right, (self.x, self.y))
        if self.left and not self.right:
            win.blit(shoot_left, (self.x, self.y))

    def shoot_bullet(self, win, _game):
        bllt = Bullet(self)
        bllt.bullet_movement(self)
        bllt.draw_bullet(win, self)



class Bullet(object):
    def __init__(self, _player):
        self.bullet_x = _player.x
        self.bullet_y = _player.y
        self.bullet_vel = 7
        self.exists = True
        self.s_right = True if _player.right else False
        self.s_left = True if _player.left else False

    def draw_bullet(self, win, _player):
        if _player.hold_gun:
            if self.s_right:
                win.blit(bulletR, (_player.x + 64, _player.y + 10))
            elif self.s_left:
                win.blit(bulletL, (_player.x, _player.y))

    def bullet_movement(self):
        while self.exists:
            if self.s_right:
                if self.bullet_x + 15 < _game.w_width:
                    self.bullet_x += self.bullet_vel
            elif self.s_left:
                if self.bullet_x - 15 > 0:
                    self.bullet_x -= self.bullet_vel


if __name__ == '__main__':
    _game = Game()
    _game.gameLoop(_player=Player(200, 410, 64, 64))

    pygame.quit()
