from typing import List

class Solution:

    def LongestSubarray_brute(self, nums: List[int],k:int) -> int:
        max_length = 0
        for i in range(len(nums)):
            current_sum = nums[i]
            for j in range(i+1,len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    max_length = max(max_length,j-i+1)
        return max_length

    def LongestSubarray_optimal(self, nums: List[int],k:int) -> int:
        pass


if __name__ == "__main__":
    arr = [1,2,3,1,1,1]
    k=3
    sol = Solution()
    print(sol.LongestSubarray_brute(arr,k))
    print(sol.LongestSubarray_optimal(arr,k))

