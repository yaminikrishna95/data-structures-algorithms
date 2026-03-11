class Solution:
	# Function to return the length of the longest valid substring
	# where at most k characters can be replaced to make all characters same
	def characterReplacement(self, s: str, k: int) -> int:

		# Variable to store the max length of valid substring
		max_length = 0

		# Outer loop for starting index of substrings
		for i in range(len(s)):

			# Array to track frequency of characters in window
			freq = [0] * 26

			# Variable to store the frequency of most common character in window
			max_freq = 0

			# Inner loop to go from current start to end of string
			for j in range(i, len(s)):

				# Increment count of current character
				freq[ord(s[j]) - ord('A')] += 1

				# Update max frequency seen so far
				max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])


				# Length of current window
				window_len = j - i + 1


				# Number of characters to replace
				replace = window_len - max_freq


				# Check if we can replace within k
				if replace <= k:
					max_length = max(max_length, window_len)

		return max_length


# Driver code
if __name__ == "__main__":
	sol = Solution()
	s = "AABABBA"
	k = 1
	print(sol.characterReplacement(s, k))
