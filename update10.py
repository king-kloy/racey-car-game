import pygame
import time
import random

pygame.init()

screen_width = 800
screen_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
light_blue = (0,0,200)
green = (0,255,0)
light_green = (0,200,0)


gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('kloy 1.0')
clock = pygame.time.Clock()

image = pygame.image.load('car.png')

def thing(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])

def screen_object(x, y):
    gameDisplay.blit(image, (x,y))

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

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

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        textFont = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("kloy 1.0", textFont)
        TextRect.center = ((screen_width/2),(screen_width/4))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, light_green, (150,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, green, (150,450,100,50))
    
        if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, light_blue, (550,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, blue, (550,450,100,50))

        Font = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_objects("play", Font)
        textRect.center = ((150+100/2),(450+50/2))
        gameDisplay.blit(textSurf, textRect)

        textSurf, textRect = text_objects("exit", Font)
        textRect.center = ((550+100/2),(450+50/2))
        gameDisplay.blit(textSurf, textRect)


        pygame.display.update()
        clock.tick(20)

    #time.sleep(3)
    #game_loop()

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

    dodged = 0

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
        things_dodged(dodged)

        if x > (screen_width - object_width) or x < 0:
            crash()
            
        if thing_y > screen_height:
            thing_y = 0 - thing_height
            thing_x = random.randrange(0, (screen_width-object_width))
            dodged += 1
            thing_speed += 1

        if y < thing_y + thing_height:
            print('y crossover')
            

            if (x  > thing_x) and (x < thing_x + thing_width) or (x + object_width > thing_x) and (x + object_width < thing_x + thing_width):
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()        
#game_loop()
pygame.quit()
quit()


