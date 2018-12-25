# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from sdl2 import SDL_Color, SDL_SetRenderDrawColor, SDL_RenderFillRect, SDL_RenderDrawRect, SDL_Renderer

from rectangle import Rectangle


class Cell(Rectangle):
    def __init__(self, x: int, y: int, size: int, color: SDL_Color):
        Rectangle.__init__(self, x, y, size, size, color)
        self._default_color = color
        
    def draw(self, renderer: SDL_Renderer, fill: bool=True):
        SDL_SetRenderDrawColor(renderer, self._color.r, self._color.g, self._color.b, self._color.a)
        if fill:
            SDL_RenderFillRect(renderer, self._rect)
        else:
            SDL_RenderDrawRect(renderer, self._rect)
    
    def is_in_bounds(self, x: int, y: int) -> bool:
        if (self._rect.x <= x <= self._rect.x + self._rect.w) and \
        (self._rect.y <= y <= self._rect.y + self._rect.h):
            return True
        return False
