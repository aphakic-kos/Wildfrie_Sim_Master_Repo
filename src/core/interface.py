from numpy.lib import row_stack
from board import Map, MapCreator
import numpy as np
import os

#-------------------------------------------------------------
# constants
BARRIER = -1      # No fire spreads on the bariers
GROUND = 0        # ground/empty cell
VEGETATION = 1    # vegetation/fuel cell
BURNING = 2       # burning cell
BURNT = 3         # burnt cell
CHOICES = [BARRIER,
           GROUND,
           VEGETATION,
           BURNING,
           BURNT]


VALID_MAPS = ["random",
              "trailed",
              "custom"]

#------------------------------------------------------
# Interface class uses Map, MapCreator, and Rules
# classes to create objects and then uses the
# engine class to create a simulation
class Interface:
    map_x_size = 0
    map_y_size = 0
    map_type = ""
    
    def __init__(self):
        self.map = Interface.__create_map()

    # Initial method acting on the class to adjust
    # shape of the map. The input values can be
    # only positive integers. Number of rows in the
    # will represent the x size of the map, and number
    # of columns will represent the y size of the map
    # usage Interface.get_map_shape()
    def get_map_shape():
        rows, cols = 0, 0
        print("Enter the shape of the map.")
        while not Interface.__valid_shape(rows, cols):
            cols = int(input("Enter x size of the map: "))
            rows = int(input("Enter y size of the map: "))

            if Interface.__valid_shape(rows, cols):
                break
            else:
                print("Invalid input. Try again.")
            
        Interface.map_x_size = cols
        Interface.map_y_size = rows

    # Helper method to check the valid input of the shape 
    def __valid_shape(rows, cols):
        cond_1 = rows > 0
        cond_2 = cols > 0
        return (cond_1 & cond_2)

    # Initial method acting on the class to determine the
    # type of the map. There are three possible maps:
    # random, trailed and custom map.
    # usage Interface.get_map_type()
    def get_map_type():
        type = ""
        print("Enter the type of the map.")
        while type not in VALID_MAPS:
            type = input("Enter type of the map: ")

            if type in VALID_MAPS:
                break
            else:
                print("Invalid input. Try again.")
        Interface.map_type = type

    # This method records the commands to create the
    # custom map. The result is the N x 3 matrix, where
    # N is the number of the commands. First element in
    # the row is y coordinate (row index), second element
    # is the x coordinate (column index), and the third
    # element is the value.
    def get_commands():
        commands = []
        while(True):
            row = Interface.__get_row()
            col = Interface.__get_col()
            value = Interface.__get_value()
            commands.append([row, col, value])

            answer = input("Do you want to continue entering data\n(type NO to finish)? ")
            if (answer == "NO"):
                break
        return commands

    # helper method to get row index (y coordinate)
    def __get_row():
        row = -1
        while(True):
            row = int(input("Enter y coordinate: "))
            if(row < 0 or row > Interface.map_y_size - 1):
                print("Invalid input. Try again.")
            else:
                break
        return row

    # helper method to get column index (x coordinate)
    def __get_col():
        col = -1
        while(True):
            col = int(input("Enter x coordinate: "))
            if (col < 0 or col > Interface.map_y_size - 1):
                print("Invalid input. Try again.")
            else:
                break
        return col

    # helper method to get value on the position
    def __get_value():
        value = -1
        while(True):
            value = int(input("Enter the state: "))
            if value not in CHOICES:
                print("Invalid input. Try again.")
            elif (value == BURNING or value == BURNT):
                print("Initialy there is no fire, and no place burnt. Try again.")
            else:
                break
        return value

    # helper method to initialize the map in the __init__()
    def __create_map():
        map_prototype = MapCreator(Interface.map_y_size,
                         Interface.map_x_size)
        if Interface.map_type == "random":
            map_prototype.random_map()
        elif Interface.map_type == "trailed":
            num_vegetation = int(input("Enter Number of vegetation to be seeded: "))
            map_prototype.trailed_map(num_vegetation)
        else:
            map_prototype.custom_map(Interface.get_commands())

        path = "boards"
        filename = input("Enter the board name: ")
        filename = filename + ".npy"
        map_prototype.save_data(path, filename)

        map = Map(os.path.join(path, filename))
        return map


Interface.get_map_shape()
Interface.get_map_type()

I = Interface()
print(I.map.curr_map)


