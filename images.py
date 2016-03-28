import pygame, sys, random
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([1200, 1000])
screen.fill([255, 0, 255])
for i in range (100):
    width = random.randit(0, 255)
    height = random.randit(0,100)
    top = random.randint(0, 400)
    left = random.randint(0,500)
    color_name = random.choice(THECOLORS.Keys())
    line_width = random.randint(1, 3)
    pygame.draw.rect(screen, [0,0,0], [left, top, width, height], 1)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
                    
