import arcade
from models import World, Ship

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class StarwarGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(width, height)
        self.ship_sprite = arcade.Sprite('images/ship.png')

    def on_draw(self):
        arcade.start_render()
        self.ship_sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)
        self.ship_sprite.set_position(self.world.ship.x, self.world.ship.y)

if __name__ == '__main__':
    window = StarwarGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
