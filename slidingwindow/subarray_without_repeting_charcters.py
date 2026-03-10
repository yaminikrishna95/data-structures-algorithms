class Solution:
	def longestNonRepeatingSubstring_brute(self, s):
		# Length of the input string
		n = len(s)

		# Variable to store max length
		maxLen = 0

		""" Iterate through all possible 
			starting points of the substring """
		for i in range(n):

			""" Hash to track characters in 
				the current substring window """
			# Assuming extended ASCII characters
			hash_set = [0] * 256

			for j in range(i, n):

				""" If s[j] is already in the
					current substring window """
				if hash_set[ord(s[j])] == 1:
					break

				""" Update the hash_set to mark s[j]
					as present in the current window """
				hash_set[ord(s[j])] = 1

				""" Calculate the length of
					the current substring """
				current_len = j - i + 1

				""" Update maxLen if the current
					substring length is greater """
				maxLen = max(maxLen, current_len)

		# Return the maximum length
		return maxLen

	def longestNonRepeatingSubstring(self, s):
		n = len(s)

		# Assuming all ASCII characters
		HashLen = 256

		""" Hash table to store last
			occurrence of each character """
		hash = [-1] * HashLen

		""" Initialize hash table with
			-1 (indicating no occurrence) """
		for i in range(HashLen):
			hash[i] = -1

		l, r, maxLen = 0, 0, 0
		while r < n:
			""" If current character s[r] 
				is already in the substring """
			if hash[ord(s[r])] != -1:
				""" Move left pointer to the right
					of the last occurrence of s[r] """
				l = max(hash[ord(s[r])] + 1, l)

			# Calculate the current substring length
			current_len = r - l + 1

			# Update maximum length found so far
			maxLen = max(current_len, maxLen)

			""" Store the index of the current
				character in the hash table """
			hash[ord(s[r])] = r

			# Move right pointer to next position
			r += 1

		# Return the maximum length found
		return maxLen


if __name__ == "__main__":
	input_str = "cadbzabcd"

	# Create an instance of Solution class
	sol = Solution()

	length = sol.longestNonRepeatingSubstring_brute(input_str)
	length_optimal = sol.longestNonRepeatingSubstring(input_str)

	# Print the result
	print("Length of longest substring without repeating characters:", length)
	print("Length of longest substring without repeating characters:", length_optimal)