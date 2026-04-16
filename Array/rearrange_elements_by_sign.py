def rearrange(arr):
    """

    :type arr: object
    """
    pos = []
    neg = []

    # Separate positive and negative numbers
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    posIdx = 0
    negIdx = 0
    i = 0

    # Place positive and negative numbers alternately
    # in the original array
    while posIdx < len(pos) and negIdx < len(neg):
        if i % 2 == 0:
            arr[i] = pos[posIdx]
            posIdx += 1
        else:
            arr[i] = neg[negIdx]
            negIdx += 1
        i += 1

    # Append remaining positive numbers (if any)
    while posIdx < len(pos):
        arr[i] = pos[posIdx]
        posIdx += 1
        i += 1

    # Append remaining negative numbers (if any)
    while negIdx < len(neg):
        arr[i] = neg[negIdx]
        negIdx += 1
        i += 1
    return arr
"""
def rearrange_optimal(arr):

       ans=0*len(arr)
       pos_index = 0
       neg_index = 1


       for i in range(len(arr)):
            if arr[i] < 0:
                # Place negative at odd index
                ans[neg_index] = ans[i]
                neg_index += 2
            else:
                # Place positive at even index
                ans[pos_index] = ans[i]
                pos_index += 2
       return arr
"""
if __name__ == "__main__":
    arr = [1, 2, 3, -4, -1, 4]
    print(rearrange(arr))
    #print(rearrange_optimal(arr))