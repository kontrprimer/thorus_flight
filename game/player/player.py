import pygame

from game.framework import Vector


class Player:
    def __init__(self, position: Vector):
        self.pos = position
        self.speed = Vector([0.51, 0.37])
        self.max_speed = 1

    def move(self, clip: Vector):
        self.pos = (self.pos + self.speed) % clip

    def accelerate(self, direction: Vector):
        self.speed += direction * 0.0008
        self.speed = self.speed.limit(self.max_speed)

    def draw(self):
        diagonal = Vector([40, 40])
        left_up = self.pos - diagonal / 2
        return pygame.Rect(*left_up, *diagonal)
