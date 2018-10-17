import pygame

pygame.init()

screen_width = 800
screen_height = 600

black = (0,0,0)
white = (255,255,255)


gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('race car')
clock = pygame.time.Clock()

image = pygame.image.load('heart.png')

def screen_object(x, y):
    gameDisplay.blit(image, (x,y))


def game_loop():

    x = (screen_width * 0.45)
    y = (screen_height * 0.8)
    
    object_width = 100
    object_position = 0

    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    object_position = -5

                if event.key == pygame.K_RIGHT:
                    object_position = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    object_position = 0
        
        x += object_position
        
        gameDisplay.fill(white)
        screen_object(x,y)

        if x > (screen_width - object_width) or x < 0:
            gameExit = True
        
        pygame.display.update()
        clock.tick(60)
        
game_loop()
pygame.quit()
quit()


