from typing import List


class Solution:

    def twosum_brute(self, nums: List[int], k: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == k:
                    return [i, j]

    def twosum_better(self, nums: List[int], target:int) -> list[int] | None:

        firstseen = {}
        for i, num in enumerate(nums):
            if num not in firstseen:
                complement = target - num
                if complement in firstseen:
                    return [firstseen[complement], i]
                else:
                    firstseen[num] = i
        return [-1, -1]
    def twosum_optimal(self, nums: List[int],k:int):
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                return [left, right]
        return	[-1, -1]

if __name__ == "__main__":
    arr = [2, 6, 5, 8, 11]
    k = 14
    sol = Solution()
    print(sol.twosum_brute(arr, k))
    print(sol.twosum_better(arr, k))
    print(sol.twosum_optimal(arr,k))
