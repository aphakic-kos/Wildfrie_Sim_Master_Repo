from __future__ import annotations
import json
import random
from typing import List, Optional
import numpy as np
from .grid import Grid, CellState
from .rules import FireRules
from .interfaces import SimulationConfig, SimulationState, Metrics


class SimulationEngine:
    def __init__(self, config: SimulationConfig) -> None:
        self._config = config
        self._grid: Grid = Grid(1, 1)
        self._rules: FireRules = FireRules()
        self._step: int = 0
        self._barriers_placed: int = 0
        self._initial_vegetation: int = 0
        self._is_running: bool = False
        self.reset(config)

    def reset(self, config: SimulationConfig) -> None:
        self._config = config
        if config.seed is not None:
            random.seed(config.seed)
            np.random.seed(config.seed)
        self._rules = FireRules(
            neighborhood=config.neighborhood,
            p=config.p,
            wind_direction=config.wind_direction,
            wind_strength=config.wind_strength,
        )
        self._grid = Grid(config.width, config.height)
        rng = np.random.default_rng(config.seed)
        veg_mask = rng.random((config.height, config.width)) < config.vegetation_density
        for y in range(config.height):
            for x in range(config.width):
                if veg_mask[y, x]:
                    self._grid.set_state(x, y, CellState.VEGETATION)
        self._initial_vegetation = self._grid.count(CellState.VEGETATION)
        self._step = 0
        self._barriers_placed = 0
        self._is_running = False

    def ignite(self, x: int, y: int) -> None:
        if self._grid.get_state(x, y) != CellState.VEGETATION:
            raise ValueError(f"Cell ({x},{y}) is not VEGETATION")
        self._grid.set_state(x, y, CellState.BURNING)

    def place_barrier(self, x: int, y: int) -> None:
        if self._barriers_placed >= self._config.barrier_budget:
            raise ValueError("Barrier budget exhausted")
        state = self._grid.get_state(x, y)
        if state not in (CellState.VEGETATION, CellState.EMPTY):
            raise ValueError(f"Cannot place barrier on {state.name}")
        self._grid.set_state(x, y, CellState.BARRIER)
        self._barriers_placed += 1

    def step(self) -> SimulationState:
        self._is_running = True
        self._grid = self._rules.apply(self._grid)
        self._step += 1
        is_done = self._grid.count(CellState.BURNING) == 0
        if is_done:
            self._is_running = False
        return SimulationState(
            grid_array=self._grid.to_array(),
            step=self._step,
            is_running=self._is_running,
            is_done=is_done,
        )

    def get_state(self) -> SimulationState:
        is_done = self._grid.count(CellState.BURNING) == 0 and self._step > 0
        return SimulationState(
            grid_array=self._grid.to_array(),
            step=self._step,
            is_running=self._is_running,
            is_done=is_done,
        )

    def get_metrics(self) -> Metrics:
        burned = self._grid.count(CellState.BURNED)
        burning = self._grid.count(CellState.BURNING)
        burned_pct = burned / self._initial_vegetation if self._initial_vegetation > 0 else 0.0
        arr = self._grid.to_array()
        reached = bool(
            np.any(arr[0, :] == int(CellState.BURNED))
            or np.any(arr[-1, :] == int(CellState.BURNED))
            or np.any(arr[:, 0] == int(CellState.BURNED))
            or np.any(arr[:, -1] == int(CellState.BURNED))
        )
        return Metrics(
            burned_pct=burned_pct,
            burning_count=burning,
            duration=self._step,
            reached_boundary=reached,
        )

    def run_headless(self, n_steps: int) -> List[SimulationState]:
        history: List[SimulationState] = []
        for _ in range(n_steps):
            state = self.step()
            history.append(state)
            if state.is_done:
                break
        return history

    @classmethod
    def from_json(cls, path: str) -> SimulationEngine:
        with open(path) as f:
            data = json.load(f)
        ignition_pts = data.pop("ignition", [])
        config = SimulationConfig(**data)
        engine = cls(config)
        for pt in ignition_pts:
            engine.ignite(pt["x"], pt["y"])
        return engine
