# Python3 program to implement
# the above approach

# Function to find the missing elements
def printMissingElements(arr, N):

    b = [0] * (arr[N - 1] + 1)
    print(b)

    # Make b[i]=1 if i is present
    # in the array
    for i in range(N):

        # If the element is present
        # make b[arr[i]]=1
        b[arr[i]] = 1
    print(b)

    # Print the indices where b[i]=0
    for i in range(arr[0], arr[N - 1] + 1):
        if(b[i] == 0):
            print(i, end = " ")

# Driver Code

# Given array arr[]
arr = [ 6, 7, 10, 11, 13 ]

N = len(arr)
print(N)

# Function call
printMissingElements(arr, N)