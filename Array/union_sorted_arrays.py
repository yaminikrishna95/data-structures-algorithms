from typing import List

class Solution:

    def union_brute(self, nums1: List[int], nums2:List[int]) -> List[int]:
        hash_map = {}
        for i in range(len(nums1)):
            if nums1[i] not in hash_map:
                hash_map[nums1[i]] = i
        for i in range(len(nums2)):
            if nums2[i] not in hash_map:
                hash_map[nums2[i]] = i
        return list(hash_map)
    def union_brute1(self, nums1: List[int], nums2:List[int]) -> List[int]:
        final_set = set()
        for i in range(len(nums1)):
                final_set.add(nums1[i])
        for i in range(len(nums2)):
                final_set.add(nums2[i])
        return list(final_set)

    def union_optimal(self, nums1: List[int], nums2:List[int]) -> List[int]:
        i=0
        j=0
        union=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                if not union or union[-1] != nums1[i]:
                   union.append(nums1[i])
                i+= 1
            elif nums2[j]<nums1[i]:
                if not union or union[-1] != nums2[j]:
                    union.append(nums2[j])

                j +=1

            else:
                # Elements are equal, add once if not duplicate
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
                j += 1
        while i<len(nums1):
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
                i += 1
        while j<len(nums2):
            if not union or union[-1] != arr2[j]:
                union.append(arr2[i])
                j +=1

        return union



if __name__ == "__main__":
    arr1 = [1,2,3,3,4,5]
    arr2 = [1,2,2,3,4]
    sol = Solution()
    print(sol.union_brute(arr1,arr2))
    print(sol.union_brute1(arr1,arr2))
    print(sol.union_optimal(arr1,arr2))
