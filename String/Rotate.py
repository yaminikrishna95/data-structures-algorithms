from typing import List


class Solution:

    def Rotate_brute(self, nums: str,goal:str ) -> str:

        for i in range(len(nums)):
            final_string=nums[i:]+nums[:i]
            if final_string==goal:
                return True

    def Rotate_optimal(self, nums: str,goal:str ) -> str:

        num=nums+nums
        if goal in num:
            return True


if __name__ == "__main__":
    arr = 'rotation'
    goal='tionrota'
    sol = Solution()
    print(sol.Rotate_brute(arr,goal))
    print(sol.Rotate_optimal(arr, goal))

