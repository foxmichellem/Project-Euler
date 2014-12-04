def find_triangular_num_divisors(number_of_divsors):
	#start with 0
	n = 2
	#start divisors at 0
	divisors = 1
	#run the loop until a number with parameter number of divisors is found
	while divisors < number_of_divsors - 1:
		#reset the divisors to 0
		#find the triangular number
		tri_num = (n * (n + 1)/2)
		#we will start checking the divisors of the triangular number
		i = 2
		divisors = 1
		#We check everything less than the square root and if it is divisble, add 2 (one for each divisor)
		while i*i < tri_num:
			if tri_num % i == 0:
				divisors += 2
			i += 1
		n += 1
		print divisors, tri_num
find_triangular_num_divisors(500)