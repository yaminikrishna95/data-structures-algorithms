
from typing import List

from traitlets import Bool


class Solution:

    def productarray_brute(self, nums: List[int]) -> List[int]:
        n=len(nums)

        final_list=[]
        for i in range(n):
            product=1
            for j in range(n):
                if i != j:
                    product*=nums[j]
            final_list.append(product)
        return final_list


    def productarray_optimal(self, nums: List[int]) -> List[int]:
        pass





if __name__ == "__main__":
    arr = [1,2,3,4]

    # Create an instance of Solution class
    sol = Solution()

    brute_ans = sol.productarray_brute(arr)
    optimal_ans = sol.productarray_optimal(arr)
    print(brute_ans)
    #print(optimal_ans)