import numpy as np
import os
import random

#-------------------------------------------------------------
# constants
BARRIER = -1      # No fire spreads on the bariers
GROUND = 0        # ground/empty cell
VEGETATION = 1    # vegetation/fuel cell
BURNING = 2       # burning cell
BURNT = 3         # burnt cell

# list of choices
CHOICES = [BARRIER,
           GROUND,
           VEGETATION,
           BURNING,
           BURNT]

#--------------------------------------------------------------
# MapCreator class:
# This class stores the .npy files with the information
# about the configuration of the map. The default map
# only contains the GROUND.
class MapCreator:
    # initialises map creator.
    def __init__(self, num_rows, num_cols):
        self.grid = np.full([num_rows, num_cols],
                            GROUND, dtype = 'int16')
        self.num_rows = num_rows
        self.num_cols = num_cols

    # This method creates random map
    # usage: .random_map()
    def random_map(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.grid[i, j] = random.choices(CHOICES[1 : 2])

    # This method creates seeded_map
    # At the begining, we consider that we have 
    # default map with only ground. Now, at the
    # randomly chosen cell vegetation is seeded
    # and expanded on random direction. This will
    # create chain of wegetation that will cover
    # the map.
    # usage .seeded_map(Num_Vegetation)
    def seeded_map(self, Num_Vegetation):
        rows = self.num_rows
        cols = self.num_rows
        visited = np.zeros([rows, cols], dtype = bool)
        start_i = np.random.randint(0, rows - 1)
        start_j = np.random.randint(0, cols - 1)

        self.__helper_seeded_map(Num_Vegetation, visited,
                               start_i, start_j)

    # Helper method for creating vegetation
    # Starts from the given point and implements
    # the vegetation chain of size Num_Vegetation
    # usage: non-usable
    def __helper_seeded_map(self, Num_Vegetation,
                            visited, start_i, start_j):
        curr_i = start_i
        curr_j = start_j

        for step in range(Num_Vegetation):
            visited[curr_i, curr_j] = True 
            self.grid[curr_i, curr_j] = VEGETATION
            curr_i, curr_j = self.__getTranslation(visited, curr_i, curr_j)

    # Helper method for translation of the cell.
    # Finds random translation for the cell and
    # returns new current position
    def __getTranslation(self, visited, curr_i, curr_j):
        rows, cols = visited.shape
        dx, dy = 0, 0
        while(True):
            dx = np.random.randint(-1, 2)
            dy = np.random.randint(-1, 2)
            if(curr_i + dx < 0 | curr_i + dx > rows - 1 |
               curr_j + dy < 0 | curr_j + dy > cols - 1 |
               visited[curr_i + dx, curr_j + dy]):
                continue
        return curr_i + dx, curr_j + dy
    
    # The method receives list of commands.
    # The method fills the proper values in the matrix
    # The commands should be list of vectors of size 3
    # First component of the vector notifies the row index
    # Second component of the vector notifies the column index
    # Third component of the vector notifies the stage
    # usage: .custom_grid(commands)
    def custom_map(self, commands):
        for command in commands:
            row = command[0]
            col = command[1]
            value = command[2]
            self.grid[row, col] = value
    
    # saves the current map configuration
    # usage: .save_data(path, output)
    def save_data(self, path, output = "output.npy"):
        fullpath = os.path.join(path, output)
        np.save(fullpath, self.grid)


#----------------------------------------------------------------
# Map class:
# This class receives the text .npy files, and recreates map.
# Map configuration can be manipulated by the methods below.
class Map:
    # initialising the map
    def __init__(self, filename):
        # importing data from the text file
        data = np.load(filename)

        self.init_map = data # creating the initial map
        self.curr_map = data # creating the current map

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
    # The output value of this method can be -1, 0, 1, 2, 3.
    # usage: .get_value(row, col)
    def get_value(self, row, col):
        return (self.curr_map[row, col])


    # This method sets the value at the specific position.
    # The input value of this method can be -1, 0, 1, 2, 3.
    # For any other input value, method throws an exception.
    # usage: .set_value(row, col, input)
    def set_value(self, row, col, input):
        if input not in CHOICES:
            raise ValueError("Invalid input")
        self.curr_map[row, col] = input


    # This method restarts the current grid. The state
    # of the map returns to the initial configuration.
    # usage: .restart_map()
    def restart_map(self):
        self.curr_map = self.init_map


    # This method builds a barrier on the given position
    # This is simplification of the set_value method
    # usage: .buld_barrier(row, col)
    def build_barrier(self, row, col):
        self.set_value(row, col, BARRIER)


    # This method ignites the fire on the given position
    # This is simplification of the set_value method
    # usage: .ignite_fire(row, col)
    def ignite_fire(self, row, col):
        self.set_value(row, col, BURNING)

        
        








