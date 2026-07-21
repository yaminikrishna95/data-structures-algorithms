def subarray_divisible(arr, target, remainder=None):

	count = 0
	prefix_sum = 0
	seen = {0: 1}                # empty prefix sum seen once
	for num in arr:
		prefix_sum += num
		remainder = prefix_sum % target
		count += seen.get(remainder ,0)
		seen[remainder] = seen.get(remainder, 0) + 1

	return count









if __name__ == "__main__":
	arr = [4,5,0,-2,-3,1]
	target=5
	print(subarray_divisible(arr,target))