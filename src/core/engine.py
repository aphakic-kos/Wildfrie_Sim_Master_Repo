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
        self.get_size()
        current_step = 0
# The main loop which is automatically started after ignition   
       while current_step <= total_steps:
            for idxX in range(X_size):
                for idxY in range(Y_Size):
                    current_val = self.get_value(idxY, idxX)
                    if current_val == 2
                        self.new_cell(idxY, idxX)
            current_step +=1
       self.save_data()



