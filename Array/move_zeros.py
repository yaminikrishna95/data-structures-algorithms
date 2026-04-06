from typing import List


class Solution:
    # As we have used 2 for loops time complexity is o(n**2)
    # space complexity is o(1)

    def movezeros_brute(self, arr: List[int]) -> List[int]:
        n = len(arr)
        temp = [0] * n
        j = 0
        for i in range(n):
            if arr[i] > 0:
                temp[j] = arr[i]
                j += 1
        return temp



    def movezeros_optimal(self, arr: List[int]) -> List[int]:
        j=-1
        # Find the first zero
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        # If no zero found, return
        if j == -1:
            return

        for i in range(j + 1, len(nums)):
            # If current element is non-zero
            if nums[i] != 0:
                # Swap with nums[j]
                nums[i], nums[j] = nums[j], nums[i]
                # Move j to next zero
                j += 1
        return nums






if "__main__" == __name__:
    sol = Solution()
    nums = [1,0,2,0,3,0,4,0,5,1]
    print(sol.movezeros_brute(nums))
    print(sol.movezeros_optimal(nums))


