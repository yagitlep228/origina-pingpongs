from pygame import *
width = 900
height =700
window = display.set_mode((width, height))
display.set_caption("11st of september")
background = transform.scale(image.load('a19edd5907bfcda8f2ba376a574bf247.jpg'), (width, height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x ,player_y, player_speed,size_x , size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys =key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys =key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed


clock = time.Clock()
FPS = 60
run = True
NIggER = GameSprite('ball.png', 400,200,10,100,100)
player1 = Player('player1.png', 0,100,10,80,100)
player2 = Player('player2.png', 820,100,10,80,100)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0,0))
    NIggER.reset()
    player1.update_l()
    player2.update_r()
    player1.reset()
    player2.reset()
    
    display.update()