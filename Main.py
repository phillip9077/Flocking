import pygame
import math
import random
from Vector2 import Vector2

class Boid:
    pos = (0,0)
    dir = 0
    vel = 0
    radius = 0
    image = None
    
    def __init__(self, x, y, anglex, angley):
        self.pos = Vector2(x, y)
        self.dir = Vector2(anglex,angley) #default dir of 90 degrees
        self.vel = Vector2(3, 3)
        self.radius = 100
        self.image = pygame.image.load('triangle.png')
        
    def draw(self, screen):
        zoomed_img = pygame.transform.rotozoom(self.image, self.dir.rotation*(180/math.pi), 0.05)
        screen.blit(zoomed_img,(self.pos.x, self.pos.y))
        #pygame.draw.polygon(screen, (99,247,76), [(self.pos.x, self.pos.y+5), (self.pos.x, self.pos.y-5), (self.pos.x + 15, self.pos.y)], 0)

    def update(self):
        #change position of boid
        if(self.pos.y < -30):
            self.pos.y = 430
        if(self.pos.y > 430):
            self.pos.y = -30
            
        if(self.pos.x > 630):
           self.pos.x = -30
        if(self.pos.x < -30):
            self.pos.x = 630
        

        """if(self.dir.x == 0):
            self.pos.x += self.vel.x
        elif(self.dir.y == 0):
            self.pos.y -= self.vel.y"""
        #else:
        self.pos.x +=  self.dir.x*self.vel.x
        self.pos.y -= self.dir.y*self.vel.y #origin starts from top left so need to minus y to move "forward"
        
    def alignment(self, boid_list):
        result_vec = Vector2(0,0)
        neighbor_count = 0

        #add all neighboring velocities
        for boid in boid_list:
            if((self.pos.dist(boid.pos)) > 0 and (self.pos.dist(boid.pos) < self.radius)):
                result_vec.x += boid.dir.x
                result_vec.y += boid.dir.y
                neighbor_count+=1

        #divide by neighbor count to get average directional change

        if(neighbor_count == 0):
            return result_vec
        
        if(neighbor_count > 0):
            result_vec.x /= neighbor_count
            result_vec.y /= neighbor_count

        result_vec.normalize()
        
        return result_vec

    def cohesion(self, boid_list):
        result_vec = Vector2(0,0)
        neighbor_count = 0

        for boid in boid_list:
            if((self.pos.dist(boid.pos)) > 0 and (self.pos.dist(boid.pos) < self.radius)):
                result_vec.x += boid.pos.x
                result_vec.y += boid.pos.y
                neighbor_count+=1

        if(neighbor_count == 0):
            return result_vec

        #calculates the average "center of mass"
        if(neighbor_count > 0):
            result_vec.x /= neighbor_count
            result_vec.y /= neighbor_count
            result_vec = Vector2(result_vec.x - self.pos.x, result_vec.y - self.pos.y)
            
        result_vec.normalize()

        return result_vec

    def separation(self, boid_list):
        result_vec = Vector2(0,0)
        neighbor_count = 0

        for boid in boid_list:
            if((self.pos.dist(boid.pos)) > 0 and (self.pos.dist(boid.pos) < self.radius)): #detect boids in neighborhood
                result_vec.x += (boid.pos.x - self.pos.x)
                result_vec.y += (boid.pos.y - self.pos.y)
                neighbor_count+=1

        if(neighbor_count == 0):
            return result_vec

        if(neighbor_count > 0):
            result_vec.x /= neighbor_count
            result_vec.y /= neighbor_count

        result_vec.x *= -1
        result_vec.y *= -1

        result_vec.normalize()

        return result_vec

    def flocking(self, boid_list):
        align = self.alignment(boid_list)
        cohesion = self.cohesion(boid_list)
        separation = self.separation(boid_list)
        aWeight = 0.2
        cWeight = 0.2
        sWeight = 0.25
        
        """self.dir = self.dir + align
        self.dir = self.dir + cohesion
        self.dir = self.dir + separation"""

        self.dir.x += align.x + cohesion.x*cWeight + separation.x*sWeight
        self.dir.y += align.y + cohesion.y*cWeight + separation.y*sWeight
            
        self.dir.normalize()

def main():
    pygame.init()
    size = width, height = 600, 400
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption('Boids')
          
    flock = [] #list of boids

    print('Welcome to my flocking simulation!')
    print('Click anywhere on the screen to spawn a boid')
    print('Please enjoy!')

    for int in range(10):
        flock.append(Boid(random.randint(200,400), random.randint(100,200), 1, 2))
    
    while True:
        for e in pygame.event.get():
            if (e.type == pygame.MOUSEBUTTONDOWN):
                x,y = pygame.mouse.get_pos()
                flock.append(Boid(x, y, 1, 2))
        
        for boid in flock:
            boid.draw(surface)
            boid.flocking(flock)
            boid.update()
        pygame.display.update()
        surface.fill((255,255,255))
        pygame.time.delay(10)

if __name__ == "__main__": main()

        


