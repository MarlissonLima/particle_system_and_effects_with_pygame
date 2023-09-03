import pygame
from pygame.locals import *
import sys,math
from particles import ParticleSystem

#initialize pygame
pygame.init()

#clock
clock = pygame.time.Clock()

#window setup
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Simple game for particly system")

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)


#player setup
player_size = (50,50) #width,height
player_x = (window_width-player_size[0])//2
player_y = window_height - player_size[1]

player = pygame.Surface(player_size)
player.fill(WHITE)

speed = 5


#particle system
particle_system = ParticleSystem()



#rotation
def blitRotateCenter(window,surface,angle,x,y):
    rotated_surface = pygame.transform.rotate(surface,angle)
    new_rect = rotated_surface.get_rect(center = surface.get_rect(center=(x,y)).center)
    
    window.blit(rotated_surface,new_rect)

angle = 0
# game loop
while True:
    
    dt = clock.tick(60)/1000
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #particle position 
    particle_x = player_x + player_size[0]//2
    particle_y = player_y+player_size[1]//2

    keys = pygame.key.get_pressed()

    if keys[K_UP] and player_y >0:
        player_y -= speed/math.sqrt(2)
        particle_system.add_particles(particle_x,particle_y)
    
    if keys[K_DOWN] and player_y < window_height - player_size[1]:
        player_y += speed/math.sqrt(2)
        particle_system.add_particles(particle_x,particle_y)
    
    if keys[K_LEFT] and player_x > 0:
        player_x -= speed/math.sqrt(2)
        particle_system.add_particles(particle_x,particle_y)

    if keys[K_RIGHT] and player_x < window_width - player_size[0]:
        player_x += speed/math.sqrt(2)
        particle_system.add_particles(particle_x,particle_y)


    particle_system.update()

    window.fill(BLACK)
    player_pos = (player_x,player_y)

    rotate = blitRotateCenter(window,player,angle,*player_pos)
    angle+=5
    
    particle_system.draw(window)

    pygame.display.flip()


    

