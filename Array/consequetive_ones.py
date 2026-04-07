from typing import List

class Solution:

    def consequetive_brute(self, nums: List[int]) -> int:
        max_length = 0
        for i in range(len(nums)):
            if nums[i] ==1:
                max_length += 1
            elif nums[i]==0:
                if i == len(nums)-1:
                   return max_length
                else:
                   max_length=0
        return max_length








if __name__ == "__main__":
    arr = [1,1,0,1,1,1]
    sol = Solution()
    print(sol.consequetive_brute(arr))
    #optimal_ans = sol.rotate_array_optimal(arr)
