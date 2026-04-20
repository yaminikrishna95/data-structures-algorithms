from typing import List


class Solution:

    def LargestOdd_brute(self, nums: str ) -> str:

        ind=-1
        i=0
        for i in range(len(nums)):
            if int(nums[i]) % 2 != 0:
                ind=i
                break
        i=0
        while i<=ind and nums[i]=='0':
            i +=1

        return nums[i:ind+1]





if __name__ == "__main__":
    arr = '504'

    sol = Solution()
    print(sol.LargestOdd_brute(arr))

