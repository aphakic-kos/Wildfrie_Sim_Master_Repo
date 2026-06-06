# PROJECT WILDFIRE ENGINE
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import numpy as np
import random as rand
from board import MapCreator, Map
from rules import Rules

# Engine class. Design of the engine
# class is primitive. There is no
# neccessary atribute for this class.
# Only static methods are defined in
# the class.
class Engine:
    
    def __init__(self):
        pass

    # static method running the simulation
    # for N times.
    # usage: Engine.simulation(map, N)
    def simulation(map, N):
        for i in range(N):
            Engine.change_state(map)

    # static method running the simlation
    # for once. Also used as a helper method,
    # one can also have public access to the
    # method.
    # usage Engine.change_state(map)
    def change_state(map):
        rows = map.num_rows
        cols = map.num_cols
        rules = Rules(map)
        new_data = np.zeros([rows, cols], dtype="int16")
        for row in range(rows):
            for col in range(cols):
                new_cell_state = rules.new_cell(row, col)
                new_data[row, col] = new_cell_state
        map.curr_map = new_data


    # Additional method, for visualisation
    # Currently contains bug, and only displays
    # the final stage. 
    def run_wildfire_animation(map, frames=100, interval=200):
        fig, ax = plt.subplots(figsize=(8, 8))
        cmap = ListedColormap(['#1f77b4', '#d7c49e', '#2ca02c', '#d62728', '#555555'])

        # Adjusted vmin/vmax to match a 0-4 state range cleanly
        im = ax.imshow(map.curr_map, cmap=cmap, vmin=0, vmax=4)

        def update(frame):
            Engine.change_state(map)
            im.set_array(map.curr_map)
            return [im]

        ani = animation.FuncAnimation(
            fig,
            update,
            frames=frames,
            interval=interval,
            blit=True,
            repeat=True)

        plt.show()
    

    
