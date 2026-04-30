class Solution:
    def mergeAlternately_brute(self, word1: str, word2: str) -> str:
        merged = []
        left = 0
        while left < len(word1) and left < len(word2):
            merged.append(word1[left])
            merged.append(word2[left])
            left += 1
        while left < len(word1):
            merged.append(word1[left])
            left += 1
        while left < len(word2):
            merged.append(word2[left])
            left += 1

        return "".join(merged)
    def mergeAlternately_optimal(self, word1: str, word2: str) -> str:
        merged = []
        max_len=max(len(word1),len(word2))
        for i in range(max_len):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
        return "".join(merged)

if __name__ == "__main__":
    arr = 'abcd'
    goal = 'pq'

    sol = Solution()
    print(sol.mergeAlternately_brute(arr,goal))
    print(sol.mergeAlternately_optimal(arr, goal))