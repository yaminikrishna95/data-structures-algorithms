def countBinarySubstrings_bruteforce(s: str) -> int:
    n = len(s)
    count = 0

    for i in range(n):
        zeros = 0
        ones = 0
        transitions = 0

        for j in range(i, n):
            if s[j] == '0':
                zeros += 1
            else:
                ones += 1
            if j > i and s[j]!=s[j-1]:
                transitions += 1
            if zeros ==ones and transitions == 1:
                count += 1
    print(count)
def countBinarySubstrings_optimal(s: str) -> int:
    count=0
    curr=1
    prev=0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr+=1
        else:
            count +=min(prev,curr)
            prev=curr
            curr=1
    count +=min(prev,curr)
    print(count)



if __name__ == "__main__":
    s = "00110011"
    countBinarySubstrings_bruteforce(s)
    countBinarySubstrings_optimal(s)
