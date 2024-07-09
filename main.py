from pygame import*

class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y,player_width,player_height, player_speed):
        super().__init__()
        # each sprite must store an image property
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        # each sprite must store the rect property it is inscribed in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_S] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed


clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == Quit:
            game = False
    display.update()
    clock.tick(FPS)
