from __future__ import annotations
import math
import random
from .grid import Grid, CellState


class FireRules:
    def __init__(
        self,
        neighborhood: str = "moore",
        p: float = 0.3,
        wind_direction: float = 0.0,
        wind_strength: float = 0.0,
    ) -> None:
        self.neighborhood = neighborhood
        self.p = p
        self._wind_dir_rad = math.radians(wind_direction)
        self.wind_strength = wind_strength

    def _effective_p(self, from_x: int, from_y: int, to_x: int, to_y: int) -> float:
        if self.wind_strength == 0.0:
            return self.p
        # angle of spread direction; North=0°, East=90°
        angle = math.atan2(to_x - from_x, -(to_y - from_y))
        factor = 1.0 + self.wind_strength * math.cos(angle - self._wind_dir_rad)
        return min(1.0, max(0.0, self.p * factor))

    def apply(self, grid: Grid) -> Grid:
        new_grid = Grid.from_array(grid.to_array())
        for y in range(grid.height):
            for x in range(grid.width):
                if grid.get_state(x, y) == CellState.BURNING:
                    new_grid.set_state(x, y, CellState.BURNED)
                    for nx, ny in grid.get_neighbors(x, y, self.neighborhood):
                        if grid.get_state(nx, ny) == CellState.VEGETATION:
                            p_eff = self._effective_p(x, y, nx, ny)
                            if random.random() < p_eff:
                                new_grid.set_state(nx, ny, CellState.BURNING)
        return new_grid
