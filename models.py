import random
import arcade
bullet_speed = 5

class Bullet:
    def __init__(self, world):
        self.x = 0
        self.y = 0
        self.world = world

    def update(self):
        self.y += bullet_speed

class Alien:
    def __init__(self):
        self.y = 620
        self.x = random.randrange(480)
        self.speed = random.randrange(2,4)

    def update(self):
        self.y -= self.speed
        self.n = random.randint(2,100)
        if self.y < 0:
            self.__init__()

class Rocket:
    def __init__(self, world, x, y):
        self.x = x
        self.y = y

        self.delta_x = 0

    def move(self):
        # Move left/right
        self.x += self.delta_x

        if(self.x < 0 or self.x > 480):
            self.delta_x = 0

class World:
    SCREEN_HEIGHT = 620

    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.rocket = Rocket(self, width / 2, 60)
        self.alien_list = []
        self.bullet_list = arcade.SpriteList()
        self.ispress = False
        self.bullet_model = []
        for alien in range(4):
            self.alien_list.append(Alien())
 
    def add_bullet(self):
        bullet = Bullet()
        self.bullet.append(bullet)
        return bullet

    def update(self, delta):
        self.rocket.move()
        for alien in self.alien_list:
            alien.update()

        for bulletsp in self.bullet_list:
            bulletsp.model.update()
            if bulletsp.center_y > World.SCREEN_HEIGHT:
                self.bullet_model.remove(bulletsp.model)
                bulletsp.kill()
        