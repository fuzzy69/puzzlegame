# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from ctypes import byref, c_int
from random import choice, randrange, shuffle

from sdl2 import SDL_Color, SDL_Event, SDL_GetMouseState, SDL_MOUSEBUTTONUP, SDL_MOUSEMOTION, \
    SDL_MOUSEBUTTONDOWN, SDL_Renderer, SDL_KEYDOWN, SDLK_a

from game_object import GameObject
from cell import Cell
from mixins import DraggableMixin, SignalMixin
from config import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, SHAPES_TEMPLATES, COLORS
from vector2d import Vector2D


class PieceCell(Cell):
    """
    """
    def __init__(self, x: int, y: int, size: int, color: SDL_Color, row: int, col: int):
        """
        :param x: x position on screen in px
        :param y: y position on screen in px
        :param size: width/height in px
        :param color: cell color
        :param row: row position in board
        :param col: column position in board
        """
        Cell.__init__(self, x, y, size, color)
        self._row = row
        self._col = col
        self._def_x = x
        self._def_y = y

    def reset(self):
        """
        Revert piece cell position  to default
        """
        self.x = self._def_x
        self.y = self._def_y

    @property
    def row(self) -> int:
        return self._row

    @property
    def column(self) -> int:
        return self._col

    def draw(self, renderer: SDL_Renderer, used: bool=False):
        Cell.draw(self, renderer, used)


class Piece(GameObject, DraggableMixin, SignalMixin):
    """
    Puzzle board piece
    """
    top = None  # Last moved piece
    
    def __init__(self, x: int, y: int, cell_size: int, color: SDL_Color, shape: tuple):
        """
        :param x:
        :param y:
        :param cell_size:
        :param color:
        :param shape:
        """
        GameObject.__init__(self, x, y, cell_size, cell_size, "piece")
        DraggableMixin.__init__(self)
        SignalMixin.__init__(self)
        self._cell_size = cell_size
        self._cells = []
        self._color = color
        self._shape = shape
        self._create_shape()
        self.used = False

    def _create_shape(self):
        for i, row in enumerate(self._shape):
            for j, cell in enumerate(row):
                if cell == 1:
                    x = self.x + j * self._cell_size
                    y = self.y + i * self._cell_size
                    cell = PieceCell(x, y, self._cell_size, self._color, i, j)
                    self._cells.append(cell)
                    w = (j + 1) * self._cell_size
                    h = (i + 1) * self._cell_size
                    self.width = max(self.width, w)
                    self.height = max(self.height, h)

    def reset(self):
        for cell in self._cells:
            cell.reset()
    
    def draw(self, renderer: SDL_Renderer):
        for cell in self._cells:
            cell.draw(renderer, not self.used)
    
    def set_position(self, x: int, y: int):
        if x <= 0 or x >= (SCREEN_WIDTH - self.width) or \
           y <= 0 or y >= (SCREEN_HEIGHT - self.height):
            return
        self.x = x
        self.y = y
        for cell in self._cells:
            cell.x = self.x + cell.column * self._cell_size
            cell.y = self.y + cell.row * self._cell_size
        Piece.top = self
    
    @property
    def color(self) -> SDL_Color:
        return self._color

    @property
    def cells(self) -> list:
        return self._cells
    
    # Event handlers
    def handle_events(self, event: SDL_Event):
        if not self.used:
            self.on_drag(event)

    def on_drag(self, event: SDL_Event):
        x = c_int(0)
        y = c_int(0)
        SDL_GetMouseState(byref(x), byref(y))
        if event.type == SDL_MOUSEBUTTONDOWN:
            if self.is_in_bounds(x.value, y.value):
                DraggableMixin.instance = self
        elif event.type == SDL_MOUSEBUTTONUP:
            if DraggableMixin.instance == self:
                self.send("slot_drop_piece", self)
                DraggableMixin.instance = None
        elif event.type == SDL_MOUSEMOTION:
            if DraggableMixin.instance and DraggableMixin.instance == self:
                if self.is_in_bounds(x.value, y.value):
                    # TODO: fix vector2d positioning
                    x1 , y1 = self.get_position()
                    # v1 = Vector2D(x1, y1)
                    # x2 = x1 + event.motion.xrel
                    # y2 = y1 + event.motion.yrel
                    # v2 = Vector2D(x2, y2)
                    # direction = v2 - v1
                    # print(direction)
                    # direction.normalize()
                    # print(direction)
                    # v3 = v1 + direction * 1.4
                    # print(v3)
                    # self.set_position(int(v3.x), int(v3.y))
                    # return
                    
                    x1 += event.motion.xrel
                    y1 += event.motion.yrel
                    self.set_position(x1, y1)
                elif self.is_in_bounds(x.value, y.value, 20):
                    x1 , y1 = self.get_position()
                    v1 = Vector2D(x1, y1)
                    # x2 = x1 + event.motion.xrel
                    # y2 = y1 + event.motion.yrel
                    v2 = Vector2D(x.value, y.value)
                    direction = v2 - v1
                    print(direction)
                    direction.normalize()
                    print(direction)
                    v3 = v1 + direction
                    print(v3)
                    self.set_position(int(v3.x), int(v3.y))
                    # self.set_position(x.value, y.value)

    def test(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key.keysym.sym == SDLK_a:
                self.send("slot_win_game")

    # Slots
    def slot_piece_used(self, piece):
        if piece == self:
            self.used = True
            for cell in self._cells:
                cell.reset()


class PieceFactory:
    
    def __init__(self, board):
        self._board = board
        self._pieces = []
        
    def create(self, count: int) -> [Piece]:
        """
        Factory method for creating puzzle piece instances
        :param count: number of pieces
        :return: list of piece objects
        """
        screen_blocks = []
        block_size = CELL_SIZE * 6  #
        for i in range(count):
            # TODO: better free space finding algorithm
            while True:
                # Split screen space into blocks
                x = randrange(1, (SCREEN_WIDTH - CELL_SIZE) // block_size) * block_size
                y = randrange(1, (SCREEN_HEIGHT - CELL_SIZE) // block_size) * block_size
                # Skip identical blocks
                if (x, y) in screen_blocks:
                    continue
                # Piece is in board bounds?
                if self._board.is_in_bounds(x, y, CELL_SIZE * 4):
                    continue
                if self._board.is_in_bounds(x + CELL_SIZE, y + CELL_SIZE, CELL_SIZE * 4):
                    continue
                # OK
                screen_blocks.append((x, y))
                break
        # Create piece shapes
        shapes = []
        for i in range(count // 4):
            shapes.extend(list(choice(SHAPES_TEMPLATES)))
        shuffle(shapes)
        for x, y in screen_blocks:
            piece = Piece(x, y, CELL_SIZE, choice(COLORS[1:]), shapes.pop())
            self._pieces.append(piece)
            
        return self._pieces

    @property
    def items(self):
        pass

    def rearrange(self):
        pass
