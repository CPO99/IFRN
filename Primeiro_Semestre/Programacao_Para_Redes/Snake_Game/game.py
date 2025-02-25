import pygame #importando biblioteca de jogos pygame
import random
import time

#definições do pygame
pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()

exe = True

num_frutas = 0


def Frutas():
    cores = ["white","red","green","yellow","silver"]
    
    frut = pygame.Vector2(random.randrange(0, screen.get_width()), random.randrange(0, screen.get_height()))

    pygame.draw.circle(screen, random.sample(cores,1)[0], frut, 5)

while exe:
    Frutas()

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            exe = False

    time.sleep(1)


pygame.quit()
    

