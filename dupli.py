def dupli(A):
	"""Function takes a list and for every duplicate it removes one"""
	list_new = []
	for i in range(len(A)-1):
		if A[i] != A[i+1]:
			list_new.append(A[i])
	list_new.append(A[len(A)-1])
	return list_new
print (dupli([5,5,1,3,6,6,7]))