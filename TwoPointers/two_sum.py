from typing import List

class Solution:
   #As we have used 2 for loops time complexity is o(n**2)
   #space complexity is o(1)

	def twoSum_brute(self,arr: List[int], target: int) -> List[int]:
		n = len(arr)
		for i in range(n):
			for j in range(i + 1, n):
				sum = arr[i] + arr[j]
				if sum == target:
					return [i + 1, j + 1]
		# no pair sum with given target
		return [-1, -1]

   #As we have one loop time complexity is o(n)
   #space complexity is o(1)
	def twoSum_optimal(self,arr: List[int], target: int) -> List[int]:
		i, j = 0, len(arr) - 1
		while i<j:
			sum = arr[i] + arr[j]
			if sum == target:
				return [i+1, j+1]
			if sum > target:
				j-=1
			elif sum < target:
				i+=1
		return [-1, -1]





if "__main__" == __name__:
	sol=Solution()
	nums = [2,7,11, 15]
	target = 9
	print(sol.twoSum_brute(nums, target))
	print(sol.twoSum_optimal(nums, target))