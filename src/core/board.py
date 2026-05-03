import numpy as np

class Board:
    # constants 
    BARRIER = -1      # No fire spreads on the bariers
    GROUND = 0        # ground/empty cell
    VEGETATION = 1    # vegetation/fuel cell
    BURNING = 2       # burning cell
    BURNT = 3         # burnt cell
    
    # initialising the board
    def __init__(self, filename):
        # importing data from the text file
        data = np.load(filename)

        self.init_grid = data # creating the initial map
        self.curr_grid = data # creating the current map

        #saving the size of the map
        self.num_rows = len(data)
        self.num_cols = len(data[0])


    # This method returns size of the grid
    # usage: .get_size()
    def get_size(self):
        X_size = self.num_cols
        Y_size = self.num_rows
        return X_size, Y_size
    
    # This method returns the value at the specific position.
    # The output value of this method can be 0, 1, 2, 3.
    # 0 - ground/empty cell
    # 1 - vegetation/fuel cell
    # 2 - burning cell
    # 3 - burnt cell
    # usage: .get_value(row, col)
    def get_value(self, row, col):
        return (self.curr_grid[row, col])


    # This method sets the value at the specific position.
    # The input value of this method can be 0, 1, 2, 3.
    # For any other input value, method throws an exception.
    # usage: .set_value(row, col, input)
    def set_value(self, row, col, input):
        allowed_values = [self.BARRIER,
                          self.GROUND,
                          self.VEGETATION,
                          self.BURNING,
                          self.BURNT]
        if input not in allowed_values:
            raise ValueError("Invalid input")
        self.curr_grid[row, col] = input


    # This method restarts the current grid. The state
    # of the map returns to the initial configuration.
    # usage: .restart_map()
    def restart_map(self):
        self.curr_grid = self.init_grid


    # This method builds a barrier on the given position
    # This is simplification of the set_value method
    # usage: .buld_barrier(row, col)
    def build_barrier(self, row, col):
        self.set_value(row, col, self.BARRIER)


    # This method ignites the fire on the given position
    # This is simplification of the set_value method
    # usage: .ignite_fire(row, col)
    def ignite_fire(self, row, col):
        self.set_value(row, col, self.BURNING)

        
        








