def checkSubarraySum(nums, k):
    remainder_index = {0: -1}
    prefixsum=0
    for i, num in enumerate(nums):
        prefixsum += num
        remainder = prefixsum % k
        if remainder in remainder_index:
            i- remainder_index[remainder] >=2
            return True
        else:
            remainder_index[remainder] = i
    return False



if __name__ == "__main__":
    arr = [23, 2, 6, 4, 7]
    print(checkSubarraySum(arr, 6))  # True