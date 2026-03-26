from typing import List

class Solution:
   #As we have used 2 for loops time complexity is o(n**3)
   #space complexity is o(1)

	def threeSum_brute(self,arr: List[int], target: int) -> List[int]:
		n = len(arr)
		st = set()
		for i in range(n):
			for j in range(i + 1, n):
				for k in range(j + 1, n):
					sum = arr[i] + arr[j]+ arr[k]
					if sum == 0:
						triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
						st.add(triplet)
		return [list(triplet) for triplet in st]


	def threeSum_better(self,arr: List[int], target: int) -> List[int]:
		n = len(arr)
		st = set()
		for i in range(n):
			hashset = set()
			for j in range(i + 1, n):

					third = -(arr[i] + arr[j])
					if third in hashset:
						triplet = tuple(sorted([arr[i], arr[j], third]))

						st.add(triplet)
					hashset.add(third)
		return [list(triplet) for triplet in st]

	def threeSum_optimal(self,arr: List[int], target: int) -> List[int]:
		n = len(arr)
		arr.sort()
		ans=[]
		for i in range(n):

			if i > 0 and arr[i] == arr[i - 1]:
				continue
			left=i+1
			right=n-1
			while left < right:
				total = arr[i] + arr[left] + arr[right]
				if total ==0:
					ans.append([arr[i], arr[left], arr[right]])
					left += 1
					right -=1
					while left < right and arr[left] == arr[left - 1]:
						left +=1
					while left < right and arr[right] == arr[right + 1]:
						right -=1
				elif total < 0:
					left += 1
				else:
					right -= 1
		return ans



















if "__main__" == __name__:
	sol=Solution()
	nums = [-1,0,1,2,-1,-4]
	target = 0

	print(sol.threeSum_optimal(nums, target))


