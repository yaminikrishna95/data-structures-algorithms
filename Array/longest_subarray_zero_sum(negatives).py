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

    def LongestSubarray_optimal(self, nums: List[int]) -> int:
        max_length = 0
        firstseen={}
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum in firstseen:
                prev_index=firstseen[prefix_sum]
                max_length = max(max_length, i-prev_index)
            else:
                firstseen[prefix_sum]=i
        return max_length


if __name__ == "__main__":
    arr = [9,-3,3,-1,6,-5]
    k=0
    sol = Solution()
    print(sol.LongestSubarray_brute(arr,k))
    print(sol.LongestSubarray_optimal(arr))

