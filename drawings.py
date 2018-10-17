import pygame

pygame.init()

black = (0,0,0)
red = (255,0,0)
blue = (0,255,0)
white = (255,255,255)
green = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('drawing')
gameDisplay.fill(white)

pixel_array = pygame.PixelArray(gameDisplay)
pixel_array[30][50] = blue

pygame.draw.line(gameDisplay, red, (200,200), (400,200), 5)#5 = thickness and others = position

pygame.draw.rect(gameDisplay, blue, (400,400,50,20)) # 400 = position #50 = width #20 = height

pygame.draw.circle(gameDisplay, green, (200,400), 35) #35 = radius and others are the position

pygame.draw.polygon(gameDisplay, black,((100,200),(200,300),(300,200),(200,100),(200,300)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
