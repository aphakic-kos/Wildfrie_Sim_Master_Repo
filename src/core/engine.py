# PROJECT WILDFIRE ENGINE

import numpy as np
import random as rand
import board
import rules


# MAP GENERATION

#First step is the initialisation of the grid size 

class MapGeneration(board.MapCreator):

    def __init__(self, seed, num_rows, num_cols, path, output):
        self.gen_type = gen_type
        super(MapGeneration).__init__(num_rows, num_cols)
        if self.seed == 'random':
            self.random_map()
        elif self.seed == 'trail':
            self.trail_map()
        else:
            raise ValueError('invalid seed input')
        self.save_data(path, output)

    def add_barriers(self, filename, row, col, path, output)
        super(MapGeneration).__init__(fiename)
        self.build_barrier(row, col)
        self.save_data(path, output)


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



            



