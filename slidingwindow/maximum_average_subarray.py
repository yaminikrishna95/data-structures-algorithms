class Solution:
	def MaximumAverage_brute(self, nums: list[int],k) -> int:
		n = len(nums)
		max_sum = float('-inf')
		for i in range(n-k):
			window_sum = 0
			for j in range(i,i+k):
				window_sum += nums[j]
				max_sum = max(max_sum, window_sum)
		return max_sum/k

	def MaximumAverage_optimal(self, nums: list[int],k) -> int:
		n = len(nums)
		window_sum = sum(nums[:k])
		max_sum = window_sum
		for i in range(k,len(nums)):
			window_sum += nums[i] - nums[i-k]
			max_sum = max(max_sum, window_sum)
		return max_sum/k



if __name__ == "__main__":
	arr = [1,12,-5,-6,50,3]
	k=4
	sol = Solution()
	print(sol.MaximumAverage_brute(arr,k))
	print(sol.MaximumAverage_optimal(arr, k))


