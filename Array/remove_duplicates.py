from turtle import left
from typing import List


class Solution:

    def removeduplicates_brute(self, nums: List[int]) -> List[int]:

        # Size of the given array
        n = len(nums)
        final_set=set()
        # Iterate through each element of the array
        for i in range(n):
            final_set.add(nums[i])

        return list(final_set)
    def removeduplicates_optimal(self, nums: List[int]) -> List[int]:
        # If list is empty, return 0
        if not nums:
            return 0

        # Pointer for last unique element
        i = 0

        # Traverse list starting from second element
        for j in range(1, len(nums)):
            # If current element is different from last unique one
            if nums[j] != nums[i]:
                # Move pointer forward
                i += 1
                # Place the unique element in next position
                nums[i] = nums[j]

        # i is last index of unique element, count = i + 1
        return i + 1

if __name__ == "__main__":
    arr = [ 1, 1, 1, 2, 2, 2, 3, 3, 4, 4 ]

    # Create an instance of Solution class
    sol = Solution()

    ans = sol.removeduplicates_brute(arr)
    optimal_ans = sol.removeduplicates_optimal(arr)
    print(ans)
    print(optimal_ans)

