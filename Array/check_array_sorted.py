from typing import List

class Solution:
   # tc-o(nlog n) sc -o(1)
    def sortarray_brute(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    return False
        return True

   # tc-o(nlog n) sc -o(1)
    def sortarray_optimal(self, arr: List[int]) -> int:
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True


if __name__ == "__main__":
    arr = [5,4,3,2,1]
    sol = Solution()
    brute_ans = sol.sortarray_brute(arr)
    optimal_ans = sol.sortarray_optimal(arr)
    print(brute_ans)
    print(optimal_ans)