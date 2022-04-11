#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from moveManage import Menu

Size = 6
Height = 100 * Size + 100
Width = 100 * Size


def GameMenu():
    pygame.init()
    screen = pygame.display.set_mode([Width, Height])
    pygame.display.set_caption("Hunt The Wumpus")

    fps = pygame.time.Clock()
    fps.tick(60)
    menu = Menu(Size, Height, Width, screen)
    quitMenu = False
    pygame.mixer.init()
    pygame.mixer.music.load("./assets/musica.mp3")

    while not quitMenu:
        pygame.mixer.music.play()
        menu = menu.menu()
        if menu == 1:
            quitMenu = True
    pygame.quit()


if __name__ == "__main__":
    GameMenu()

