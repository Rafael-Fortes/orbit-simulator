import pygame


class NewText:
    def __init__(self, position:tuple, color:tuple, size:int):
        self.font = pygame.font.Font("assets/font/Home And Work.otf", size)
        self.position = position
        self.color = color


    def draw(self, screen, text:str):
        text_to_draw = self.font.render(text, True, self.color)
        text_rect = text_to_draw.get_rect(center=self.position)

        screen.blit(text_to_draw, text_rect)
