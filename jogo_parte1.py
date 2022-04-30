import pygame

from pygame.locals import *

from random import choice


pygame.init()

x = 57    
y = 30    
velocidade = 4
boost = 3

fundo = pygame.image.load('mapa.png')
direcao = pygame.image.load('linkcostas1.png')

#musica = pygame.mixer.music.load('Kakarino.mp3')
#pygame.mixer.music.play(-1)

cima = [pygame.image.load('linkcima1.png'), pygame.image.load('linkcima2.png')]

baixo = pygame.image.load('linkbaixo2.png') #pygame.image.load('linkbaixo1.png'), 

direita = [pygame.image.load('linkdireita1.png'), pygame.image.load('linkdireita2.png')]

esquerda = [pygame.image.load('linkesquerda1.png'), pygame.image.load('linkesquerda2.png')]

janela = pygame.display.set_mode((800,600))
nomeArq = pygame.display.set_caption('Jogo em Python')

janelaAberta = True

while janelaAberta:
    pygame.time.delay(50)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janelaAberta = False
            
    
    comandos = pygame.key.get_pressed()
    
    if comandos[pygame.K_UP] or comandos[pygame.K_w]:
        if y > -25:
            if comandos[pygame.K_w] and comandos[pygame.K_LCTRL] or comandos[pygame.K_UP] and comandos[pygame.K_LCTRL]:
                y -= velocidade + boost
            else:
                y -= velocidade
        
        direcao = choice(cima)
        
        
    elif comandos[pygame.K_DOWN] or comandos[pygame.K_s]:
        if y < 515:
            if comandos[pygame.K_s] and comandos[pygame.K_LCTRL] or comandos[pygame.K_DOWN] and comandos[pygame.K_LCTRL]:
                y += velocidade + boost
            else:
                y += velocidade
        
        direcao = baixo
        
        
    elif comandos[pygame.K_RIGHT] or comandos[pygame.K_d]:
        if x < 690 or x < 710 and y > 505:
            if comandos[pygame.K_d] and comandos[pygame.K_LCTRL] or comandos[pygame.K_RIGHT] and comandos[pygame.K_LCTRL]:
                x += velocidade + boost
            else:
                x += velocidade
        
        direcao = choice(direita)
        
        
    elif comandos[pygame.K_LEFT] or comandos[pygame.K_a]:
        if x > 5:
            if comandos[pygame.K_a] and comandos[pygame.K_LCTRL] or comandos[pygame.K_LEFT] and comandos[pygame.K_LCTRL]:
                x -= velocidade + boost
            else:
                x -= velocidade
        
        direcao = choice(esquerda)
    
    
    janela.blit(fundo, (0,0))     
    janela.blit(direcao, (x,y))
    pygame.display.update()
    
    

            
pygame.quit()        
