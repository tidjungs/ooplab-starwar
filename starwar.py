import arcade
import arcade.key

from models import World, Ship

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

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

class StarwarGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(self, width, height)
        self.ship_sprite = ModelSprite('images/ship.png',model=self.world.ship)
        self.update_enemy_sprite()

    def update_enemy_sprite(self):
        self.enemy_sprites = []
        for enemy in self.world.enemy:
            self.enemy_sprites.append(ModelSprite('images/enemy.png',model=enemy))

    def on_draw(self):
        arcade.start_render()
        self.ship_sprite.draw()

        for sprite in self.enemy_sprites:
            if self.world.enemy:
                sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = StarwarGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
