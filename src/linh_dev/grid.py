from __future__ import annotations
from enum import IntEnum
from typing import List, Tuple
import numpy as np


class CellState(IntEnum):
    EMPTY = 0
    VEGETATION = 1
    BURNING = 2
    BURNED = 3
    BARRIER = 4


class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._cells = np.zeros((height, width), dtype=np.int8)

    def set_state(self, x: int, y: int, state: CellState) -> None:
        self._cells[y, x] = int(state)

    def get_state(self, x: int, y: int) -> CellState:
        return CellState(int(self._cells[y, x]))

    def get_neighbors(self, x: int, y: int, neighborhood: str = "moore") -> List[Tuple[int, int]]:
        if neighborhood == "moore":
            deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        else:
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = []
        for dy, dx in deltas:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                result.append((nx, ny))
        return result

    def count(self, state: CellState) -> int:
        return int(np.sum(self._cells == int(state)))

    def to_array(self) -> np.ndarray:
        return self._cells.copy()

    @classmethod
    def from_array(cls, array: np.ndarray) -> Grid:
        h, w = array.shape
        grid = cls(w, h)
        grid._cells = array.copy().astype(np.int8)
        return grid
