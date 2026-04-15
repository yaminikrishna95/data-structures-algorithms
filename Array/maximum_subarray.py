from typing import List


class Solution:

    def maxSubArray_brute(self, nums: List[int]) -> int:
        res=nums[0]
        for i in range(len(nums)):
            current_sum = nums[i]
            for j in range(i+1, len(nums)):
                current_sum += nums[j]
                res = max(res, current_sum)
        return res

    def maxSubArray_optimal(self, nums: List[int]) -> int:

        res=nums[0]
        max_length=nums[0]
        for i in range(1,len(nums)):
            max_length = max(max_length+nums[i], nums[i])
            res = max(res, max_length)
        return res

if __name__ == "__main__":
    arr = [-2, -4]

    sol = Solution()
    print(sol.maxSubArray_brute(arr))
    print(sol.maxSubArray_optimal(arr))
