from typing import List


class Solution:

    def threesum_brute(self, nums: List[int]) -> List[int]:
        final_list=set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                       if nums[i] + nums[j] +nums[k] == 0:
                           triplet=tuple(sorted([nums[i],nums[j],nums[k]]))
                           final_list.add(triplet)
        return list(final_list)



if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    print(sol.threesum_brute(arr))
