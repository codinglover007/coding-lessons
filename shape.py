import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
done = False
size = [400, 300]

screen = pygame.display.set_mode(size)

while not done:
  pygame.time.wait(500)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill (BLACK)
  SQUARE = pygame.Rect((0,0), (200,200))
  pygame.draw.rect(screen, BLUE,SQUARE,1)
  pygame.draw.circle(screen,(204, 0, 204), (100,100), 100, 1)
  pygame.draw.line(screen,(0, 255,0), (0, 100), (100,0),1)
  pygame.draw.line(screen, ( 255, 0, 0), (100,0), (200,100),1)
  pygame.draw.line(screen, ( 255, 20, 147), (200,100), (100,200), 1)
  pygame.draw.line(screen, ( 255, 255, 51), (100,200), (0,100), 1)
  pygame.display.flip()
