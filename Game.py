import arcade
from models import World, Rocket

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 620

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.rocket = arcade.Sprite('images/Rocket2.png')
        self.world = World(width, height)

    def on_draw(self):
        arcade.start_render()
        self.rocket.draw()

    def update(self, delta):
        self.world.update(delta)
        self.rocket.set_position(self.world.rocket.x, self.world.rocket.y)

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
        main()