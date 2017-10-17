import arcade
import random

from modeltmp import Rocket, World, Alien

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

        self.score = 0
        self.world = World(width, height)
        self.alien_list = []
        self.rocketsp = ModelSprite('images/Rocket2.png', model=self.world.rocket)
        for alien in self.world.alien_list:    
            self.alien_list.append(ModelSprite('images/Alien.png', model = alien))
        self.bullet_list = []

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()

        self.rocketsp.draw()
        
        for alien in  self.alien_list:
            alien.draw()

        #self.bulletsp.draw()
        for bullet in self.bullet_list:
            bullet.draw()

        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 600, arcade.color.WHITE, 12)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.world.rocket.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.world.rocket.delta_x = MOVEMENT_SPEED
        
        if key == arcade.key.SPACE:
            for bullet in self.world.bullet_list:
                self.bullet_list.append(ModelSprite("images/bullet.png", model = bullet))
            

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.world.rocket.delta_x = 0
 
def main():
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

main()