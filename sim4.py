from math import *
from random import randint

import calc,circle

def create_n_objs(n,game):
    for i in range(n):
        new_obj = circle.Object(game,randint(0,800), randint(0,800), 5, 5,m=randint(1000,10000000),colour="green")
        game.objs.append(new_obj)
        game.objs_hitbox.append(new_obj.hitbox)
        game.nx.append(0)
        game.ny.append(0)


def sim4(self,objs, ini_v):
    G = 6, 674 * 10 ** -11
    G = G[-1]
    for obj1 in objs:
        for obj2 in objs:
            if obj1 is obj2:
                break
            dx1 = calc.dx(obj1, obj2)
            dy1 = calc.dy(obj1, obj2)
            dx2 = calc.dx(obj2, obj1)
            dy2 = calc.dy(obj2, obj1)
            r1 = hypot(dx1, dy1)
            r2 = hypot(dx2, dy2)
            fg = -float(G) * obj1.m * obj2.m / r1
            fg2 = -float(G) * obj1.m * obj2.m / r2
            v_o1 = fg / obj1.m
            v_o2 = fg2 / obj2.m
            a1 = calc.calc_angle(obj1, obj2)
            a2 = calc.calc_angle(obj2, obj1)
            gx1, gy1 = calc.vec_calc(a1, v_o1)
            gx2, gy2 = calc.vec_calc(a2, v_o2)
            if obj1.hitbox.colliderect(obj2.hitbox):
                #if obj1 is not self.c2:
                    obj1.m += obj2.m
                #if obj2 is not self.c2:
                    objs.remove(obj2)
            try:
                if not self.d:
                    # einmal um ini_v ableiten
                    self.nx[objs.index(obj1)], self.ny[objs.index(obj1)] = gx1, gy1 + ini_v
                    self.nx[objs.index(obj2)], self.ny[objs.index(obj1)] = gx2, gy2
                    self.d = True
                else:
                    # immer um fg ableiten
                    self.nx[objs.index(obj1)], self.ny[objs.index(obj1)] = self.nx[objs.index(obj1)] + gx1, self.ny[objs.index(obj1)] + gy1
                    self.nx[objs.index(obj2)], self.ny[objs.index(obj2)] = self.nx[objs.index(obj2)] + gx2, self.ny[objs.index(obj2)] + gy2
                obj1.x += (self.nx[objs.index(obj1)]) *self.slow
                obj1.y += (self.ny[objs.index(obj1)]) *self.slow
                obj2.x += (self.nx[objs.index(obj2)])*self.slow
                obj2.y += (self.ny[objs.index(obj2)])*self.slow
            except ValueError:
                print("well")
            print(self.nx,self.ny)
#    dx1 = calc.dx(obj1, obj2)
#    dy1 = calc.dy(obj1, obj2)
#    dx2 = calc.dx(obj2, obj1)
#    dy2 = calc.dy(obj2, obj1)
#    r1 = hypot(dx1, dy1)
#    r2 = hypot(dx2, dy2)
#    fg = float(G)*obj1.m * obj2.m/r1
#    fg2 = float(G)*obj1.m * obj2.m/r2
#    v_o1 = fg / self.c1.m
#    v_o2 = fg2 / self.c2.m
#    a1 = calc.calc_angle(obj1, obj2)
#    a2 = calc.calc_angle(obj2, obj1)
 #   gx1,gy1 = calc.vec_calc(a1,v_o1)
  #  gx2,gy2 = calc.vec_calc(a2,v_o2)

    #print(self.nx1, self.ny1)





    return None

