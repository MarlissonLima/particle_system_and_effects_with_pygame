import pygame,random

#particle class
class Particle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velocity_x = random.uniform(-1,1) #random.uniform(a,b) return a random number between,and included,a and b
        self.velocity_y = random.uniform(-1,1)
        self.lifetime = 60

    def update(self):
        self.x +=self.velocity_x
        self.y +=self.velocity_y
        self.lifetime-=1

    def draw(self,window):
        color = (255,255,255)
        position = (int(self.x),int(self.y))
        pygame.draw.circle(window,color,position,2)

#particle system class
class ParticleSystem:
    def __init__(self):
        self.particles = []
    
    def add_particles(self,x,y):
        self.particles.append(Particle(x,y))
    
    def update(self):
        for particle in self.particles:
            particle.update()

            if particle.lifetime<=0:
                self.particles.remove(particle)
    
    def draw(self,window):
        for particle in self.particles:
            particle.draw(window)