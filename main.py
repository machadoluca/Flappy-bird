import pygame
from classes.Bird import Bird
from classes.Pipe import Pipe
from classes.Base import Base

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Flappy Bird')
    font_text = pygame.font.SysFont("arial", 50)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg = pygame.transform.scale2x(pygame.image.load('./imgs/bg.png'))
    game_clock = pygame.time.Clock()

    player = Bird(SCREEN_WIDTH / 2 - 34, SCREEN_HEIGHT / 2)
    pipes = [Pipe(SCREEN_WIDTH)]
    base = Base(700)
    bg_move = 0
    bg_width = bg.get_width()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        for i in range(0, 2):
            screen.blit(bg, (i * bg_width + bg_move, -100))

        bg_move -= 0.5
        if abs(bg_move) > bg_width:
            bg_move = 0

        player.draw()

        for pipe in pipes:
            if pipe.collision(player):
                print('game over')
                pygame.quit()
                exit()

            if pipe.x + pipe.top_pipe.get_width() < 0:
                pipes.pop(0)
                pipes.append(Pipe(600))

            pipe.draw()

        if pipe.x < player.x and pipe.point == False:
            score += 1
            pipe.point = True

        base.draw()

        score_text = font_text.render(f'Score: {score}', 1, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH - 10 - score_text.get_width(), 10))
        game_clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    main()