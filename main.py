import pygame
import pyautogui
import circle
import presets
import sim1
import sim2
import sim3
import sim4
from sim4 import create_n_objs

pygame.init()


def edit_y_minus(obj):
    obj.y = obj.y +1
    return obj

def edit_y_plus(obj):
    obj.y = obj.y -1
    return obj

def edit_x_minus(obj):
    obj.x = obj.x +1
    return obj
def edit_x_plus(obj):
    obj.x = obj.x - 1
    return obj


class Game:
    def __init__(self,simulation):
        self.height = 800
        self.width = 1000
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.simulation = simulation
        self.preset_choice = 0
        self.should_change_delta_mouse = False
        self.scale = 0.001
        self.mouse_pos = (self.width/2, self.height/2)
        self.delta_mouse_x=0
        self.delta_mouse_y=0
        self.objs = []
        self.objs_hitbox = []
        #self.objs_hitbox = [self.c1.hitbox, self.c2.hitbox]
        self.nx = []
        self.ny = []
        self.ini_v = 0
        self.preset = False
        answer = ""
        while answer != "Y" and answer != "N" and self.simulation != 4:
            answer = input("Use a preset ? (Y/N): ")
        if  answer =="Y":
            self.preset = True
            print("Preset selected")
            self.preset_choice = presets.choose_preset(self,self.simulation)
        elif self.simulation != 4:
            self.scale = int(input("What scale shall be used? : "))
        else:
            self.scale = 1_000_000

        if self.simulation >1 and not self.preset:
            self.ini_v = int(input("Define the initial velocity:  : "))
        if self.simulation==4 and not self.preset:
            n = input("enter number of objects: ")
            n = int(n)
            create_n_objs(n,self)
        elif self.simulation<=3 :
            if not self.preset:
                m1 = int(input("Enter the mass of the first object: "))
                m2 = int(input("Enter the mass of the second object: "))
                self.c1 = circle.Object(self, 100, 200, 5, 20, m=m1, colour="green")
                self.c2 = circle.Object(self, 400, 400, 20, 20, m=m2, colour="red")
            else:
                m1,m2 = 0 , 0
                self.c1 = circle.Object(self, 200, 200, 5, 20, m=m1, colour="green")
                self.c2 = circle.Object(self, 600, 600, 20, 20, m=m2, colour="red")

                presets.load_presets(self,self.simulation,self.preset_choice)

            self.objs = [self.c1, self.c2]
            self.objs_hitbox = [self.c1.hitbox, self.c2.hitbox]

        #self.nx,self.ny= 0,0
        self.d = False
        self.fast =False
        self.slow = 0.1
        self.run()
    def run(self):
        pyautogui.moveTo(self.mouse_pos[0], self.mouse_pos[1])
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:self.running=False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:self.running=False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    self.fast =True
                    self.slow = 0.1

                if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                    self.fast=False
                    self.slow = 0.01
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.objs = list(map(edit_y_minus, self.objs))
            if keys[pygame.K_s]:
                self.objs = list(map(edit_y_plus, self.objs))
            if keys[pygame.K_a]:
                self.objs = list(map(edit_x_minus, self.objs))
            if keys[pygame.K_d]:
                self.objs = list(map(edit_x_plus, self.objs))

            if pygame.mouse.get_pos() != self.mouse_pos and pygame.mouse.get_pressed()[0] and self.should_change_delta_mouse:
                self.delta_mouse_x = pygame.mouse.get_pos()[0] - self.mouse_pos[0]
                self.delta_mouse_y = pygame.mouse.get_pos()[1] - self.mouse_pos[1]
            if pygame.mouse.get_pressed()[0]:
                self.mouse_pos = pygame.mouse.get_pos()
                self.objs = list(map(self.apply_delta_mouse, self.objs))
                self.delta_mouse_x = self.delta_mouse_y = 0
                self.should_change_delta_mouse = True
            if not pygame.mouse.get_pressed()[0] and self.should_change_delta_mouse:
                self.should_change_delta_mouse = False
            self.screen.fill((0,0,0))
            self.update()
            pygame.display.set_caption(f"{self.clock.get_fps()}")
            if self.simulation==4 :
                sim4.sim4(self, self.objs,self.ini_v)
            elif self.simulation==3:
                sim3.sim3(self, self.c1,self.c2,self.ini_v)
            elif self.simulation==2:
                sim2.sim2(self, self.c1,self.c2,self.ini_v)
            elif self.simulation==1:
                sim1.sim1(self,self.objs)


            pygame.display.flip()
            if not self.fast:self.clock.tick(200)


    def update(self):
        for obj in self.objs:
            obj.update()
        #pygame.draw.line(self.screen, (255,255,255),(self.c1.x,self.c1.y),(self.c2.x,self.c2.y))

    def apply_delta_mouse(self,obj):
        #print("delta_mouse_x",self.delta_mouse_x,"delta_mouse_y",self.delta_mouse_y)
        obj.x += self.delta_mouse_x
        obj.y += self.delta_mouse_y
        return obj

simulation = 0
while simulation not in range(1,5):
     try:
        simulation = int(input("Which simulation shall be started?: \n"
                               "1. Simple simulation of falling objects on planet earth \n"
                               "2. Simulation of 2 Bodies in Space. One is unmoving \n"
                               "3. Simulation of 2 Bodies in Space. Both are moving \n"
                               "4. Simulation of n Bodies in Space.\n" ))
     except ValueError:
         print("Invalid input. Please try again.")

game = Game(simulation)
pygame.quit()