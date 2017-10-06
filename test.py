import arcade

# Set up the constants
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 620

MOVEMENT_SPEED = 5

class GameSpace(arcade.Window):
    """
    Main space class.
    """
    def __init__(self, width, height):
        super().__init__(width, height, title="Keyboard control")
        self.left_down = False
        arcade.set_background_color(arcade.color.BLACK)
 
        self.rocket = arcade.Sprite('images/Rocket2.png')
       # self.left_down = False
        self.rocket.set_position(100, 100)

    def update(self, dt):
        """ Move everything """
        self.rocket.move()

    def on_draw(self):
        arcade.start_render()
        self.rocket.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.LEFT:
            self.rocket.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.rocket.delta_x = MOVEMENT_SPEED

def main():
    window = GameSpace(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
    main()