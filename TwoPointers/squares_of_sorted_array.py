
from typing import List

class Solution:
    def sortedSquares_brute(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
            print(nums[i])
        nums.sort()
        return nums

if __name__ == "__main__":
    arr = [-4,-1,0,3,10]

    sol = Solution()
    print(sol.sortedSquares_brute(arr))
    #print(sol.sortedSquares_optimal(arr, goal))