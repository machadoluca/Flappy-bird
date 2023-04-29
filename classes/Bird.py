import pygame


class Bird:
    BIRD_IMGS = [
        pygame.transform.scale2x(pygame.image.load('./imgs/bird1.png')),
        pygame.transform.scale2x(pygame.image.load('./imgs/bird2.png')),
        pygame.transform.scale2x(pygame.image.load('./imgs/bird3.png'))
    ]
    BIRD_GRAVITY = 0.4
    BIRD_TIME_ANIMATION = 8
    MAX_ROTATION = 25
    MAX_ROTATION_SPEED = 5

    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.current_img = self.BIRD_IMGS[1]
        self.height = self.y
        self.img_count = 0
        self.speed = 0
        self.angle = 0

    def jump(self):
        self.speed = -14
        self.height = self.y

    def __update(self):
        if self.speed < 0 or self.y < (self.height + 10):
            self.angle = self.MAX_ROTATION
        else:
            if self.angle > -60:
                self.angle -= self.MAX_ROTATION_SPEED

        self.y += self.speed
        self.speed += self.BIRD_GRAVITY * 2

    def get_mask(self):
        return pygame.mask.from_surface(self.current_img)
    
    def draw(self):
        self.img_count += 1

        if self.img_count == self.BIRD_TIME_ANIMATION:
            if self.current_img == self.BIRD_IMGS[2]:
                self.current_img = self.BIRD_IMGS[0]
                self.img_count = 0
            else:
                self.current_img = self.BIRD_IMGS[self.BIRD_IMGS.index(
                    self.current_img) + 1]
                self.img_count = 0

        if self.angle <= -30:
            self.current_img = self.BIRD_IMGS[1]
            self.img_count = 0

        bird_image = pygame.transform.rotate(self.current_img, self.angle)
        bird_image_rect = bird_image.get_rect(
            center=self.current_img.get_rect(topleft=(self.x, self.y)).center
        )

        self.__update()
        pygame.display.get_surface().blit(bird_image, bird_image_rect.topleft)
