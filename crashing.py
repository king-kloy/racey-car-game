import pygame
import time
import random

pygame.init()

screen_width = 800
screen_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('kloy 1.0')
clock = pygame.time.Clock()

image = pygame.image.load('heart.png')

def thing(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])

def screen_object(x, y):
    gameDisplay.blit(image, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    textFont = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, textFont)
    TextRect.center = ((screen_width/2),(screen_width/4))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(3)
    
    game_loop()

def crash():
    message_display('You Crashed\n kloy')


def game_loop():

    x = (screen_width * 0.45)
    y = (screen_height * 0.8)
    
    object_width = 100
    object_position = 0

    thing_x = random.randrange(0, screen_width)
    thing_y = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100


    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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

        thing(thing_x, thing_y, thing_width, thing_height, red)
        thing_y += thing_speed

        screen_object(x,y)

        if x > (screen_width - object_width) or x < 0:
            crash()
            
        if thing_y > screen_height:
            thing_y = 0 - thing_height
            thing_x = random.randrange(0, (screen_width-object_width))

        if y < thing_y + thing_height:
            print('y crossover')
            thing_speed += 0.5

            if (x  > thing_x) and (x < thing_x + thing_width) or (x + object_width > thing_x) and (x + object_width < thing_x + thing_width):
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)
        
game_loop()
pygame.quit()
quit()


