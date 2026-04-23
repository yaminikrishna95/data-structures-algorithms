def checkDuplicates(arr):
	n = len(arr)

	# Create a set to store the unique elements
	st = set()

	# Iterate through each element
	for i in range(n):


		if arr[i] in st:
			return True
		else:
			st.add(arr[i])

	# If no duplicates are found, return false
	return False


if __name__ == "__main__":
	arr = [4, 5, 6, 4]
	print(checkDuplicates(arr))