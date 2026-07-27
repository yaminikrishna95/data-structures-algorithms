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


def findMaxLength_optimal(arr):
	prefix_map = {0: -1}  # handle subarrays starting from index 0
	prefix_sum = 0
	max_len = 0

	for i, num in enumerate(arr):
		# Treat 0 as -1: equal 0s and 1s means sum = 0
		prefix_sum += 1 if num == 1 else -1

		if prefix_sum in prefix_map:
			max_len = max(max_len, i - prefix_map[prefix_sum])
		else:
			prefix_map[prefix_sum] = i

	return max_len



if __name__ == "__main__":
	arr = [0,1,0]
	print(findMaxLength(arr))
	print(findMaxLength_optimal(arr))
