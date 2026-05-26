class Rules:
	#Rules class imposes rules on how the fire should spread
	#from one grid point to another. working with von_neumann
	#neighborhood

	from board.py import BARRIER, GROUND, VEGETATION, BURNING, BURNT
	import numpy as np

	def __init__(self, grid):
		self.grid = grid
		#holds number of burning neighbors for the cell
		self.counting_matrix = np.zeros_like(grid)
		self.num_of_rows = grid.shape[0]
		self.num_of_columns = grid.shape[1]

	#increments the value of (i, j) cell in counting matrix
	def increment(self, row, column):
		self.counting_matrix[row][column] +=1

	#depending on the number of neighbors and cell type, returns corresponding probability. (numbers can change  (-_-) )
	def spread_probability(self, row, column):
		current_value = self.grid[row][column]
		match current_value:
			case BARRIER:
				return 0.0
			case GROUND:
				p = 0.15 * self.counting_matrix[row][column]
				return p
			case VEGETATION:
				p = 0.25 * self.counting_matrix[row][column]
                                return p
			case BURNING:
                                return 0
			case BURNT:
				p = 0.1 * self.counting_matrix[row][column]
                                return p

	#builds the matrix of probability of burning (i, j) cell
	def probability(self):
		P = np.zeros_like(self.grid)
		for row in range(self.num_of_rows):
			for column in range(sef.num_of_columns):
				P[row][column] = spread_probability(row, column)

	#if the cell is barier or burning returns true.
	#if the current cell is barier or burning we dont count the neighbors
	#because it doesnt effect their cycle.
	def skippable_cell(self, value):
		if value == BARRIER or value == BURNING
			return True

	#counts neighbors for first row
	def first_row(self, i, j):
		#corner (0,0)
		if j == 0:
			if self.grid[i][j + 1] == 2:
				increment(i, j)
			if self.grid[i + 1][j] == 2:
				increment(i, j)
		#corner (0, last)
		elif j == self.num_of_columns - 1:
			if self.grid[i + 1][j] == 2:
				increment(i, j)
			if self.grid[i][j - 1] == 2:
				increment(i, j)
		#everything other than corners in first row
		else
			if self.grid[i][j + 1] == 2:
                                increment(i, j)
                       	if self.grid[i][j - 1] == 2:
                                increment(i, j)
                      	if self.grid[i + 1][j] == 2:
                                increment(i, j)

	#counts neighbors for last row
	def last_row(self, i, j):
		#corner (last, 0)
		if j == 0:
                	if self.grid[i][j + 1] == 2:
                       		increment(i, j)
                        if self.grid[i - 1][j] == 2:
                               	increment(i, j)
		#corner (last, last)
               	elif j == self.num_of_columns - 1:
                        if self.grid[i - 1][j] == 2:
                                increment(i, j)
                       	if self.grid[i][j - 1] == 2:
                                increment(i, j)
		#everything other than corners in last row
		else
			if self.grid[i][j + 1] == 2:
                                increment(i, j)
                        if self.grid[i][j - 1] == 2:
                                increment(i, j)
                        if self.grid[i - 1][j] == 2:
                                increment(i, j)

	#everything other than corners in first column
	def first_column(self, i, j):
		if self.grid[i][j + 1] == 2:
			increment(i, j)
		if self.grid[i + 1][j] == 2:
                       	increment(i, j)
		if self.grid[i - 1][j] == 2:
                        increment(i, j)

	#everything other than corners in last column
	def last_column(self, i, j):
		if self.grid[i - 1][j] == 2:
                	increment(i, j)
             	if self.grid[i][j - 1] == 2:
                        increment(i, j)
		if self.grid[i + 1][j] == 2:
                        increment(i, j)

	#everything other than boundry cells
	def interior(self, i, j):
		if self.grid[i][j - 1] == 2:
			increment(i, j)
		if self.grid[i][j + 1] == 2:
                        increment(i, j)
		if self.grid[i - 1][j] == 2:
                        increment(i, j)
		if self.grid[i + 1][j] == 2:
                       	increment(i, j)

	def count_neighbors(self):
		#iteration over rows
		for i in range(self.num_of_rows):
			#iteration over column of a i-th row
			for j in range(self.num_of_columns):
				current_value = self.grid[i][j]
				if skippable_cell(current_value):
					continue
				#manualy go over boarder cells to prevent indexing errors
				#top and bottom row
				if i == 0:
					first_row(i, j)
					continue
				elif i == self.num_of_rows - 1:
					last_row(i, j)
					continue
				#left and right columns
				if j == 0:
					first_column(i, j)
					continue
                                elif j == self.num_of_columns - 1:
                                        last_column(i, j)
					continue
				#everything else
				else
					interior(i, j)











