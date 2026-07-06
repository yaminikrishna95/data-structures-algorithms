class Solution:
    def pivotIndex_brute(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            left_sum = 0
            right_sum = 0

            # Compute left sum for index i
            for j in range(i):
                left_sum += nums[j]

            # Compute right sum for index i
            for j in range(i + 1, n):
                right_sum += nums[j]

            if left_sum == right_sum:
                return arr[i]

        return -1

    def pivotIndex_optimal(self, nums: list[int]) -> int:
        total_sum= sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum -nums[i]
            if right_sum == left_sum:
                return arr[i]
            left_sum += nums[i]



if __name__ == "__main__":
    arr = [1,7,3,6,5,6]
    sol = Solution()
    print(sol.pivotIndex_brute(arr))
    print(sol.pivotIndex_optimal(arr))
