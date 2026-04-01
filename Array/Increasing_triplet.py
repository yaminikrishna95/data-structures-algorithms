
from typing import List

from traitlets import Bool


class Solution:

    def tripletsequence_brute(self, nums: List[int]) -> Bool:
        n=len(nums)

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] < nums[j] < nums[k]:
                        return True

        return False


    def tripletsequence_optimal(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num < first:
               first = num
            elif num < second:
                second = num
            else:
                return True

        return False


if __name__ == "__main__":
    arr = [5,4,3,2,1]

    # Create an instance of Solution class
    sol = Solution()

    brute_ans = sol.tripletsequence_brute(arr)
    optimal_ans = sol.tripletsequence_optimal(arr)
    print(brute_ans)
    print(optimal_ans)