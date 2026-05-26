#imports:
from board import Map
import numpy as np
import random

#constants
BARRIER = -1
GROUND = 0
VEGETATION = 1
BURNING = 2
BURNT = 3

class Variables:
    BARRIER = -1
    GROUND = 0
    VEGETATION = 1
    BURNING = 2
    BURNT = 3


GROUND_BURNING_PROBABILITY = 0.15
VEGETATION_BURNING_PROBABILITY = 0.25
LONG_LASTING_FIRE_PROBABILITY = 0.15
BURNT_REIGNITING_PROBABILITY = 0.1

class CountingMatrix:
    #CountingMatrix is subclass of Rules class which holds the methods associated with
    #building the counting matrix.

    def __init__(self):
        Grid = Map()
        self.grid = Grid.curr_map
        #holds number of burning neighbors for the cell
        self.counting_matrix = np.zeros_like(grid)
        self.num_of_rows = grid.shape[0]
        self.num_of_columns = grid.shape[1]

    #counting matrix method returns the number of burning neighbors for grid as a matrix
    def __count_neighbors(self):
        #iteration over rows
        for i in range(self.num_of_rows):
            #iteration over column of a i-th row
            for j in range(self.num_of_columns):
                current_value = self.grid[i][j]
                if self.__skippable_cell(current_value):
                    continue
                #manualy go over boarder cells to prevent indexing errors
                #top and bottom row
                if i == 0:
                    self.__first_row(i, j)
                    continue
                elif i == self.num_of_rows - 1:
                    self.__last_row(i, j)
                    continue
                #left and right columns
                if j == 0:
                    self.__first_column(i, j)
                    continue
                elif j == self.num_of_columns - 1:
                    self.__last_column(i, j)
                    continue
                #everything else
                else:
                    self.__interior(i, j)

    #if the cell is barier or burning returns true.
    #if the current cell is barier or burning we dont count the neighbors
    #because it doesnt effect their cycle.
    def __skippable_cell(self, value):
        if value == BARRIER or value == BURNING:
            return True

    #increments the value of (i, j) cell in counting matrix
    def __increment(self, row, column):
        self.counting_matrix[row][column] += 1

    #counts neighbors for first row
    def __first_row(self, i, j):
        #corner (0,0)
        if j == 0:
            if self.grid[i][j + 1] == BURNING:
                self.__increment(i, j)
            if self.grid[i + 1][j] == BURNING:
                self.__increment(i, j)
        #corner (0, last)
        elif j == self.num_of_columns - 1:
            if self.grid[i + 1][j] == BURNING:
                self.__increment(i, j)
            if self.grid[i][j - 1] == BURNING:
                self.__increment(i, j)
        #everything other than corners in first row
        else:
            if self.grid[i][j + 1] == BURNING:
                self.__increment(i, j)
            if self.grid[i][j - 1] == BURNING:
                self.__increment(i, j)
            if self.grid[i + 1][j] == BURNING:
                self.__increment(i, j)

    #counts neighbors for last row
    def __last_row(self, i, j):
        #corner (last, 0)
        if j == 0:
            if self.grid[i][j + 1] == BURNING:
                self.__increment(i, j)
            if self.grid[i - 1][j] == BURNING:
                self.__increment(i, j)
        #corner (last, last)
        elif j == self.num_of_columns - 1:
            if self.grid[i - 1][j] == BURNING:
                self.__increment(i, j)
            if self.grid[i][j - 1] == BURNING:
                self.__increment(i, j)
        #everything other than corners in last row
        else:
            if self.grid[i][j + 1] == BURNING:
                self.__increment(i, j)
            if self.grid[i][j - 1] == BURNING:
                self.__increment(i, j)
            if self.grid[i - 1][j] == BURNING:
                self.__increment(i, j)

    #everything other than corners in first column
    def __first_column(self, i, j):
        if self.grid[i][j + 1] == BURNING:
            self.__increment(i, j)
        if self.grid[i + 1][j] == BURNING:
            self.__increment(i, j)
        if self.grid[i - 1][j] == BURNING:
            self.__increment(i, j)

    #everything other than corners in last column
    def __last_column(self, i, j):
        if self.grid[i - 1][j] == BURNING:
            self.__increment(i, j)
        if self.grid[i][j - 1] == BURNING:
            self.__increment(i, j)
        if self.grid[i + 1][j] == BURNING:
            self.__increment(i, j)

    #everything other than boundry cells
    def __interior(self, i, j):
        if self.grid[i][j - 1] == BURNING:
            self.__increment(i, j)
        if self.grid[i][j + 1] == BURNING:
            self.__increment(i, j)
        if self.grid[i - 1][j] == BURNING:
            self.__increment(i, j)
        if self.grid[i + 1][j] == BURNING:
            self.__increment(i, j)

class Rules:
    #Rules class imposes rules on how the fire should spread
    #from one grid point to another. working with von_neumann
    #neighborhood

    def __init__(self):
        Grid = Map()
        CountingMatrix = CountingMatrix()
        self.counting_matrix = CountingMatrix.counting_matrix
        self.grid = Grid.curr_map

    #depending on the number of neighbors and cell type, returns corresponding probability. (numbers can change  (-_-) )
    def __spread_probability(self, row, column):
        current_value = self.grid[row][column]
        match current_value:
            case Variables.BARRIER:
                return 0.0
            case Variables.GROUND:
                p = GROUND_BURNING_PROBABILITY * self.counting_matrix[row][column]
                return p
            case Variables.VEGETATION:
                p = VEGETATION_BURNING_PROBABILITY * self.counting_matrix[row][column]
                return p
            case Variables.BURNING:
                #lets fire burning in current cell continue with some probability.
                if random.random() < LONG_LASTING_FIRE_PROBABILITY:
                    return 1.0
                return 0.0
            case Variables.BURNT:
                p = BURNT_REIGNITING_PROBABILITY * self.counting_matrix[row][column]
                return p

    #--------------Function that will be used from outside-------------------------#

    #returns value of cell (row, column) to build new grid
    def new_cell(self, row, column):
        current_value = self.grid[row][column]
        match current_value:
            case Variables.BARRIER:
                return BARRIER
            case Variables.GROUND:
                if random.random() < self.__spread_probability(row, column):
                    return BURNING
                return GROUND
            case Variables.VEGETATION:
                if random.random() < self.__spread_probability(row, column):
                    return BURNING
                return VEGETATION
            case Variables.BURNING:
                #lets fire burning in current cell continue with some probability.
                #return long_lasting_fire()
                return BURNT
            case Variables.BURNT:
                if random.random() < self.__spread_probability(row, column):
                    return BURNING
                return BURNT

    #-----------------------------------------------------------------------------#
