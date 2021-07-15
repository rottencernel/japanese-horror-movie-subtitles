import pygame
from random import choice, randrange


class Symbol:
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = choice(red_katakana)
        self.interval = randrange(5, 30)
    
    def draw(self, color):
        frames = pygame.time.get_ticks()

        if not frames % self.interval:
            self.value = choice(red_katakana if color == 'red' else lightred_katakana)

        self.y = self.y + self.speed if self.y < HIGHT else - FONT_SIZE
        surface.blit(self.value, (self.x, self.y))


class SymbolColumn:
    def __init__(self, x, y):
        self.column_hight = randrange(8, 24)
        self.speed = randrange(3, 7)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_hight, -FONT_SIZE)]

    def draw(self):
        [symbol.draw('red') if i else symbol.draw('lightred') for i, symbol in enumerate(self.symbols)]


RES = WIDTH, HIGHT = 1600, 900
FONT_SIZE = 40
alpha_value = 0

pygame.init()

screen = pygame.display.set_mode(RES)
surface = pygame.Surface(RES)
surface.set_alpha(alpha_value)
clock = pygame.time.Clock()

font = pygame.font.Font('font/ms mincho.ttf', FONT_SIZE, bold=True)
# алфавит символов Катакана 
katakana = [chr(int('0x30a0', 16) + i) for i in range(96)] 
# katakana = [str(int('01' )- i) for i in range(2)]
red_katakana = [font.render(char, True, pygame.Color('red')) for char in katakana]
# делаем последний символ светлым
lightred_katakana = [font.render(char, True, pygame.Color(255,52,63)) for char in katakana]

symbol_column = [SymbolColumn(x, randrange(-HIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]


while True:
    screen.blit(surface, (0, 0))
    surface.fill(pygame.Color('black'))

    [symbol_column.draw() for symbol_column in symbol_column]

    if not pygame.time.get_ticks() % 20 and alpha_value < 170:
        alpha_value += 6
        surface.set_alpha(alpha_value)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(60)





