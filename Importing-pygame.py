Import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1200,1000])
screen.fill([0,250,250])
pygame.draw.circle(screen, ([255,0,0],[600,500], 20, 0)
pygame.display.flip()
while  True:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()
                   
                
                   
