def fibonacci(n):
	"""Function gives a list of the prime numbers from 0 to n"""
	a = 0
	b = 1
	fibonacci_sequence =[a, b]
	while b < n:
		a, b = b, a+b
		fibonacci_sequence.append(b)
	return fibonacci_sequence
print fibonacci(50)