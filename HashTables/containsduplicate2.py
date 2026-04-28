from typing import Any


def containsNearbyDuplicate(arr, k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):   # start from i+1
            if arr[i] == arr[j] and j - i <= k:
                return True
    return False
def containsNearbyDuplicate_optimal(arr, k):
    hashmap ={}

    for i, val in enumerate(arr):
        if arr[i] in hashmap and i - hashmap[val] <= k:
                return True
        hashmap[val] = i

    return False




if __name__ == "__main__":
    arr = [1,2,3,1]
    k=3
    print(containsNearbyDuplicate(arr,k))
    print(containsNearbyDuplicate_optimal(arr, k))