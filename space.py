import arcade
import random

from models import Rocket, World, Alien

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 620

MOVEMENT_SPEED = 5
 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.all_sprites_list = None
        self.alien_list = None
        self.score = 0
        self.rocketsp = None
        self.world = World(width, height)

    def start_new_game(self):

        arcade.set_background_color(arcade.color.BLACK)

        self.rocketsp = arcade.Sprite('images/Rocket2.png')
        self.aliensp = aecade.Sprite('images/Alien.png') 
        self.all_sprites_list = arcade.SpriteList()
        self.alien_list = arcade.SpriteList()
        self.score = 0
        
        for i in renge(50):
            aliensp.world.alien.center_x = random.randrange(SCREEN_WIDTH)
            aliensp.world.alien.center_y = SCREEN_HEIGHT
            self.all_sprites_list.append(aliensp)
            self.alien_list.append(aliensp)

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        self.rocketsp.set_position(self.world.rocket.x, self.world.rocket.y)
        self.rocketsp.draw()
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITH, 12)

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