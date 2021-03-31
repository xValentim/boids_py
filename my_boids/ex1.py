import pygame

white = (255, 255, 255)
black = (0, 0, 0)
largura = 500
altura = 500
pos_x = largura / 2
pos_y = altura / 2
velocidade_x = 0
velocidade_y = 0
a = 1
pygame.init()
fundo = pygame.display.set_mode((largura, altura))
image = pygame.Surface((10, 10), pygame.SRCALPHA)

continua = True
while continua:
    fundo.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocidade_x = 0.01
                velocidade_y = 0
                a = 1
            if event.key == pygame.K_LEFT:
                velocidade_x = -0.01
                velocidade_y = 0
                a = -1
            if event.key == pygame.K_DOWN:
                velocidade_x = 0
                velocidade_y = 0.01
            if event.key == pygame.K_UP:
                velocidade_x = 0
                velocidade_y = -0.01
    pos_x += velocidade_x
    pos_y += velocidade_y
    pygame.draw.polygon(fundo, white,
    [(15 * a + pos_x, 5 + pos_y), (0 + pos_x, 2 + pos_y), (0 + pos_x, 8 + pos_y)])
    pygame.display.update()