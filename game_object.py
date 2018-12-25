# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from vector2d import Vector2D


class GameObject:
    """
    """
    
    def __init__(self, x: int, y: int, width: int, height: int, id_: str):
        self._position = Vector2D(x , y)
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._id = id_
    
    @property
    def x(self) -> int:
        # return self._x
        return self._position.x
    
    @x.setter
    def x(self, value: int):
        # self._x = value
        self._position.x = value
    
    @property
    def y(self) -> int:
        # return self._y
        return self._position.y
    
    @y.setter
    def y(self, value: int):
        # self._y = value
        self._position.y = value
    
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, value: int):
        self._width = value
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value: int):
        self._height = value
    
    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def get_position(self) -> tuple:
        return self.x, self.y

    def is_in_bounds(self, x: int, y: int, margin: int=0) -> bool:
        if (self.x - margin) < x < (self.x + self.width + margin) and \
           (self.y - margin) < y < (self.y + self.height + margin):
            return True
        return False

    @property
    def id(self) -> str:
        return self._id
