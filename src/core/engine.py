# PROJECT WILDFIRE ENGINE

import numpy as np
import random as rand
import board
import rules

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

                    self.set_value(idxY, idxX, self.new_cell(idxY, idxX))
                    
            current_step +=1

        self.save_data()



