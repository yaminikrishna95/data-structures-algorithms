from typing import List

class Solution:
    #TC-O(N) SC-O(N)
    def rotate_array_brute(self, nums: List[int]) -> List[int]:
        temp=[]
        element=nums[0]

        for i in range(1,len(nums)):
            temp.append(nums[i])
        temp.append(element)
        return temp

	# TC-O(N) SC-O(1)
    def rotate_array_optimal(self, nums: List[int]) -> List[int]:
        element=nums[0]
        for i in range(1,len(nums)):
            arr[i-1]=arr[i]
        arr[-1]=element
        return nums


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    sol = Solution()
    #brute_ans = sol.rotate_array_brute(arr)
    optimal_ans = sol.rotate_array_optimal(arr)
    #print(brute_ans)
    print(optimal_ans)
