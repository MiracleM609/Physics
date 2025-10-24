from math import *
import calc


def sim2(self,obj1,obj2, ini_v):
    G = 6, 674 * 10 ** -11
    G = G[-1]
    dx = calc.dx(obj1, obj2)
    dy = calc.dy(obj1, obj2)
    r = hypot(dx, dy)
    fg = float(G)*obj1.m * obj2.m/r
    v_c1 = fg / self.c1.m
    a = calc.calc_angle(obj1, obj2)
    gx1,gy1 = calc.vec_calc(a,v_c1)
    if not self.d:
        #einmal um ini_v ableiten
        self.nx1,self.ny1 = gx1 + ini_v,gy1
        self.d = True
    else:
        #immer um fg ableiten
        self.nx1,self.ny1 = self.nx1 + gx1, self.ny1 + gy1
    print("Hello",self.nx1, self.ny1)


    obj1.x -= self.nx1
    obj1.y -= self.ny1
    obj1.x -= ini_v
    if self.c1.hitbox.colliderect(self.c2.hitbox):
        self.running = False
    return None

