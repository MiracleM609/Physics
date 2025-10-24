def sim1(self, objs):
    g = 9.81
    for obj in objs:
        #if obj.hitbox.collidelist(self.objs_hitbox) == self.objs_hitbox.index(obj.hitbox):
            #print(f"hitbox {self.objs_hitbox.index(obj.hitbox)} collide {obj.hitbox.collidelist(self.objs_hitbox)}")
        obj.v += g * 1 / 60
        obj.y += obj.v * 1 / 60
        if obj.y > self.height:
            obj.y = self.height