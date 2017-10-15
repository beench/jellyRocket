import arcade
import random

from models import Rocket, World, Alien

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 620

MOVEMENT_SPEED = 5

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.all_sprites_list = arcade.SpriteList()
        self.score = 0
        self.world = World(width, height)

        #self.rocketsp = arcade.Sprite('images/Rocket2.png')
        self.rocketsp = ModelSprite('images/Rocket2.png', model=self.world.rocket)
        
        #self.aliensp = arcade.Sprite('images/Alien.png') 
        self.aliensp = ModelSprite('images/Alien.png', model=self.world.alien)

        self.all_sprites_list.append(self.rocketsp)
        self.all_sprites_list.append(self.aliensp)
        #self.alien_list = arcade.SpriteList()
        #self.alien_list.append(self.aliensp)
        self.score = 0

    def start_new_game(self):        
        for i in range(50):
            aliensp = self.world.alien
            #self.aliensp.set_position(self.world.alien.x, self.world.alien.y) 
            aliensp.x = random.randrange(SCREEN_WIDTH)
            aliensp.y = SCREEN_HEIGHT

    def update(self, delta):
        self.world.update(delta)
        #self.rocketsp.set_position(self.world.rocket.x, self.world.rocket.y)

    def on_draw(self):
        arcade.start_render()

        #self.all_sprites_list.draw()

        self.rocketsp.draw()
        self.aliensp.draw()        
        #self.rocketsp.set_position(self.world.rocket.x, self.world.rocket.y)

        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 600, arcade.color.WHITE, 12)

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
    window.start_new_game()
    arcade.run()

main()