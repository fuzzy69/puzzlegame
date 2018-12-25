# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from abc import ABC, abstractmethod
from ctypes import byref, c_int

from sdl2 import SDL_Event, SDL_GetMouseState, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP, SDL_MOUSEMOTION


class DraggableMixin(ABC):
    """
    """
    instance = None
    
    # @abstractmethod
    # def on_drag(self, event: SDL_Event):
    #     # if not Draggable.instance:
    #     x = c_int(0)
    #     y = c_int(0)
    #     SDL_GetMouseState(byref(x), byref(y))
    #     if event.type == SDL_MOUSEBUTTONDOWN:
    #         if self.is_in_bounds(x.value, y.value):
    #             DraggableMixin.instance = self
    #             # print(x, y)
    #     elif event.type == SDL_MOUSEBUTTONUP:
    #         DraggableMixin.instance = None
    #     elif event.type == SDL_MOUSEMOTION:
    #         if DraggableMixin.instance and DraggableMixin.instance == self:
    #             if self.is_in_bounds(x.value, y.value):
    #                 # print(event.motion.xrel, event.motion.yrel)
    #                 xpos , ypos = self.get_position()
    #                 # print(xpos, ypos)
    #                 xpos += event.motion.xrel
    #                 ypos += event.motion.yrel
    #                 # print(xpos, ypos)
    #                 self.set_position(xpos, ypos)


class SignalMixin(ABC):
    """
    Simple signal/slot mixin. To be replaced with user SDL_Event
    """
    listeners = []
    
    def __init__(self):
        """
        :param obj:
        """
        SignalMixin.listeners.append(self)

    # @abstractmethod
    def send(self, method: str, *args, **kwargs):
        """
        :param method:
        :param args:
        :param kwargs:
        :return:
        """
        for obj in SignalMixin.listeners:
            if hasattr(obj, method):
                meth = getattr(obj, method)
                meth(*args, **kwargs)
