from typing import List

class Solution:
   # tc-o(nlog n) sc -o(1)
    def largest_brute(self, nums: List[int]) -> int:
       nums.sort()
       return nums[-1]

   # tc-o(nlog n) sc -o(1)
    def largest_optimal(self, arr: List[int]) -> int:
        largest_element=0
        for num in arr:
            largest_element = max(num,largest_element)
        return largest_element


if __name__ == "__main__":
    arr = [10,7,1,8,6,2,9]
    sol = Solution()
    brute_ans = sol.largest_brute(arr)
    optimal_ans = sol.largest_brute(arr)
    print(brute_ans)
    print(optimal_ans)