from typing import List


class Solution:
	# As we have used 2 for loops time complexity is o(n**2)
	# space complexity is o(1)

	def movezeros_brute(self, arr: List[int]) -> List[int]:
		n = len(arr)
		temp = [0] * n
		j = 0
		for i in range(n):
			if arr[i] > 0:
				temp[j] = arr[i]
				j += 1
		return temp


	def movezeros_optimal(self, arr: List[int]) -> List[int]:
		pass







if "__main__" == __name__:
	sol = Solution()
	nums = [1,0,2,0,3,0,4,0,5,1]
	print(sol.movezeros_brute(nums))
	#print(sol.movezeros_optimal(nums))


