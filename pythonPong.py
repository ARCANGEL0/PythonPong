
import numpy
import pygame
from pygame.locals import *
from sys import exit
import random
import pygame.surfarray as surfarray



pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640,480),0,32)

#Variaveis do jogo // Game variables
jogo = pygame.Surface((640,480))
fundo = jogo.convert()
fundo.fill((0,0,0))
bar = pygame.Surface((10,50))
barra1 = bar.convert()
barra1.fill((255,255,255))
barra2 = bar.convert()
barra2.fill((255,255,255))
boladraw = pygame.Surface((15,15))
bolamd = pygame.draw.circle(boladraw,(255,255,255),(int(15/2),int(15/2)),int(15/2))
bola = boladraw.convert()
bola.set_colorkey((0,0,0))



# Variaveis de definicoes tipo velocidade // Variables for some definitions like speed and stuff
barra1_x, barra2_x = 10. , 620.
barra1_y, barra2_y = 215. , 215.
bola_x, bola_y = 307.5, 232.5
mov_barra1, mov_barra2 = 0. , 0.
vel_x, vel_y, vel_bola = 250., 250., 250.
jog1 = "Player 1"
jog2 = "Player 2"
placar_barra1, placar_barra2 = 0,0
relogio = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

pronto = False
while pronto==False:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            pronto = True 
        if evento.type == KEYDOWN:
            if evento.key == K_UP:
                mov_barra1 = -vel_ai
            elif evento.key == K_DOWN:
                mov_barra1 = vel_ai
        elif evento.type == KEYUP:
            if evento.key == K_UP:
                mov_barra1 = 0.
            elif evento.key == K_DOWN:
                mov_barra1 = 0.

   # Score render // renderizacao do placar
    placar1 = font.render(str(placar_barra1), True,(255,255,255))
    placar2 = font.render(str(placar_barra2), True,(255,255,255))
    jogador1 = font.render(jog1, True, (255,255,255))
    jogador2 = font.render(jog2, True, (255,255,255))

# Renderizacao dos elementos na tela
    screen.blit(fundo,(0,0))
    
    frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
    screen.blit(barra1,(barra1_x,barra1_y))
    screen.blit(barra2,(barra2_x,barra2_y))
    screen.blit(bola,(bola_x,bola_y))
    screen.blit(placar1,(250.,210.))
    screen.blit(placar2,(380.,210.))
    screen.blit(jogador1,(100.,20.))
    screen.blit(jogador2,(450.,20.))

    barra1_y += mov_barra1

    # movimento da bola // ball movement
    tempo = relogio.tick(30)
    tempo_seg = tempo / 1000.0

    bola_x += vel_x * tempo_seg
    bola_y += vel_y * tempo_seg
    vel_ai = vel_bola * tempo_seg

    # AI do jogador 2 // Player 2 AI
    if bola_x >= 305.:
        if not barra2_y == bola_y + 7.5:
            if barra2_y < bola_y + 7.5:
                barra2_y += vel_ai
            if  barra2_y > bola_y - 42.5:
                barra2_y -= vel_ai
        else:
            barra2_y == bola_y + 7.5

    if barra1_y >= 420.: barra1_y = 420.
    elif barra1_y <= 10. : barra1_y = 10.
    if barra2_y >= 420.: barra2_y = 420.
    elif barra2_y <= 10.: barra2_y = 10.
    if bola_x <= barra1_x + 10.:
        if bola_y >= barra1_y - 7.5 and bola_y <= barra1_y + 42.5:
            bola_x = 20.
            vel_x = -vel_x
    if bola_x >= barra2_x - 15.:
        if bola_y >= barra2_y - 7.5 and bola_y <= barra2_y + 42.5:
            bola_x = 605.
            vel_x = -vel_x
    if bola_x < 5.:
        placar_barra2 += 1
        bola_x, bola_y = 320., 232.5
        barra1_y,bar_2_y = 215., 215.
    elif bola_x > 620.:
        placar_barra1 += 1
        bola_x, bola_y = 307.5, 232.5
        barra1_y, barra2_y = 215., 215.
    if bola_y <= 10.:
        vel_y = -vel_y
        bola_y = 10.
    elif bola_y >= 457.5:
        vel_y = -vel_y
        bola_y = 457.5




    pygame.display.update()

pygame.quit()
