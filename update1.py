import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('race car')
clock = pygame.time.Clock()

clashed = False

while not clashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            clashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()


