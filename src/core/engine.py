# PROJECT WILDFIRE ENGINE

import numpy as np
import random as rand
import board
import rules


# MAP GENERATION #
class MapGeneration(board.MapCreator):
# Initialises the board module and its inputs
    def __init__(self, seed, num_rows, num_cols, path, output):
        self.seed = seed
# Creates a new input called seed which can be used to generate a predefined map grid
        super(MapGeneration).__init__(num_rows, num_cols)
        if self.seed == 'random':
            self.random_map()
        elif self.seed == 'trail':
            self.trail_map()
        else:
            raise ValueError('invalid seed input')
        self.save_data(path, output)
# A method for adding barriers to be used with GUI, can be used to skip the map genration and load a pre generated map instead
    def add_barriers(self, filename, row, col, path, output)
        super(MapGeneration).__init__(fiename)
        self.build_barrier(row, col)
        self.save_data(path, output)

# SIMULATION #
class Simuation(board.Map, rules.Rules):
# Initialises the methods needed from board and rules
    def __init__(self, total_steps, filename, grid)
        super(Simulation).__init__(filename)
        super(Simulation).__init__(grid)

# Method for setting the ignition point for the sim 
    def run(self, ignition_point):
        self.ignition_row = ignition_point[0]
        self.ignition_col = ignition_point[1]
        current_step = 0
        
        self.ignite_fire(self.ignition_row, self.ignition_col)
        self.fire_row = self.iginition_row
        self.fire_col = self.ignition_col
# The main loop which is automatically started after ignition
        while current_step <= total_steps:
            self.new_cell(self.fire_row, self.fire_col)
            for idx in grid:
                


            



