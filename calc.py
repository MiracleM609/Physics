from math import *
def vec_calc(angle, length):
    (dx, dy) = length * cos(radians(angle)), length * sin(radians(angle))
    return dx, dy

def dy(obj1, obj2):
    return obj1.y - obj2.y
def dx(obj1, obj2):
    return obj1.x - obj2.x


def calc_angle(obj1,obj2):

        return degrees(atan2(obj1.y - obj2.y, obj1.x - obj2.x))

def find_max_m(objs):
    maxm = 0
    for obj in objs:
        if obj.m > maxm:
            maxm = objs.index(obj)
    return maxm

#class Vector:
    #def __init__(self, x, y, length):
        #self.x = x
        #self.y = y
        #self.length = length
        #if self.x != 0:
        #    self.direction = degrees(atan(y / x))
        #else:
        #    self.direction = 0
#
#    def __add__(self, other):
#        return Vector(self.x+other.x,self.y+other.y,self.length+other.length)
#
#    def __str__(self):
 #       return f"({self.x}, {self.y}, {self.length}, {self.direction})"



