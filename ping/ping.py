from pygame import *
win_width = 700
win_height = 500
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

racket1 = Player('raketka.png', 30, 200, 4, 50, 150)
racket2 = Player('raketka.png', 30, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

while run:
    for e in event.get():
        if e.type == QUIT:
           run = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset

    display.update()