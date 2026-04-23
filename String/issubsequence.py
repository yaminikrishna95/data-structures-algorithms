from typing import List


class Solution:

    def Subsequence_brute(self, nums: str,goal: str  ) -> str:
        tmp=[]
        for i in range(len(goal)):
            for j in range(len(nums)):
                if goal[i]in nums:
                    tmp.append(goal[i])
        print(tmp)






if __name__ == "__main__":
    arr = 'abc'
    goal = 'ahbgde'

    sol = Solution()
    print(sol.Subsequence_brute(arr,goal))

