import numpy as np
from core.board import Map, BARRIER, GROUND, VEGETATION, BURNING, BURNT
from core.engine import Engine
import os
# This class provides analysis of data
# during the experiment. It only contains
# static methods.
class Analysis:

    # Empty constructor 
    def __init__(self):
        pass

    # This method calculates the percentage of burnt
    # area. It takes all of the burnt cells and then
    # divides total number of them on the total number
    # of map cells.
    # usage: Analysis.percentage_of_burnt_area(map)
    def percentage_of_burnt_area(map):
        curr_map = map.curr_map
    
        num_rows = curr_map.shape[0]
        num_cols = curr_map.shape[1]

        num_burned_cells = len(curr_map[curr_map == BURNT])
        num_total_cells = num_rows * num_cols

        percentage = num_burned_cells / num_total_cells * 100

        return percentage

    # This method calculates number of currently burning cells
    # usage: Analysis.currently_burning_cells(map)
    def currently_burning_cells(map):
        burning_cells = np.argwhere(map.curr_map == BURNING)
        return burning_cells

    # This method calculates total duration of the one wildfire
    # simulation.
    # usage: Analysis.wildfire_duration()
    def wildfire_duration():
        pass

    # This method runs multiple simulations of the wildfire
    # and stores duration and burnt_percentage of each simulation.
    # These data are kept in the .npy files and used for diagnostics
    # usage: statistical_experiment(map, N)
    def statistical_experiment(map, N):
        duration = np.zeros(N, dtype = "int16")
        burnt_percentage = np.zeros(N, dtype = "float32")
        for i in range(N):
            total_time = Engine.simulation(map)
            duration[i] = total_time
            burnt_percentage[i] = Analysis.percentage_of_burnt_area(map)
            map.reset()

        filename_d = input("Please enter the file name for the durations: ") + ".npy"
        filename_b = input("Please enter the file name for the burnt percentages: ") + ".npy"

        foldername = "data"
        path_d = os.path.join(foldername, filename_d)
        path_b = os.path.join(foldername, filename_b)

        np.save(path_d, duration)
        np.save(path_b, duration)

    # not that this method will not work yet, because the map.reset() method
    # returns to the state where no fire is ignited
    
    

