import pygame
import numpy
import math

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
largura = 640
altura = 300
vertices = [(25, 0), (50, 20), (25, 40), (0, 20)]

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Valentines Game')

continua = True
while continua: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            continua = False
    window.fill(white)
    pygame.draw.polygon(window, blue, vertices)
    pygame.display.update()

pygame.quit()