from typing import List

from scipy.stats import false_discovery_control


class Solution:

    def Isomorphic_brute(self, nums: str,goal:str ) -> bool:

        s1=sorted(nums)
        s2=sorted(goal)
        if s1!=s2:
            return False
        return True

    def Isomorphic_optimal(self, nums: str,goal:str ) -> str:
        if len(nums)!=len(goal):
            return False
        charCount={}
        for ch in nums:
            charCount[ch]= charCount.get(ch,0)+1
        print(charCount)
        for ch in goal:
            charCount[ch]= charCount.get(ch,0)-1
        print(charCount)
        for value in charCount.values():
            if value !=0:
                return False
        return True
    def Isomorphic_optimal1(self, nums: str,goal:str ) -> str:
        if len(nums)!=len(goal):
            return False
        charCount=[0]*26
        for ch in nums:
            charCount[ord(ch) - ord('a')] += 1
        print(charCount)
        for ch in goal:
            charCount[ord(ch) - ord('a')] -= 1
        print(charCount)
        for value in charCount:
            if value !=0:
                return False
        return True

if __name__ == "__main__":
    arr = 'geeks'
    goal='ksgee'
    sol = Solution()
    print(sol.Isomorphic_brute(arr,goal))
    print(sol.Isomorphic_optimal(arr, goal))
    print(sol.Isomorphic_optimal1(arr, goal))

