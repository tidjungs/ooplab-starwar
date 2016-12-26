import arcade.key
import math
from random import random

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class Ship(Model):
    def __init__(self, world, x, y, area):
        self.world = world
        self.x = x
        self.y = y
        self.area = area
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

        self.ship = Ship(self, 100, 100, 80)
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

        if self.is_game_over() and self.game_over == False:
            self.game_over = True
            self.starwarGameWindow.explode_sprite.set_position(self.ship.x, self.ship.y)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ship.switch_direction()

    def spawn_enemy(self):
        self.enemy.append(Enemy(self, 1000, math.ceil(random()*600)))
        self.starwarGameWindow.update_enemy_sprite()

    def is_game_over(self):
        ship = self.ship
        area = self.ship.area
        for enemy in self.enemy:
            if (ship.x >= enemy.x - area and ship.x <= enemy.x + area) and (ship.y >= enemy.y - area and ship.y <= enemy.y + area):
                return True
        return False
