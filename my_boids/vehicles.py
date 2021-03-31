import pygame as pyg 

class Vehicle(pg.sprite.Sprite):
    image = pyg.Surface((10, 10), pyg.SRCALPHA)
    pyg.draw.polygon(image, pyg.Color('white'),
                      [(15, 5), (0, 2), (0, 8)])
    
    