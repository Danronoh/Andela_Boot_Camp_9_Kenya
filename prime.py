def get_prime_numbers_upto(n):
	"""Function returns the range of prime numbers from 0 to n"""
	prime_list = [2,3]
	start_at = 4
	while True:
		for number in range(2, (start_at//2) +  1):
			if not start_at % number:
				break
		else:
			prime_list.append(start_at)
		start_at += 1
		if start_at == n + 1  :
			break
	return str(prime_list)
print get_prime_numbers_upto(29)