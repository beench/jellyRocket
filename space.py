import arcade
import random

from models import Rocket, World, Alien, Bullet

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 620

MOVEMENT_SPEED = 5

TIME = 0.5

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

        self.backgroud = arcade.load_texture('images/Space.jpg')
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.backgroud)
        

        self.score = 0
        self.world = World(width, height)
        self.alien_list = arcade.SpriteList()
        self.rocketsp = ModelSprite('images/Rocket2.png', 0.9, model=self.world.rocket)
        for alien in self.world.alien_list:    
            self.alien_list.append(ModelSprite('images/Alien.png', 0.8, model = alien))
        self.hit_list = []
        self.counttime = 0
        self.target = 50
        self.life = 2

    def update(self, delta):
        self.counttime += delta 

        for bullet in self.world.bullet_list:
            self.hit_list = arcade.check_for_collision_with_list(bullet, self.alien_list)
            if len(self.hit_list) > 0:
                bullet.kill()
            for alien in self.hit_list:
                alien.kill()
                self.score+=5

        if self.counttime >= TIME:
            self.world.status = 1
            if self.score > self.target:
                self.world.numAdd += 1
            self.target += 50
            self.counttime = 0

        if (self.score+5)%255 == 0:
            self.life += 1
            self.score += 10

        for alien in self.world.tmplist:
            self.alien_list.append(ModelSprite('images/Alien.png', 0.8, model = alien))
        
        self.world.tmplist = []

        for alien in self.alien_list:
            if alien.model.y <= 0:
                alien.kill()
                self.life -= 1
                print(self.life)
                if self.life < 0:
                    self.life = 0

        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()

        self.rocketsp.draw()
        
        for alien in self.alien_list:
            alien.draw()
            if self.life <= 0:
                output1 = "Game Over"
                arcade.draw_text(output1, 100, 320, arcade.color.WHITE, 46)
                output2 = "Score: {}".format(self.score)
                arcade.draw_text(output2, 190, 290, arcade.color.WHITE, 20) 

        for bullet in self.world.bullet_list:
            bullet.draw()

        output = "life: {}".format(self.life)
        arcade.draw_text(output, 400, 600, arcade.color.WHITE, 12)    

        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 600, arcade.color.WHITE, 12)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.world.rocket.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.world.rocket.delta_x = MOVEMENT_SPEED
        
        if key == arcade.key.SPACE:
            bullet = Bullet(self.world)
            bullet.x = self.world.rocket.x
            bullet.y = self.world.rocket.y + 10
            self.world.bullet_model.append(bullet)
            bullet_sprite = ModelSprite("images/bullet.png",0.5, model = bullet)
            self.world.bullet_list.append(bullet_sprite)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.world.rocket.delta_x = 0
 
def main():
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

main()