from typing import List


class Solution:

    def ReversePalindromeCheck_brute(self, nums: str ) -> str:
        reversed_string=nums[-1::-1]
        return reversed_string

    def ReversePalindromeCheck_optimal(self, nums: str ) -> str:
        left, right = 0, len(nums) - 1
        num=list(nums)
        while left < right:
                  num[left], num[right] = num[right], num[left]
                  left += 1
                  right -= 1
        return "".join(num)











if __name__ == "__main__":
    arr = 'welcome to the jungle'

    sol = Solution()
    print(sol.ReversePalindromeCheck_brute(arr))
    print(sol.ReversePalindromeCheck_optimal(arr))

