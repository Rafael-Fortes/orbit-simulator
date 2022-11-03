import pygame
from math import sqrt


class Object:
    def __init__(self, is_planet:bool, position:list, mass:int, direction:list=[0,0], origin:list=[0,0]):
        # define the sprite
        if is_planet:
            self.obj_surface = pygame.transform.scale(pygame.image.load("assets/sprites/17.png"), (256, 256))
        else:
            self.obj_surface = pygame.transform.scale(pygame.image.load("assets/sprites/10.png"), (16, 16))

        
        self.obj_rect = self.obj_surface.get_rect(center=position)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.obj_surface
        self.sprite.rect = self.obj_rect

        # set main config
        self.position = position
        self.mass = mass
        self.direction = direction
        self.origin = origin
        self.is_moving = True
        self.old_positions = []
        self.relative_pos = self.get_relative_pos(
            origin=self.origin,
            position=self.position
        )

        distance = self.get_distance(origin=self.origin)
        self.speed_up = self.get_acceleration(p_mass=1, distance=distance, g=10)

    
    def get_relative_pos(self, origin:list, position:list):
        # get the position in relative to the planet
        x = position[0] - origin[0]
        y = origin[1] - position[1]
        pos = [x, y]

        return pos

    
    def get_real_pos(self, origin:list, position:list):
        # get the position on the screen
        x = position[0] + origin[0]
        y = origin[1] - position[1]
        pos = [x, y]

        return pos
    

    def get_distance(self, origin:list):
        # get the distance relative o the planet
        x = self.relative_pos[0]
        y = self.relative_pos[1]
        sum_of_square = (x ** 2) + (y ** 2)
        distance = sqrt(sum_of_square)

        if distance == 0:
            return 1
        else:
            return distance
    

    def get_acceleration(self, p_mass:int, distance:float, g:float):
        # calculate the acceleration
        gravity_force = (p_mass * self.mass) / (distance ** 2)
        gravity_force = g * gravity_force

        coss = self.relative_pos[0] / distance
        sen = self.relative_pos[1] / distance

        x_force = -1 * (gravity_force * coss)
        y_force = -1 * (gravity_force * sen)

        return [x_force, y_force]


    def movement(self):
        if self.is_moving:
            distance = self.get_distance(origin=self.origin)
            self.speed_up = self.get_acceleration(p_mass=5, distance=distance, g=10)

            # acceleration
            self.direction[0] += self.speed_up[0]
            self.direction[1] += self.speed_up[1]

            # converting relative position
            self.relative_pos[0] += self.direction[0]
            self.relative_pos[1] += self.direction[1]

            # converting real position by relative position
            self.position = self.get_real_pos(origin=self.origin, position=self.relative_pos)

            # updating values
            self.obj_rect = self.obj_surface.get_rect(center=self.position)
            self.sprite.rect = self.obj_rect

            # saves all positions that the object was 
            self.old_positions.append(tuple(self.position))

    
    def draw(self, screen, show_path: bool):
        # draw the object and trail
        if show_path and len(self.old_positions) > 1:
            pygame.draw.aalines(
                surface=screen,
                color=(255, 255, 255),
                closed=False,
                points=self.old_positions)

        screen.blit(self.obj_surface, self.obj_rect)
    
    
    

    
