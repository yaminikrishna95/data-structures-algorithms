from typing import List

class Solution:

    def stock_brute(self, nums: List[int]) -> int:
        n=len(nums)
        min_price=float('inf')
        max_profit=0
        for i in range(n):
            for j in range(i+1,n):
                  min_price=min(min_price,nums[i])
                  max_profit=max(max_profit,nums[j])



        return min_price


if __name__ == "__main__":
    arr = [10,7,1,8,6,2,9]
    sol = Solution()
    ans = sol.stock_brute(arr)
    print(ans)