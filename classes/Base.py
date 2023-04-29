import pygame


class Base:
    BASE_IMAGE = pygame.transform.scale2x(pygame.image.load('./imgs/base.png'))
    WIDTH = BASE_IMAGE.get_width()
    SPEED = 5

    def __init__(self, y):
        self.y = y
        self.pos_base0 = 0
        self.pos_base1 = self.WIDTH

    def __move(self):
        self.pos_base0 -= self.SPEED
        self.pos_base1 -= self.SPEED

        if self.pos_base0 + self.WIDTH < 0:
            self.pos_base0 = self.pos_base1 + self.WIDTH

        if self.pos_base1 + self.WIDTH < 0:
            self.pos_base1 = self.pos_base0 + self.WIDTH

    def draw(self):
        pygame.display.get_surface().blit(
            self.BASE_IMAGE, (self.pos_base0, self.y))
        pygame.display.get_surface().blit(
            self.BASE_IMAGE, (self.pos_base1, self.y))

        self.__move()
