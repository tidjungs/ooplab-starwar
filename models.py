import arcade.key
import math
from random import random

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class Bullet(Model):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def animate(self, delta):
        self.x += 5
        if self.x > 1000:
            del self

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
        self.bullet = []
        self.start = 0
        self.game_over = False

    def animate(self, delta):
        if self.start % 100 == 0:
            self.spawn_enemy()
        self.start += 1
        self.ship.animate(delta)
        for enemy in self.enemy:
            enemy.animate(delta)

        for bullet in self.bullet:
            bullet.animate(delta)

        self.check_enemy_dead()

        if self.is_game_over() and self.game_over == False:
            self.game_over = True
            self.starwarGameWindow.explode_sprite.set_position(self.ship.x, self.ship.y)


    def on_key_press(self, key, key_modifiers):
        if self.game_over == False:
            if key == arcade.key.SPACE:
                self.ship.switch_direction()
            elif key == arcade.key.ENTER:
                self.bullet.append(Bullet(self.ship.x, self.ship.y))
                self.starwarGameWindow.update_bullet_sprite()

    def check_enemy_dead(self):
        area = 60
        for enemy in self.enemy:
            for bullet in self.bullet:
                if (enemy.x >= bullet.x - area and enemy.x <= bullet.x + area) and (enemy.y >= bullet.y - area and enemy.y <= bullet.y + area):
                    self.enemy.remove(enemy)
                    self.bullet.remove(bullet)
                    self.starwarGameWindow.update_enemy_sprite()
                    self.starwarGameWindow.update_bullet_sprite()

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
