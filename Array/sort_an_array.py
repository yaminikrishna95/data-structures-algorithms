from typing import List


class Solution:

    def sortZeroOneTwo_brute(self, nums: List[int]) -> None:
        zeros = ones = twos = 0

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        index = 0

        for _ in range(zeros):
            nums[index] = 0
            index += 1

        for _ in range(ones):
            nums[index] = 1
            index += 1

        for _ in range(twos):
            nums[index] = 2
            index += 1
        return nums

    def sortZeroOneTwo_optimal(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif nums[i] == 1:
                 mid += 1
            else:
                arr[high], arr[mid] = arr[mid], arr[high]
                high -= 1
        return nums


if __name__ == "__main__":
    arr = [1, 0, 1, 0, 2, 2]

    sol = Solution()
    print(sol.sortZeroOneTwo_brute(arr))
    print(sol.sortZeroOneTwo_optimal(arr))
