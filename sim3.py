from math import *
import calc


def sim3(self,obj1,obj2, ini_v):
    G = 6, 674 * 10 ** -11
    G = G[-1]
    dx1 = calc.dx(obj1, obj2)
    dy1 = calc.dy(obj1, obj2)
    dx2 = calc.dx(obj2, obj1)
    dy2 = calc.dy(obj2, obj1)
    r1 = hypot(dx1, dy1)
    r2 = hypot(dx2, dy2)
    fg = float(G)*obj1.m * obj2.m/r1
    fg2 = float(G)*obj1.m * obj2.m/r2
    v_c1 = fg / self.c1.m
    v_c2 = fg2 / self.c2.m
    a1 = calc.calc_angle(obj1, obj2)
    a2 = calc.calc_angle(obj2, obj1)
    gx1,gy1 = calc.vec_calc(a1,v_c1)
    gx2,gy2 = calc.vec_calc(a2,v_c2)
    if not self.d:
        #einmal um ini_v ableiten
        self.nx1,self.ny1 = gx1 ,gy1 + ini_v
        self.nx2,self.ny2 = gx2 ,gy2
        self.d = True
    else:
        #immer um fg ableiten
        self.nx1,self.ny1 = self.nx1 + gx1, self.ny1 + gy1
        self.nx2,self.ny2 = self.nx2 + gx2, self.ny2 + gy2
    #print(self.nx1, self.ny1)


    obj1.x -= self.nx1
    obj1.y -= self.ny1
    obj2.x -= self.nx2
    obj2.y -= self.ny2
    if self.c1.hitbox.colliderect(self.c2.hitbox):
        self.running = False
    return None

