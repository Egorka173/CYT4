import pygame
import sys

W, H = 1000, 600
collide = False
collide2 = False
n = 0

b = 0

# квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
# круг
circle_radius = 35
circle_pos = (0, 0)
# ЦВЕТА
RED = (255, 165, 0, 180)
BLUE = (0, 250, 154, 180)
YELLOW = (138, 43, 226, 180)
GRAY = (247, 37, 0)
BG = (175, 1, 255)


pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((W, H))
font = pygame.font.Font(None, 32)
font2 = pygame.font.Font(None, 32)
# создаем поверхность размером в 2-а раза больше радиуса круга и вкл. альфа-канал
surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
# на созданной поверхности рисуем круг желтого цвета
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
# находим рект у поверхности
rect1 = surface.get_rect()

clock = pygame.time.Clock()
FPS = 100
speed = [3, 3]


car = pygame.image.load('car3.png')
car_rect = car.get_rect()


def abc(x, y):
    if car_rect.left < 0 or car_rect.right > W:
        speed[0] = -x
    if car_rect.top < 0 or car_rect.bottom > H:
        speed[1] = -y
    return car_rect.move(speed)


while True:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            # circle_pos = e.pos
            rect1.center = e.pos

    car_rect = abc(speed[0], speed[1])

    screen.fill(BG)    

    screen.blit(car, car_rect)
    pygame.display.update()
