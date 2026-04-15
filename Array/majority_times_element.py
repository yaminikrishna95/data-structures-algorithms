from typing import List

class Solution:

    def majorityElement_brute(self, nums: List[int]) -> int:
        max_length = 0
        n=len(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                   max_length += 1
            if max_length >= n/2:
                return nums[i]
        return -1

    def majorityElement_optimal(self, nums: List[int]) -> int:
        count=0
        candidate=0
        for i in range(len(nums)):
            if count==0:
                count +=1
                candidate=nums[i]
            elif nums[i]==candidate:
                count+=1
            else:
                count-=1
        count=0
        for num in nums:
            if candidate==num:
                count+=1
        if count >= len(nums)/2:
            return candidate
        return -1





if __name__ == "__main__":
    arr = [5, 5, 2, 5, 3, 5, 1]

    sol = Solution()
    print(sol.majorityElement_brute(arr))
    print(sol.majorityElement_optimal(arr))

