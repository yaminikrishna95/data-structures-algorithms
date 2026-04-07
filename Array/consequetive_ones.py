from typing import List

class Solution:


    def consequetive_brute(self, nums: List[int]) -> int:
        max_length=0
        current_length=0
        for i in range(len(nums)):
            if nums[i]==1:
                current_length+=1
                max_length = max(current_length,max_length)
            elif nums[i]==0:
                current_length =0
                max_length= max(current_length,max_length)
        return max_length






if __name__ == "__main__":
    arr = [1,1,0,1,1,1]
    sol = Solution()
    print(sol.consequetive_brute(arr))
    #optimal_ans = sol.rotate_array_optimal(arr)
