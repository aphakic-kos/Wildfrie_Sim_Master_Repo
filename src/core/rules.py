class Rules:
	#Rules class imposes rules on how the fire should spread
	#from one grid point to another. working with von_neumann
	#neighborhood

	import numpy as np

	def __init__(self, grid):
		self.grid = grid
		#holds number of burning neighbors for the cell
		self.counting_matrix = np.zeros_like(grid)
		self.num_of_rows = grid.shape[0]
		self.num_of_columns = grid.shape[1]
		print("where the fuck is my commit")

	#increments the value of (i, j) cell in counting matrix
	def increment(self, i, j):
		counting_matrix[i][j] +=1

	def spread_probability(self):
		for i in range(num_of_rows):
			for j in range(num_of_columns):
				current_value = grid[i][j]
				match current_value:
					case -1:
						return 0.0
					case 0:
						p = 0.15 * counting_matrix[i][j]
						return p
					case 1:
						p = 0.25 * counting_matrix[i][j]
                                                return p
					case 2:
                                                return 0
					case 3:
						p = 0.1 * counting_matrix[i][j]
                                                return p

	def count_neighbors(self):
		#iteration over rows
		for i in range(num_of_rows):
			#iteration over column of a i-th row
			for j in range(num_of_columns):
				#if the current cell is barier or burning we dont count the neighbors
				#because it doesnt effect their cycle.
				current_value = grid[i][j]
				if current_value == -1 or current_value == 2:
					continue
				#manualy go over boarder cells to prevent indexing errors
				#going over first and last rows
				#going over corners seperately
				if i == 0:
					if j == 0:
						if grid[i][j + 1] == 2:
							increment(i, j)
						if grid[i + 1][j] == 2:
							increment(i, j)
					elif j == num_of_columns - 1:
						if grid[i + 1][j] == 2:
							increment(i, j)
						if grid[i][j - 1] == 2:
							increment(i, j)
					else
						if grid[i][j + 1] == 2:
                                                        increment(i, j)
                                                if grid[i][j - 1] == 2:
                                                        increment(i, j)
                                                if grid[i + 1][j] == 2:
                                                        increment(i, j)
                                                continue
				elif i == num_of_rows - 1:
					if j == 0:
                                                if grid[i][j + 1] == 2:
                                                        increment(i, j)
                                                if grid[i - 1][j] == 2:
                                                        increment(i, j)
                                        elif j == num_of_columns - 1:
                                                if grid[i - 1][j] == 2:
                                                        increment(i, j)
                                                if grid[i][j - 1] == 2:
                                                        increment(i, j)
					else
						if grid[i][j + 1] == 2:
                                                        increment(i, j)
                                                if grid[i][j - 1] == 2:
                                                        increment(i, j)
                                                if grid[i - 1][j] == 2:
                                                        increment(i, j)
                                                continue
				#going over first and last columns
				if j == 0:
					if grid[i][j + 1] == 2:
						increment(i, j)
					if grid[i + 1][j] == 2:
                                                increment(i, j)
					if grid[i - 1][j] == 2:
                                                increment(i, j)
					continue
                                elif j == num_of_columns - 1:
                                        if grid[i - 1][j] == 2:
                                                increment(i, j)
                                        if grid[i][j - 1] == 2:
                                                increment(i, j)
					if grid[i + 1][j] == 2:
                                               	increment(i, j)
					continue
				##########################################
				#everything else
				if grid[i][j - 1] == 2:
					increment(i, j)
				if grid[i][j + 1] == 2:
                                        increment(i, j)
				if grid[i - 1][j] == 2:
                                        increment(i, j)
				if grid[i + 1][j] == 2:
                                        increment(i, j)










