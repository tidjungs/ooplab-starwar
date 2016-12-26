import arcade.key

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class Ship(Model):
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = "UP"

    def animate(self, delta):
        if self.y > self.world.height:
            self.y = 0
        elif self.y < 0:
            self.y = self.world.height

        if self.direction == "UP":
            self.y += 5
        else:
            self.y -= 5

    def switch_direction(self):
        if self.direction == "UP":
            self.direction = "DOWN"
        else:
            self.direction = "UP"

class Enemy(Model):
    def __init__(self, world,  x, y):
        self.x = x
        self.y = y
        self.world = world

    def animate(self, delta):
        self.x -= 5
        if self.x < 0:
            del self


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.ship = Ship(self, 100, 100)
        self.enemy = Enemy(self, 1000, 100)

    def animate(self, delta):
        self.ship.animate(delta)
        self.enemy.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ship.switch_direction()
