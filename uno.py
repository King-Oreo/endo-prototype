from types import FunctionType
from typing import List, Tuple
import pygame, sys
from pygame.constants import MOUSEBUTTONDOWN
from pygame.locals import QUIT
from dataclasses import dataclass

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Hello World!')

down = pygame.Vector2(0,1)

def rotate_point(point : tuple, angle : float, origin : tuple):
  ...


@dataclass
class Block:
    label : str
    pos : tuple
    width : int
    height : int
    angle : float
    colour : tuple
    
    def initialise(self):
      #for the 'private' variables
      self.x = self.pos[0]
      self.y = self.pos[1]
      #creating poitns going ccw from the top left
      self.points = [(self.x - self.width // 2, self.y - self.height // 2),
                     (self.x - self.width // 2, self.y + self.height // 2),
                     (self.x + self.width // 2, self.y + self.height // 2),
                     (self.x + self.width // 2, self.y - self.height // 2)]
      
    def spin(self, angle):
      for point in points:
        point = rotate_point(point, angle, pos)
      self.angle += angle

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.colour, self.obj, 0)
       

@dataclass
class Handle:
    label : str
    start_target : Block
    end_target : Block
    pos : tuple
    radius : float
    thickness : float

    def draw(self):
        pygame.draw.circle(DISPLAYSURF, (0,0,0), self.pos, self.radius)
        pygame.draw.line(DISPLAYSURF, (0,255,0), self.pos, self.start_target.pos, self.thickness)
        pygame.draw.line(DISPLAYSURF, (255,0,0), self.pos, self.end_target.pos, self.thickness)

UA = Block("Upper arm", (400, 300), 50, 20, 0, (0,255,255))
LA = Block("Lower arm", (500, 300), 50, 20, 0, (255,255,0))
blocks = [UA, LA]
for block in blocks:
  block.initialise()
  
elbow = Handle("Elbow", UA, LA, (450, 300), 5, 2)
handles = [elbow]
        

while True:
    DISPLAYSURF.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()

    for handle in handles:
        handle.draw()

    for block in blocks:
        block.draw()
        block.spin(1)

   
    pygame.display.update()