

from typing import List


class Solution:

	def prefixsum(self, arr: List[int]) -> List[int]:
		for i in range(1,len(arr)):
				arr[i] = arr[i] + arr[i-1]
		return arr





if __name__ == "__main__":
	arr = [3,1,2,10,1]
	sol = Solution()
	print(sol.prefixsum(arr))
