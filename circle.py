import math

import pygame

class Object:
    def __init__(self, game, x, y, width, height, m, colour="red"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.game = game
        self.hitbox = pygame.Rect(self.x-self.width, self.y-self.width,self.width*2,self.height*2)
        self.m = m
        self.width =self.m/self.game.scale
        self.height =self.m/self.game.scale
        self.v = 0
        self.vec = pygame.math.Vector2(self.x,self.y)
    def draw(self):
        pygame.draw.circle(self.game.screen, self.colour, (self.x, self.y), self.m/self.game.scale)
        #pygame.draw.rect(self.game.screen, "red", self.hitbox,2)
        self.hitbox = pygame.Rect(self.x-self.width, self.y-self.width,self.width*2,self.height*2)

    def calcnewpos(self, vector):
        (angle, z) = vector
        (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
        return dx, dy


    def update(self):
        self.draw()
