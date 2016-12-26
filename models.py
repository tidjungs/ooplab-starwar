import arcade.key
import math
from random import random

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
    def __init__(self, starwarGameWindow, width, height):
        self.width = width
        self.height = height
        self.starwarGameWindow = starwarGameWindow

        self.ship = Ship(self, 100, 100)
        self.enemy = []
        self.start = 0
        self.game_over = False

    def animate(self, delta):
        if self.start % 100 == 0:
            self.spawn_enemy()
        self.start += 1
        self.ship.animate(delta)
        for enemy in self.enemy:
            enemy.animate(delta)

        if self.is_game_over():
            self.game_over = True

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ship.switch_direction()

    def spawn_enemy(self):
        self.enemy.append(Enemy(self, 1000, math.ceil(random()*600)))
        self.starwarGameWindow.update_enemy_sprite()

    def is_game_over(self):
        ship = self.ship
        for enemy in self.enemy:
            if (ship.x >= enemy.x - 10 or ship.x == enemy.x + 10) and (ship.y >= enemy.y - 10 or ship.y == enemy.y + 10):
                return True
        return False
