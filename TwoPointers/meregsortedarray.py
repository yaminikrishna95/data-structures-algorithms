from typing import List

class Solution:
    def mergeArray_brute(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged_array=[]

        for i in range(len(nums1)):
            if nums1[i] > 0:
               merged_array.append(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] > 0:
               merged_array.append(nums2[j])
        merged_array.sort()
        return merged_array

    def mergeArray_better(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        merged=[]
        i=j=0
        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1

        # copy remaining elements from arr1
        while i < n:
            merged.append(arr1[i])
            i += 1

        # copy remaining elements from arr2
        while j < m:
            merged.append(arr2[j])
            j += 1
        return merged






if __name__ == "__main__":
    nums1= [4,5,6,0,0,0]
    nums2=[1,2,3]
    m=3
    n=3

    sol = Solution()
    print(sol.mergeArray_brute(nums1,m,  nums2,n))
    print(sol.mergeArray_better(nums1, m, nums2, n))
    print(sol.mergeArray_optimal(nums1, m, nums2, n))