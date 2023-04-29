import pygame
import random


class Pipe:
    PIPE_IMG = pygame.transform.scale2x(pygame.image.load('./imgs/pipe.png'))
    PIPE_DISTANCE = 200
    SPEED = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top_pos = 0
        self.bottom_pos = 0
        self.top_pipe = pygame.transform.flip(self.PIPE_IMG, False, True)
        self.bottom_pipe = self.PIPE_IMG
        self.point = False
        self.__define_height()

    def __define_height(self):
        self.height = random.randrange(50, 450)
        self.top_pos = self.height - self.top_pipe.get_height()
        self.bottom_pos = self.height + self.PIPE_DISTANCE

    def __move_pipe(self):
        self.x -= self.SPEED

    def collision(self, bird):
        bird_mask = bird.get_mask()
        top_pipe_mask = pygame.mask.from_surface(self.top_pipe)
        bottom_pipe_mask = pygame.mask.from_surface(self.bottom_pipe)

        top_distance = (self.x - bird.x, self.top_pos - round(bird.y))
        bottom_distance = (self.x - bird.x, self.bottom_pos - round(bird.y))

        top_collision = bird_mask.overlap(top_pipe_mask, top_distance)
        bottom_collision = bird_mask.overlap(bottom_pipe_mask, bottom_distance)

        if top_collision or bottom_collision:
            return True

        return False

    def draw(self):
        self.__move_pipe()

        pygame.display.get_surface().blit(
            self.top_pipe, (self.x, self.top_pos))

        pygame.display.get_surface().blit(
            self.bottom_pipe, (self.x, self.bottom_pos))
