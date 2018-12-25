# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from ctypes import byref, c_int

from sdl2 import SDL_Event, SDL_Renderer, SDL_MOUSEBUTTONDOWN, SDL_GetMouseState

from game_object import GameObject
from mixins import SignalMixin
from texture import TextureManager


class Button(TextureManager, GameObject, SignalMixin):
    
    def __init__(self, file_path: str, x: int, y: int, width: int, height: int, renderer: SDL_Renderer, id_: str,
                 show: bool=True):
        TextureManager.__init__(self, x, y, width, height, show)
        GameObject.__init__(self, x, y, width, height, id_)
        SignalMixin.__init__(self)
        self.load(file_path, renderer)
        
    def on_click(self):
        raise NotImplementedError
    
    def on_hover(self):
        pass

    def handle_events(self, event: SDL_Event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            x = c_int(0)
            y = c_int(0)
            SDL_GetMouseState(byref(x), byref(y))
            if self.is_in_bounds(x.value, y.value):
                self.on_click()
                # self.send("slot_restart_game")

    def set_show(self, show: bool):
        self.show = show
