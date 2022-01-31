import pygame
from time import sleep
pygame.init()
pygame.mixer.music.load('des21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
sleep(3600)