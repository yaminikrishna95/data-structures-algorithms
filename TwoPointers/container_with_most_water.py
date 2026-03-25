from typing import List

class Solution:

	#two for loops so time complexity is o(n**2)
	#space complexity is o(n) as there is no extra space

	def mostwater_brute(self,arr: List[int]) -> int:
		n = len(arr)
		res=0
		for i in range(n):
			for j in range(i+1,n):
				amount = min(arr[i], arr[j]) * (j - i)
				res = max(amount, res)


		return res
	def mostwater_optimal(self,arr: List[int]) -> int:
		i, j = 0, len(arr) - 1
		res=0
		while i<j:
			amount = min(arr[i], arr[j]) * (j - i)
			res = max(amount, res)
			if arr[i] < arr[j]:
				i += 1
			else:
				j -= 1

		return res




if "__main__" == __name__:
	sol=Solution()
	nums = [1,8,6,2,5,4,8,3,7]
	print(sol.mostwater_brute(nums))
	print(sol.mostwater_optimal(nums))
