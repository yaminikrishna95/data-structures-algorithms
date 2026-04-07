from typing import List

class Solution:

    def number_occur_once_better(self, nums: List[int]) -> int:
        maxi=max(arr)
        hash_arr = [0] * (maxi + 1)
        for num in nums:
            hash_arr[num] +=1

        for num in nums:
            if hash_arr[num] == 1:
                return num

    def number_occur_once_optimal(self, nums: List[int]) -> int:
        xor=0
        for num in nums:
            xor ^=num
        return xor




if __name__ == "__main__":
    arr = [1,1,2,3,3]
    sol = Solution()
    print(sol.number_occur_once_better(arr))
    print(sol.number_occur_once_optimal(arr))

