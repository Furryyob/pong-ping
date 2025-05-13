from pygame import *
win_width = 700
win_height = 500
back = (200, 255, 255)
window = display.set_mode((win_width, win_height))
window.fill(back)
background = transform.scale(image.load('fon.jpg'),(win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image =  transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


run = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('raketka.png', 20, 200, 40, 50, 10)
racket2 = Player('raketka.png', 600, 200, 40, 50, 10)
ball = GameSprite('pingpongball.png', 200, 200, 40, 50, 1)
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYERR 1 LOSE', True, (180, 0, 0))
font2 = font.Font(None, 35)
lose2 = font1.render('PLAYERR 2 LOSE', True, (180, 0, 0))
speed_x = 3
speed_y = 3


while run:
    for e in event.get():
        if e.type == QUIT:
           run = False

    
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
        ball.reset()

    if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
    if ball.rect.x > 600:
        finish = True
        window.blit(lose2, (200, 200))
    
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1

    display.update()
    clock.tick(FPS)