def find_square_difference(n):
	one_to_n_list = [i for i in range(1, n+1)]
	sum_of_squares = 0
	for x in one_to_n_list:
		sum_of_squares = sum_of_squares + x**2
		print sum_of_squares
	sum_of_list_squared = (sum(one_to_n_list))**2
	square_differences = sum_of_list_squared - sum_of_squares
	print square_differences

find_square_difference(100)