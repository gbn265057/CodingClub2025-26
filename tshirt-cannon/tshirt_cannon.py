import random

import pygame

from pygame.math import Vector2
from pygame.sprite import Sprite

pygame.init()

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RIGHT = Vector2(1, 0)

def make_transparent(image):
    image.set_colorkey(WHITE)
    image.fill(WHITE)

cannon = pygame.Surface((100, 100))
arrow = pygame.Surface((75, 10))
tshirt_image = pygame.Surface((100, 100))
target = pygame.Surface((100, 50))
make_transparent(cannon)
make_transparent(arrow)
make_transparent(tshirt_image)
make_transparent(target)

pygame.draw.polygon(cannon, BLACK, ((0, 75), (25, 100), (100, 25), (75, 0)))

pygame.draw.line(arrow, BLACK, (0, 5), (75, 5))
pygame.draw.polygon(arrow, BLACK, ((75, 5), (70, 0), (70, 10)))

pygame.draw.circle(tshirt_image, BLACK, (50, 50), 50)

pygame.draw.ellipse(target, GREEN, target.get_rect())

class TShirt(Sprite):
    GRAVITY: Vector2
    SIZE: float
    LAUNCH_SPEED: float

    def __init__(self, direction, *groups):
        super().__init__(*groups)
        self.velocity = direction
        self.velocity.scale_to_length(self.LAUNCH_SPEED)
        self.image = pygame.transform.scale(tshirt_image, (self.SIZE, self.SIZE))
        self.rect = self.image.get_rect()
    
    def update(self, time):
        self.rect.move_ip(self.velocity * time)
        self.velocity += self.GRAVITY * time

class Game:
    def __init__(self, screen, ticks):
        self.WIDTH, self.HEIGHT = screen.get_width(), screen.get_height()
        self.TICKS = ticks
        self.screen = screen
        self.playing = True

        self.build_cannon()
        self.place_target()

        self.points = 0
        self.points_font = pygame.font.Font(pygame.font.get_default_font(), 24)

        TShirt.SIZE = HEIGHT / 50
        TShirt.GRAVITY = Vector2(0, HEIGHT * 5/7)
        TShirt.LAUNCH_SPEED = 3/5 * WIDTH

        self.tshirts = pygame.sprite.Group()

    def build_cannon(self):
        CANNON_SIZE = self.HEIGHT / 8
        self.cannon = pygame.transform.scale(cannon, (CANNON_SIZE, CANNON_SIZE))
        self.CANNON_RECT = self.cannon.get_rect(bottomleft=(0, HEIGHT))
        self.CANNON_LOCATION = Vector2(
            self.CANNON_RECT.right - (self.CANNON_RECT.width / 8),
            self.CANNON_RECT.top + (self.CANNON_RECT.height / 8)
        )
    
    def place_target(self):
        target_height = self.HEIGHT / 16
        target_width = target_height * 2
        self.target = pygame.transform.scale(target, (target_width, target_height))
        min_x = self.CANNON_RECT.right
        max_x = self.WIDTH - self.target.get_rect().width
        target_x = random.randrange(min_x, max_x)
        self.target_rect = self.target.get_rect(bottomleft=(target_x, self.HEIGHT))

    def launch_tshirt(self, mouse_pos):
        x = max(mouse_pos[0], self.CANNON_LOCATION.x)
        y = min(mouse_pos[1], self.CANNON_LOCATION.y)
        direction = Vector2(x, y) - self.CANNON_LOCATION
        tshirt = TShirt(direction, self.tshirts)
        tshirt.rect.center = self.CANNON_LOCATION.xy # type: ignore
    
    def point_arrow(self, mouse_pos):
        x = max(mouse_pos[0], self.CANNON_LOCATION.x)
        y = min(mouse_pos[1], self.CANNON_LOCATION.y)
        direction_vector = Vector2(x, y) - self.CANNON_LOCATION
        angle = direction_vector.angle_to(RIGHT)
        rotated_arrow = pygame.transform.rotate(arrow, angle)
        arrow_rect = rotated_arrow.get_rect(bottomleft = self.CANNON_LOCATION.xy)
        return rotated_arrow, arrow_rect

    def check_collisions(self):
        hit_target = False
        for tshirt in self.tshirts:
            if not self.screen.get_rect().contains(tshirt.rect):
                tshirt.kill()
            if (not hit_target) and self.target_rect.colliderect(tshirt.rect):
                tshirt.kill()
                hit_target = True
        if hit_target:
            self.points += 1
            self.place_target()

    def draw_game(self):
        screen.fill(WHITE)
        screen.blit(self.cannon, self.CANNON_RECT)
        screen.blit(self.target, self.target_rect)
        self.tshirts.draw(screen)
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(*self.point_arrow(mouse_pos))
        points_text = self.points_font.render(str(self.points), True, BLACK)
        screen.blit(points_text, (10, 10))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.launch_tshirt(event.pos)
        self.tshirts.update(1 / self.TICKS)
        self.check_collisions()
        self.draw_game()
        
if __name__ == "__main__":
    WIDTH, HEIGHT = 1080, 720
    TICKS = 30
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen, TICKS)
    clock = pygame.time.Clock()

    while game.playing:
        clock.tick(TICKS)
        game.update()
        pygame.display.flip()
