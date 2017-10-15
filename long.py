import arcade

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 620

MOVEMENT_SPEED = 5

class Rocket:
    def __init__(self, world, x, y):
        self.x = x
        self.y = y

        self.delta_x = 0

    def move(self):
        # Move left/right
        self.x += self.delta_x
 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.width = width
        self.height = height
        arcade.set_background_color(arcade.color.BLACK)
 
        self.rocketsp = arcade.Sprite('images/Rocket2.png')
        self.rocket = Rocket(self, width/2, 60)

 
    def update(self, delta):
        self.rocket.move()

    def on_draw(self):
        arcade.start_render()
        self.rocketsp.set_position(self.rocket.x, self.rocket.y)
        self.rocketsp.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.rocket.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.rocket.delta_x = MOVEMENT_SPEED
        else:
            self.rocket.delta_x = 0
 
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

    main()