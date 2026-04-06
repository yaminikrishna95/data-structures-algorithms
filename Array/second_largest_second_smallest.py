from typing import List

class Solution:
   # tc-o(nlog n) sc -o(1)
    def largest_brute(self, nums: List[int]) -> list[int]:
       nums.sort()
       return nums[1],nums[-2]

   # tc-o(nlog n) sc -o(1)
    def largest_better(self, arr: List[int]) -> list[int]:
        max_element=0
        min_element=arr[0]
        second_largest=float('-inf')
        second_smallest=float('inf')
        for i in range(1,len(arr)):
            max_element = max(arr[i],max_element)
            min_element = min(arr[i],min_element)
        for i in range(len(arr)):
            if arr[i] > second_largest and arr[i] != max_element:
               second_largest = arr[i]
            if arr[i] < second_smallest and arr[i] != min_element:
                second_smallest = arr[i]
        return [second_smallest,second_largest]







if __name__ == "__main__":
    arr = [10,7,1,8,6,2,9]
    sol = Solution()
    brute_ans = sol.largest_brute(arr)
    optimal_ans = sol.largest_better(arr)
    print(brute_ans)
    print(optimal_ans)