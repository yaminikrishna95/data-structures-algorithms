from typing import List

class Solution:
    #TC-O(N) SC-O(N)
    def move_array_brute(self, nums: List[int]) -> List[int]:
        temp=nums[0:2]
        for i in range(2,len(nums)):
            arr[i-2]=arr[i]
        arr[-2:]=temp
        return arr

    def move_array_optimal(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    sol = Solution()
    brute_ans = sol.move_array_brute(arr)
    optimal_ans = sol.move_array_optimal(arr)
    print(brute_ans)
    #print(optimal_ans)
