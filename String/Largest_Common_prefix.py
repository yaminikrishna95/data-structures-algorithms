class Solution:
    # Returns the longest common prefix from a list of strings
    def longestCommonPrefix(self, strs):
        strs.sort()
        first = strs[0]
        last = strs[-1]
        min_length = min(len(first), len(last))
        i=0
        while  i < min_length and first[i]==last[i]:
            i += 1
        return first[:i]

# Run the function with sample input
if __name__ == "__main__":
    # Create an instance of Solution
    solution = Solution()

    # Input list of strings
    input_strs = ["interview", "internet", "internal", "interval"]

    # Call the method to find prefix
    result = solution.longestCommonPrefix(input_strs)

    # Print the result
    print("Longest Common Prefix:", result)
