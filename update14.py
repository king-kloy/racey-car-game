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

pause = False

def thing(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])

def screen_object(x, y):
    gameDisplay.blit(image, (x,y))

def things_dodged(count):
    font = pygame.font.SysFont('comicsansms',25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    textFont = pygame.font.SysFont('comicsansms',50)
    TextSurf, TextRect = text_objects(text, textFont)
    TextRect.center = ((screen_width/2),(screen_width/4))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(3)
    
    game_loop()

def crash():
    message_display('You Crashed kloy')

def quitgame():
    pygame.quit()
    quit()

def button(text,x,y,w,h,deep_color,light_color,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, light_color, (x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, deep_color, (x,y,w,h))
    
    Font = pygame.font.SysFont('comicsansms',20)
    textSurf, textRect = text_objects(text, Font)
    textRect.center = ((x+w/2),(y+50/2))
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False
           
def paused():

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(white)
        textFont = pygame.font.SysFont('comicsansms',100)
        TextSurf, TextRect = text_objects("kloy 1.0", textFont)
        TextRect.center = ((screen_width/2),(screen_width/4))
        gameDisplay.blit(TextSurf, TextRect)

        button("continue",150,450,100,50,green,light_green,unpause)
        button("quit",550,450,100,50,blue,light_blue,quitgame)
        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(20)
           
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(white)
        textFont = pygame.font.SysFont('comicsansms',100)
        TextSurf, TextRect = text_objects("kloy 1.0", textFont)
        TextRect.center = ((screen_width/2),(screen_width/4))
        gameDisplay.blit(TextSurf, TextRect)

        button("play",150,450,100,50,green,light_green,game_loop)
        button("quit",550,450,100,50,blue,light_blue,quitgame)
        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(20)

    #time.sleep(3)
    #game_loop()

def game_loop():
    global pause

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
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    object_position = -5

                if event.key == pygame.K_RIGHT:
                    object_position = 5

                if event.key == pygame.K_p:
                    pause = True
                    paused()

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
quitgame()

