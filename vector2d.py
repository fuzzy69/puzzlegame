# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from math import sqrt


class Vector2D:
    """
    
    """
    def __init__(self, x: float=0, y: float=0):
        """
        
        :param x:
        :param y:
        """
        self._x = x
        self._y = y
        
    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, val):
        self._y = val
    
    def __add__(self, vector):
        return Vector2D(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vector2D(self.x - vector.x, self.y - vector.y)
    
    def __mul__(self, scalar: float):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __eq__(self, vector) -> bool:
        return self.x == vector.x and self.y == vector.y
    
    def __ne__(self, vector) -> bool:
        return not self.__eq__(vector)

    def length(self) -> float:
        """
        :return:
        """
        return sqrt(self._x * self._x + self._y * self._y)
    
    def normalize(self):
        l = self.length()
        if l > 0:
            self._x /= l
            self._y /= l
    
    def __repr__(self):
        return "Vector2D({}, {})".format(self.x, self.y)
    
    
if __name__ == "__main__":
        v = Vector2D(3, 5)
        print(v)
