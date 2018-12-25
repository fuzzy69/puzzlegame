# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from ctypes import c_int, byref
from random import choice, randrange, shuffle

from sdl2 import SDL_Init, SDL_Quit, SDL_CreateWindow, SDL_DestroyWindow,SDL_CreateRenderer, SDL_DestroyRenderer, \
    SDL_Delay, SDL_Event, SDL_PollEvent, SDL_SetRenderDrawColor, SDL_RenderClear, SDL_RenderPresent, \
    SDL_SetRenderDrawColor, SDL_RenderFillRect, SDL_RenderDrawRect, SDL_RenderCopy

from sdl2 import SDL_INIT_VIDEO, SDL_WINDOWPOS_CENTERED, SDL_WINDOW_SHOWN, SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, \
    SDL_RENDERER_SOFTWARE, SDLK_t

from config import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TICKS_PER_FRAME, COLORS, BLACK_COLOR, \
    WHITE_COLOR, CELL_SIZE, BOARD_POSITION, BOARD_SIZE, SHAPES_TEMPLATES, PIECES_COUNT, DEBUG

from board import Board
from piece import Piece, PieceFactory
from ui import Button
from mixins import SignalMixin

class Game(SignalMixin):
    """
    """
    def __init__(self, title: str, x: int, y: int, width: int, height: int, flags: int):
        """
        :param title: game title
        :param x: game window x position in px
        :param y: game window y position in px
        :param width: game window width
        :param height: game window height
        :param flags: SDL_CreateWindow flags
        """
        SignalMixin.__init__(self)
        self._title = title
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._flags = flags
        self._window = None
        self._renderer = None
        self._game_objects = []
        self._pieces = None  # TODO: remove this
        self._running = False
        
    def init(self) -> bool:
        if SDL_Init(SDL_INIT_VIDEO) < 0:
            return False
        self._window = SDL_CreateWindow(GAME_TITLE, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH,
                                        SCREEN_HEIGHT, SDL_WINDOW_SHOWN)
        if not self._window:
            return False
        self._renderer = SDL_CreateRenderer(self._window, -1, SDL_RENDERER_SOFTWARE)
        if not self._renderer:
            return False
        # Game objects
        board = Board(BOARD_POSITION[0], BOARD_POSITION[1], BOARD_SIZE, CELL_SIZE, WHITE_COLOR)
        self._game_objects.append(board)
        # Create piece shapes
        self._pieces = PieceFactory(board)
        for piece in self._pieces.create(PIECES_COUNT):
            self._game_objects.append(piece)
        # Create menu buttons
        restart_menu = Button(b"assets/img/restart.bmp", 0, 0, 200, 50, self._renderer, "restart_menu")
        exit_menu = Button(b"assets/img/exit.bmp", SCREEN_WIDTH - 200, 0, 200, 50, self._renderer, "exit_menu")
        win_box = Button(b"assets/img/win.bmp", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 100, 400, 200,
                         self._renderer, "win_box", False)
        restart_menu.on_click = lambda: exit_menu.send("slot_restart_game")
        exit_menu.on_click = lambda: exit_menu.send("slot_exit_game")
        win_box.on_click = lambda: None
        win_box.slot_win_game = lambda: win_box.set_show(True)
        win_box.slot_restart_game = lambda: win_box.set_show(False)
        self._game_objects.append(restart_menu)
        self._game_objects.append(exit_menu)
        self._game_objects.append(win_box)
        self._running = True
        return True
    
    def run(self):
        pass
    
    def loop(self):
        event = SDL_Event()
        while self.is_running():
            self.handle_events(event)
            self.update()
            self.render()
    
    def handle_events(self, event: SDL_Event):
        while SDL_PollEvent(byref(event)) != 0:
            if event.type == SDL_QUIT:
                self._running = False
                break
            if event.type == SDL_KEYDOWN:
                if event.key.keysym.sym == SDLK_ESCAPE:
                    self._running = False
                    break
                elif DEBUG and event.key.keysym.sym == SDLK_t:
                    print("-" * 50)
                    for game_object in self._game_objects:
                        try:
                            print(game_object.used)
                        except Exception as e:
                            print(e)
            for game_object in self._game_objects:
                game_object.handle_events(event)
    
    def update(self):
        pass
    
    def render(self):
        # Render background
        SDL_SetRenderDrawColor(self._renderer, BLACK_COLOR.r, BLACK_COLOR.g, BLACK_COLOR.b, BLACK_COLOR.a)
        SDL_RenderClear(self._renderer)
        # Render game objects
        top_piece = None
        win_box = None
        for game_object in self._game_objects:
            if game_object.id == "piece" and globals()["Piece"].top == game_object:
                top_piece = game_object
            elif game_object.id == "win_box":
                win_box = game_object
            else:
                game_object.draw(self._renderer)
        if top_piece:
            top_piece.draw(self._renderer)
        if win_box:
            win_box.draw(self._renderer)
        # Update renderer
        SDL_RenderPresent(self._renderer)
        SDL_Delay(SCREEN_TICKS_PER_FRAME) # ~16ms ~60fps
    
    def destroy(self) -> int:
        """
        
        :return: status code
        """
        # Destroy game objects
        self._game_objects = []
        # Exit framework
        if self._renderer:
            SDL_DestroyRenderer(self._renderer)
        if self._window:
            SDL_DestroyWindow(self._window)
        SDL_Quit()
        return 0
    
    def is_running(self) -> bool:
        return self._running

    # Slots
    def slot_restart_game(self):
        # TODO: fix this
        pieces = self._pieces.create(PIECES_COUNT)
        for i, game_object in enumerate(self._game_objects):
            if game_object.__class__.__name__ == "Board":
                game_object.reset()
            if game_object.__class__.__name__ == "Piece":
                self._game_objects[i] = pieces.pop()

    def slot_exit_game(self):
        self._running = False
