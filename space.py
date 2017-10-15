import arcade
import random

from models import Rocket, World

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 620

MOVEMENT_SPEED = 5
 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
 
        self.rocketsp = arcade.Sprite('images/Rocket2.png')
        self.world = World(width, height)

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        self.rocketsp.set_position(self.world.rocket.x, 
                                 self.world.rocket.y)
        self.rocketsp.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.world.rocket.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.world.rocket.delta_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.world.rocket.delta_x = 0

 
def main():
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

main()