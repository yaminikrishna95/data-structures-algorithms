def mergeArrays(arr1, arr2):
	n = len(arr1)
	m = len(arr2)

	# temporary array to store all elements
	# from arr1 and arr2
	merged = [0] * (n + m)

	# copy elements from arr1 and arr2
	# into merged array
	for i in range(n):
		merged[i] = arr1[i]

	for j in range(m):
		merged[n + j] = arr2[j]

	merged.sort()
	return merged




if "__main__" == __name__:
	arr1 = [1, 3, 5, 7]
	arr2 = [2, 4, 6, 8]

	print(mergeArrays(arr1, arr2))

