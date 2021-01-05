import pygame

from tetrislogic import * 


pygame.init()
size = (800, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")
carryOn = True

ScreenColor = ("#756C6C")
StraightLineColor = ("#F6810C")
clock = pygame.time.Clock()

while carryOn:
  locked_pos = {}
  grid = create_grid(locked_pos)

  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      carryOn = False 

  screen.fill(ScreenColor)
  draw_grid(screen, 20 , 11)


  pygame.display.flip()
 

pygame.quit()
