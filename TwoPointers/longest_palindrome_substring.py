"""def longestPalindrome(s):
    n = len(s)
    longest = ""

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]

            if substring == substring[::-1]:
                if len(substring) > len(longest):
                    longest = substring

    return longest
"""


def longestPalindrome(s):
    if not s:
        return ""

    start = end = 0

    def expand(left, right):
        print(left, right)
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        print(left, right)
        return right - left - 1

    for i in range(len(s)):
        # Odd length palindrome
        len1 = expand(i, i)
        print(len1)

        # Even length palindrome
        len2 = expand(i, i + 1)
        print(len2)


        max_len = max(len1, len2)
        print(max_len)
        if max_len > end - start + 1:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


if __name__ == "__main__":
    arr = "bab"
    print(longestPalindrome(arr))

