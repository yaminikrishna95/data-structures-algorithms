from collections import defaultdict
def count_pairs_brute(nums):
    count_pairs=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if i < j:
                if nums[i] == nums[j]:
                   count_pairs +=1
    return count_pairs

def count_pairs_optimal(arr):
    mp = defaultdict(int)

    count = 0
    for num in arr:
        print("num:",num)
        count += mp[num]
        print(count)
        mp[num] += 1
        print(mp)


    return count


# Driver Program
arr = [1, 2,3,1,1,3]
print(count_pairs_optimal(arr))
#print(count_pairs_brute(arr))