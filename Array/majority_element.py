from typing import List


class Solution:
    # Function to find the majority element in an array
    def majorityElement_brute(self, nums: List[int]) -> int:

        # Size of the given array
        n = len(nums)

        # Iterate through each element of the array
        for i in range(n):

            # Counter to count occurrences of nums[i]
            cnt = 0

            # Count the frequency of nums[i] in the array
            for j in range(n):
                if nums[j] == nums[i]:
                    cnt += 1

            # Check if frequency of nums[i] is greater than n/2
            if cnt > (n // 2):
                # Return the majority element
                return nums[i]

        # Return -1 if no majority element is found
        return -1

    def majorityElement_better(self, nums: List[int]) -> int:

        # Size of the given array
        n = len(nums)
        mp={}


        # Iterate through each element of the array
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        for num,count in mp.items():
            if count > n//2:
                return num
        return -1

    def majorityElement_optimal(self, nums: List[int]) -> int:

        # Size of the given array
        n = len(nums)
        element=0
        count=0
        for i in range(n):
            if count==0:
               count=1
               element=nums[i]
            elif element==nums[i]:
                count+=1
            else:
                count-=1
        cnt1 = nums.count(element)
        if cnt1 > n//2:
            return element

        return -1









if __name__ == "__main__":
    arr = [2, 2, 1, 1, 1, 2, 2]

    # Create an instance of Solution class
    sol = Solution()

    ans = sol.majorityElement_brute(arr)
    better_ans = sol.majorityElement_better(arr)
    optimal_ans = sol.majorityElement_optimal(arr)

    # Print the majority element found
    print("The majority element is:", ans)
    print("The majority element is:", better_ans)
    print("The majority element is:", optimal_ans)

