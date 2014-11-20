#This is how you will move the numbers through the list
def find_highest_consec_product(thousand_digit_num):
	thous_dig_num_string = str(thousand_digit_num)
	indices_list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
	max_product = 1

	for i in range(len(thous_dig_num_string)-12):
		product = 1
		for i in indices_list:
			product *= int(thous_dig_num_string[i])
		print product
		if product > max_product:
			max_product = product
		x = indices_list[12]
		x += 1
		indices_list.append(x)
		del indices_list[0]

	print max_product
