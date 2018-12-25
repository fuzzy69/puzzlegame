# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from ctypes import byref

from sdl2 import SDL_Texture, SDL_Rect, SDL_LoadBMP, SDL_CreateTextureFromSurface, SDL_FreeSurface, SDL_Renderer, \
    SDL_RenderCopy


class TextureManager:
    
    def __init__(self, x: int, y: int, width: int, height: int, show: bool=True):
        self._texture = None
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._frame = 0
        self._show = show
    
    def load(self, file_path: str, renderer: SDL_Renderer) -> bool:
        temp_surface = SDL_LoadBMP(file_path)
        if not temp_surface:
            return False
        self._texture = SDL_CreateTextureFromSurface(renderer, temp_surface)
        SDL_FreeSurface(temp_surface)
        if not self._texture:
            return False
        return True
        
    def draw(self, renderer: SDL_Renderer):
        if self._show:
            x = 0 + self._width * self._frame
            src_rect = SDL_Rect(x, 0, self._width, self._height)
            dst_rect = SDL_Rect(self._x, self._y, self._width, self._height)
            SDL_RenderCopy(renderer, self._texture, byref(src_rect), byref(dst_rect))

    @property
    def show(self) -> bool:
        return self._show

    @show.setter
    def show(self, show: bool):
        self._show = show
