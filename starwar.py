import arcade
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
 
class StarwarGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)

        self.ship = arcade.Sprite('images/ship.png')
        self.ship.set_position(100, 100)
 
    def on_draw(self):
        arcade.start_render()
        self.ship.draw()
 
 
if __name__ == '__main__':
    window = StarwarGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()