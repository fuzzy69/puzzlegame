# -*- coding: UTF-8 -*-
# !/usr/bin/env python

import os
import platform
import sys

from sdl2 import SDL_WINDOWPOS_CENTERED, SDL_WINDOW_SHOWN

from config import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game

if platform.system() == "Windows":
    os.environ["PYSDL2_DLL_PATH"] = os.path.abspath(os.path.dirname(sys.argv[0]))


def main():
    game = Game(GAME_TITLE, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT,
                SDL_WINDOW_SHOWN)
    if game.init():
        game.loop()
    game.destroy()
    return 0


if __name__ == "__main__":
    sys.exit(main())


# import sys
# import ctypes
# from sdl2 import *
#
# from puzzle.test import TextureManager
#
# def main():
#     SDL_Init(SDL_INIT_VIDEO)
#     window = SDL_CreateWindow(b"Hello World",
#                               SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
#                               592, 460, SDL_WINDOW_SHOWN)
#     windowsurface = SDL_GetWindowSurface(window)
#     renderer = SDL_CreateRenderer(window,-1, 0)
#
#     # image = SDL_LoadBMP(b"exampleimage.bmp")
#     # surface = SDL_LoadBMP(b"/mnt/ramdisk/lena_grary.bmp")
#     # print(surface)
#     # if not surface:
#     #     print(1)
#     # SDL_BlitSurface(image, None, windowsurface, None)
#     #
#     # SDL_UpdateWindowSurface(window)
#     # SDL_FreeSurface(image)
#
#     text = SDL_Texture()
#     src_rect = SDL_Rect(0, 0, 200, 100)
#     dst_rect = SDL_Rect(0, 0, 200, 200)
#     # surface = SDL_LoadBMP(b"assets/img/resume.bmp")
#     # surface = SDL_LoadBMP(b"/mnt/ramdisk/lena_gray.bmp")
#     # if not surface:
#     #     print(1)
#     # print(surface)
#     text_man = TextureManager()
#     print(text_man.load(b"/mnt/ramdisk/resume.bmp", renderer))
#
#     # text = SDL_CreateTextureFromSurface(renderer, surface)
#     # if not text:
#         # print(2)
#     # SDL_FreeSurface(surface)
#     # return text, byref(src_rect), byref(dst_rect)
#     # return text, src_rect, dst_rect
#
#     SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0)
#     SDL_RenderClear(renderer)
#     # SDL_RenderCopy(renderer, text, ctypes.byref(src_rect), ctypes.byref(dst_rect))
#     text_man.draw(0, 0, 200, 200, renderer)
#     SDL_RenderPresent(renderer)
#
#     running = True
#     event = SDL_Event()
#     while running:
#         while SDL_PollEvent(ctypes.byref(event)) != 0:
#             if event.type == SDL_QUIT:
#                 running = False
#                 break
#
#     SDL_DestroyWindow(window)
#     SDL_Quit()
#     return 0
#
# if __name__ == "__main__":
#     sys.exit(main())
