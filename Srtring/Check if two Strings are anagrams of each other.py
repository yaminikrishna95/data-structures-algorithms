class Solution:

	def check_anagram_brute(self, s: str, goal: str) -> bool:
		# Check if strings are of the same length
		if len(s) != len(goal):
			return False

		if sorted(s) == sorted(goal):
			return True  # Strings are anagrams if sorted versions are equal

		return False

	def check_anagram_optimal(self, s: str, goal: str) -> bool:
		if len(s) != len(goal):
			return False
		charCount = {}
		for ch in s:
			charCount[ch] = charCount.get(ch, 0) + 1

		for ch in goal:
			charCount[ch] = charCount.get(ch, 0) - 1

		for value in charCount.values():
			if value != 0:
				return False

		return True
	def check_anagram_optimal2(self, s: str, goal: str) -> bool:
		if len(s) != len(goal):
			return False
		freq = [0] * 26

		# Count frequency of each character in str1
		for char in s:
			freq[ord(char) - ord('A')] += 1  # Increment frequency for each character in str1

		# Decrement frequency for each character in str2
		for char in goal:
			freq[ord(char) - ord('A')] -= 1  # Decrement frequency for each character in str2

		# Check if all frequencies are zero, meaning both strings have the same characters
		for count in freq:
			if count != 0:
				return False  # If any frequency is non-zero, they are not anagrams

		return True  # The strings are anagrams if all frequencies are zero




# Test case
sol = Solution()

print(sol.check_anagram_brute("ABC", "CBA"))
print(sol.check_anagram_optimal("ABC", "CBA"))
print(sol.check_anagram_optimal2("ABC", "CBA"))
