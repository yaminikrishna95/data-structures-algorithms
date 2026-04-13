from typing import List

class Solution:
    max_length = 0
    def LongestSubarray_brute(self, nums: List[int],k:int) -> int:
        max_length = 0
        for i in range(len(nums)):
            current_sum = nums[i]
            for j in range(i+1,len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    max_length = max(max_length,j-i+1)
        return max_length




if __name__ == "__main__":
    arr = [10,5,2,7,1,9]
    k=15
    sol = Solution()
    print(sol.LongestSubarray_brute(arr,k))
    #optimal_ans = sol.rotate_array_optimal(arr)

