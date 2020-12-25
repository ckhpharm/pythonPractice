import pygame
import sys
import random

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

width = 400
height = 300

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")

done = False

error_time = 0
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load(
    'hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]

# show hangman image depending on no answer


def createImage(error):
    pic = hangmanPics[error]
    screen.blit(pic, (width/2 - pic.get_width()/2 + 20, 50))

# word selection for quiz


def wordPick():
    f = open("words.txt", 'r')
    line = f.readlines()
    number = random.randrange(0, len(line)-1)
    return line[number].replace(' ', '')


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.unicode in quiz:

    screen = pygame.display.set_mode((width, height))
    screen.fill(WHITE)
    createImage(error_time)
    pygame.display.update()
    print(wordPick())
    pygame.time.wait(3000)

# while not done:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#     screen.fill(WHITE)
#     createImage(error_time)
