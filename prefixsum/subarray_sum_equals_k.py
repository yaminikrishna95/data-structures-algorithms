def subarray_sum(arr, target):
	count = 0
	prefix_sum = 0
	seen = {0: 1}                # empty prefix sum seen once
	for num in arr:
		prefix_sum += num
		count += seen.get(prefix_sum- target, 0)
		seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

	return count










if __name__ == "__main__":
	arr = [1,2,3]
	target=2
	print(subarray_sum(arr,target))