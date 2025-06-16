#verlet integration

import pygame, sys
from pygame.constants import MOUSEBUTTONDOWN
from pygame.locals import QUIT
from dataclasses import dataclass

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()

#convenience defs
vec2 = pygame.Vector2
down = vec2(0,1)
right = vec2(1,0)
zero_vec = vec2(0,0)

local_g = 98100

@dataclass
class Point:
    label : str
    pos : vec2
    old_pos : vec2
    radius : float
    colour : list
    force : vec2 = zero_vec
    accel : vec2 = zero_vec
    mass : float = 1
    disp : float =0
    
    
    def draw(self):
        pygame.draw.circle(DISPLAYSURF, self.colour, self.pos, self.radius)
       
    def integrate(self, dt):
        self.accel = self.force / self.mass
        self.pos += (self.pos - self.old_pos) + 0.5 * self.accel * dt * dt
        self.disp = (self.pos - self.old_pos) + 0.5 * self.accel * dt * dt
        self.old_pos = self.pos
        
    def force_accum(self):
        self.force = local_g * self.mass * down
fp = Point("First point", vec2(200, 200), vec2(200, 200), 8, [0, 0, 0])

points = [fp]

while True:
  
    DISPLAYSURF.fill((255,255,255))
    #dt = clock.tick() / 1000
    dt = 0.001
    
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()

    for point in points:
      point.draw()
      point.force_accum()
      
    for point in points:
      point.integrate(dt)
   
    print(fp.disp)
    pygame.display.update()
