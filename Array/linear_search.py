from typing import List

class Solution:

    def linear_search(self, nums: List[int],k:int) -> int:
        for i in range(len(nums)):
            if nums[i] == k:
                return i





if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k=3
    sol = Solution()
    print(sol.linear_search(arr,k))
    #optimal_ans = sol.rotate_array_optimal(arr)
