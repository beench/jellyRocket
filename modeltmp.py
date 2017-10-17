import random
import arcade

class Bullet():
    def __init__(self, rocket):
        self.bullet_speed = 5
        self.x = rocket.x
        self.y = rocket.y

    def update(self):
        self.y += self.bullet_speed

class Alien():
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
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.rocket = Rocket(self, width/2, 60)
        self.alien_list = []
        self.bullet_list = []
        self.n = random.randint(2,4)
        for alien in range(3):
            self.alien_list.append(Alien())
        for bullet in range(20): 
            self.bullet_list.append(Bullet(self.rocket))
 
    def update(self, delta):
        self.rocket.move()
        for alien in self.alien_list:
            alien.update()
        for bullet in self.bullet_list:
            bullet.update()