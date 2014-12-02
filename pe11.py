#create a test matrix
M = []
M.append([1,2,3,4,5,6,7,8])
M.append([2,45,1,62,62,6,6,1])
M.append([52,7,5,62,4,23,5,7])
M.append([3,5,62,3,57,67,4,2])
M.append([2,62,6,4,2,9,8,0])


#function to find largest product
#matrix is a list of the rows in the matrix
#assumes that each inner list is the same length
def find_largest_product(matrix):
	#find the largest product for left to right
	max_product = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])-3):
			lr_product = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]
			if lr_product > max_product:
				max_product = lr_product

	
	#find the largest product for up and down
	for i in range(len(matrix[0])):
		for j in range(len(matrix)-3):
			ud_product = matrix[j][i] * matrix[j+1][i] * matrix[j+2][i] * matrix[j+3][i]
			if ud_product > max_product:
				max_product = ud_product

	#find the largest product for l-to-r diagonal
	for i in range(len(matrix)-3):
		for j in range(len(matrix[0]) - 3):
			lr_diagonal_product = M[i][j] * M[i+1][j+1] * M[i+2][j+2] * M[i*3][j+3]
			if lr_diagonal_product > max_product:
				max_product = lr_diagonal_product

	#find the largest product for r-to-l diagonal
	for i in range(len(matrix)-3):
		for j in range(len(matrix[0])-1,2,-1):
			rl_diagonal_product = M[i][j] * M[i+1][j-1] * M[i+2][j-2] * M[i+3][j-3]
			if rl_diagonal_product > max_product:
				max_product = rl_diagonal_product
	print max_product

find_largest_product(M)
