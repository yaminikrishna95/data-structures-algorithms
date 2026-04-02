from typing import List

class Solution:
   # tc-o(nlog n) sc -o(1)
    def largest_brute(self, nums: List[int]) -> list[int]:
       nums.sort()
       return nums[1],nums[-2]

   # tc-o(nlog n) sc -o(1)
    def largest_optimal(self, arr: List[int]) -> int:
        max_element=0
        min_element=arr[0]
        for i in range(1,len(arr)):
            max_element = max(arr[i],max_element)
            min_element = min(arr[i],min_element)
        print(max_element,min_element)



if __name__ == "__main__":
    arr = [10,7,1,8,6,2,9]
    sol = Solution()
    brute_ans = sol.largest_brute(arr)
    optimal_ans = sol.largest_optimal(arr)
    print(brute_ans)
    #print(optimal_ans)