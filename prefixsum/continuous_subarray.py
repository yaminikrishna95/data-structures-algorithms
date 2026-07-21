def findMaxLength(arr):
	max_len = 0
	for i in range(len(arr)):
		zeros = 0
		ones = 0
		for j in range(i, len(arr)):
			if arr[j] == 0:
				zeros += 1
			else:
				ones += 1
			if zeros == ones:
				max_len = max(max_len, j - i + 1)
	return max_len


if __name__ == "__main__":
	arr = [0,1,1,1,1,1,1,0,0,0]
	print(findMaxLength(arr))