import arcade
I=False
J=False
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 620

MOVEMENT_SPEED = 5

class Rocket:
    def __init__(self, world, x, y):
        self.x = x
        self.y = y

        self.change_x = 0
        self.delta_y = 0

    def move(self):
        # Move left/right
        self.x += self.change_x

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.rocket = Rocket(self, 100, 100)
 
    def update(self, delta):
        global I,J,MOVEMENT_SPEED
        #self.rocket.update(delta)
        if(I):
            self.rocket.change_x = -MOVEMENT_SPEED
        elif(J):
            self.rocket.change_x = MOVEMENT_SPEED
        else:
            self.rocket.change_x = 0

        self.rocket.move()

 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
 
        self.rocket = arcade.Sprite('images/Rocket2.png')
        self.world = World(width, height)

       # self.direction = MOVEMENT_SPEED
 
    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        self.rocket.set_position(self.world.rocket.x, 
                                 self.world.rocket.y)
        self.rocket.draw()

    def on_key_press(self, key, modifiers):
        global I,J
        if key == arcade.key.LEFT:
            I=True
            J=False
            #self.rocket.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            I=False
            J=True
            self.rocket.delta_x = MOVEMENT_SPEED
 
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

    main()