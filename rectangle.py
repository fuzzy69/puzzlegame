# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from sdl2 import SDL_Rect, SDL_Color


class Rectangle:
    """
    Proxy class for SDL_Rect struct
    """
    def __init__(self, x: int, y: int, w: int, h: int, color: SDL_Color):
        self._rect = SDL_Rect(x, y, w, h)
        self._color = color
        
    @property
    def x(self) -> int:
        return self._rect.x

    @x.setter
    def x(self, value: int):
        self._rect.x = value

    @property
    def y(self) -> int:
        return self._rect.y

    @y.setter
    def y(self, value: int):
        self._rect.y = value

    @property
    def width(self) -> int:
        return self._rect.w

    @width.setter
    def width(self, value: int):
        self._rect.w = value

    @property
    def height(self) -> int:
        return self._rect.h

    @height.setter
    def height(self, value: int):
        self._rect.h = value

    @property
    def color(self) -> SDL_Color:
        return self._color

    @color.setter
    def color(self, color: SDL_Color):
        self._color = color

    def get(self):
        return self._rect

    def set_position(self, x: int, y: int):
        self._rect.x = x
        self._rect.y = y
        
    def get_position(self) -> tuple:
        return self._rect.x, self._rect.y
