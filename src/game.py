import pygame
from src import object, text


class Game:
    def __init__(self, width, height, bg_color):
        pygame.font.init()

        # set main config
        self.width = width
        self.height = height
        self.bg_color = bg_color

        self.screen_center = (self.width // 2, self.height // 2)

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.obj_qnt = 0
        self.objects = []
        self.force = [0, 0]

        # creating planet object
        self.planet = object.Object(
            is_planet=True,
            position=self.screen_center,
            mass=1,
            direction=[0, 0],
            origin=[0, 0]
        )

        # creating text object
        self.forcex_text = text.NewText(position=(width-100, self.screen_center[1]), color=(255, 255, 255), size=25)
        self.direction_text = text.NewText(position=(width-100, self.screen_center[1]-25), color=(255, 255, 255), size=25)
        self.forcey_text = text.NewText(position=(width-100, self.screen_center[1]+25), color=(255, 255, 255), size=25)
        self.keys1_text = text.NewText(position=(self.screen_center[0], height - 45), color=(255, 255, 255), size=25)
        self.keys2_text = text.NewText(position=(self.screen_center[0], height - 20), color=(255, 255, 255), size=25)


    def draw(self):
        # draw screen and planet
        self.screen.fill(self.bg_color)
        self.planet.draw(self.screen, show_path=False)
        
        # draw objects
        for pos, obj in enumerate(self.objects):
            if pos == self.obj_qnt - 1:
                show_path = True
            else:
                show_path = False
                
            obj.draw(self.screen, show_path=show_path)

        # update and draw all texts
        self.update_text()
        self.direction_text.draw(screen=self.screen, text=self.text_direction)
        self.forcex_text.draw(screen=self.screen, text=self.text_forcex)
        self.forcey_text.draw(screen=self.screen, text=self.text_forcey)
        self.keys1_text.draw(screen=self.screen, text=self.text_keys1)
        self.keys2_text.draw(screen=self.screen, text=self.text_keys2)

        
    
    def create_random_object(self, position):
        self.obj_qnt += 1

        force = self.force.copy()

        direction = [force[0], force[1]]

        obj = object.Object(
            is_planet=False,
            position=list(position),
            mass=10,
            direction=direction,
            origin=self.screen_center
        )

        self.objects.append(obj)


    def check_collision(self, sprite_1, sprite_2):
        # check if an object collided with another object
        if pygame.sprite.collide_mask(sprite_1, sprite_2):
            return True
        else:
            return False


    def update(self):
        # it makes the object move
        if len(self.objects) > 0:
            for obj in self.objects:
                if obj.is_moving:
                    obj.movement()
                    
                    if self.check_collision(self.planet.sprite, obj.sprite):
                        obj.is_moving = False
    

    def update_text(self):
        # update all texts
        if self.force[0] > 0 and self.force[1] == 0:
            self.text_direction = "direção: direita"
        elif self.force[0] < 0 and self.force[1] == 0:
            self.text_direction = "direção: esquerda"
        elif self.force[1] > 0 and self.force[0] == 0:
            self.text_direction = "direção: cima"
        elif self.force[1] < 0 and self.force[0] == 0:
            self.text_direction = "direção: baixo"
        elif self.force[1] < 0 and self.force[0] < 0:
            self.text_direction = "direção: esquerda e baixo"
        elif self.force[1] < 0 and self.force[0] > 0:
            self.text_direction = "direção: direita e baixo"
        elif self.force[1] < 0 and self.force[0] < 0:
            self.text_direction = "direção: esquerda e baixo"
        elif self.force[1] > 0 and self.force[0] > 0:
            self.text_direction = "direção: direita e cima"
        elif self.force[1] > 0 and self.force[0] < 0:
            self.text_direction = "direção: esquerda e cima"
        else:
            self.text_direction = "Sem direção"

        self.text_forcex = f"Força x: {self.force[0]:.3f}"
        self.text_forcey = f"Força y: {self.force[1]:.3f}"

        self.text_keys1 = """Left Mouse button: cria um novo objeto"""
        self.text_keys2 = """P: Pause  KEYUP: Sobe  KEYDOWN: Desce  KEYRIGHT: Direita  KEYLEFT: Esquerda"""