# PROJECT WILDFIRE ENGINE

import numpy as np
import random as rand
import board
import rules


# MAP GENERATION

class Simuation(board.Map, rules.Rules):
    def __init__(self, total_steps, filename, grid)
        self.total_steps = total_steps
        super(Simulation).__init__(filename)
        super(Simulation).__init__(grid)


    def run(self, ignition_point):
        self.ignition_row = ignition_point[0]
        self.ignition_col = ignition_point[1]
        current_step = 0
        
        self.ignite_fire(self.ignition_row, self.ignition_col)
        self.fire_row = self.iginition_row
        self.fire_col = self.ignition_col

        while current_step <= total_steps:
            self.probibility(self.fire_row, self.fire_col)
            for idx in grid:



            



