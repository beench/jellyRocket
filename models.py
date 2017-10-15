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
 
    def update(self, delta):
        self.rocket.move()