
def find_sum_of_n_primes(n):
	import math
	prime_list = [1,2]
	current_val = 3
	while len(prime_list) < n+1:
		cur_val_sqrt = math.sqrt(current_val)
		x = 1
		prime_val = 0
		while prime_list[x] <= cur_val_sqrt:
			if current_val % prime_list[x] == 0:
				x += 1
				prime_val = 1
				break
	        else:
	            x += 1
        if prime_val == 0:
	    	prime_list.append(current_val)
    	current_val += 2
	sum_of_primes = sum(prime_list) 
	print prime_list

find_sum_of_n_primes(100)

