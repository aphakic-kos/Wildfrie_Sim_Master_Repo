from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
import numpy as np


@dataclass
class SimulationConfig:
    width: int = 50
    height: int = 50
    neighborhood: str = "moore"
    p: float = 0.3
    wind_direction: float = 0.0
    wind_strength: float = 0.0
    seed: Optional[int] = 42
    barrier_budget: int = 20
    vegetation_density: float = 0.8


@dataclass
class SimulationState:
    grid_array: np.ndarray
    step: int
    is_running: bool
    is_done: bool


@dataclass
class Metrics:
    burned_pct: float
    burning_count: int
    duration: int
    reached_boundary: bool
