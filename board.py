# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from ctypes import byref, c_int
from sdl2 import SDL_Color, SDL_Renderer, SDL_Event, SDL_GetMouseState, SDL_MOUSEBUTTONUP, SDL_RegisterEvents

from cell import Cell
from mixins import SignalMixin


class BoardCell(Cell):
    """
    Square element of puzzle board
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
        self._def_color = color
        self._used = False
    
    def draw(self, renderer: SDL_Renderer):
        Cell.draw(self, renderer, self._used)
        
    def reset(self):
        """
        Change cells properties to default
        """
        self._color = self._def_color
        self._used = False

    def get_board_position(self) -> tuple:
        """
        """
        return self._row, self._col

    @property
    def row(self) -> int:
        return self._row

    @property
    def column(self) -> int:
        return self._col

    @property
    def used(self) -> bool:
        return self._used
    
    @used.setter
    def used(self, value: bool):
        self._used = value

    # Events
    def on_drop_piece(self):
        pass

    
class Board(SignalMixin):
    """
    Puzzle board
    """
    def __init__(self, x: int, y: int, size: int, cell_size: int, color: SDL_Color):
        """
        :param x: x position on screen in px
        :param y: y position on screen in px
        :param size: number of rows/columns
        :param cell_size: board cell width/height in px
        :param color: color of cells
        """
        self._x = x
        self._y = y
        self._size = size
        self._cell_size = cell_size
        self._color = color
        self._cells = []
        self._create_grid()
        self.id = "board"
        SignalMixin.__init__(self)
        
    def _create_grid(self):
        """
        Create board cell instances and add them to cell list
        """
        for row in range(self._size):
            cells = []
            for col in range(self._size):
                x = self._x + col * self._cell_size
                y = self._y + row * self._cell_size
                cell = BoardCell(x, y, self._cell_size, self._color, row, col)
                cells.append(cell)
            self._cells.append(cells)
    
    def draw(self, renderer: SDL_Renderer):
        for row in self._cells:
            for cell in row:
                cell.draw(renderer)
            
    def is_in_bounds(self, x: int, y: int, margin: int=0) -> bool:
        """
        
        :param x:
        :param y:
        :param margin:
        :return:
        """
        if (self._x - margin) < x < (self._x + self._size * self._cell_size +margin) and \
           (self._y - margin) < y < (self._y + self._size * self._cell_size + margin):
            return True
        return False

    def _add_piece(self, piece, row: int, col: int, cell):
        # Check piece fit
        for piece_cell in piece.cells:
            r = row + piece_cell.row
            c = col + piece_cell.column
            if r >= self._size or c >= self._size:
                return
            if self._cells[r][c].used:
                return
        # Update board cell state
        for piece_cell in piece.cells:
            r = row + piece_cell.row
            c = col + piece_cell.column
            self._cells[r][c].used = True
            self._cells[r][c].color = piece.color
        self.send("slot_piece_used", piece)
        if self.is_full():
            self.send("slot_win_game")

    def _used_cells_count(self) -> int:
        num_used_cells = 0
        for row in self._cells:
            for cell in row:
                if cell.used:
                    num_used_cells += 1
        return num_used_cells

    def is_full(self) -> bool:
        return self._used_cells_count() == self._size * self._size

    def reset(self):
        for cells in self._cells:
            for cell in cells:
                cell.reset()

    # Event handlers
    def handle_events(self, event: SDL_Event):
        pass
        # self.on_drop_piece(event)
        
    # Signal slots
    def slot_drop_piece(self, piece):
        if not self.is_in_bounds(piece.x, piece.y):
            return
        for cells in self._cells:
            for cell in cells:
                if not cell.is_in_bounds(piece.x, piece.y):
                    continue
                if cell.used:
                    return
                row, col = cell.get_board_position()
                self._add_piece(piece, row, col, cell)
                return
