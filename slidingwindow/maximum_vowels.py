def maxVowels_brute(s: str, k: int) -> int:
	vowels = set('aeiou')
	n = len(s)
	max_count = 0

	# Try every starting index for a window of length k
	for i in range(n - k + 1):
		count = 0
		# Count vowels in the substring s[i : i+k]
		for j in range(i, i + k):
			if s[j] in vowels:
				count += 1
		max_count = max(max_count, count)

	return max_count


def maxVowels_optimal(s: str, k: int) -> int:
	vowels = set('aeiou')

	# Count vowels in the first window s[0:k]
	count = 0
	for i in range(k):
		if s[i] in vowels:
			count += 1

	max_count = count

	# Slide the window across the rest of the string
	for i in range(k, len(s)):
		# Add the new character entering on the right
		if s[i] in vowels:
			count += 1
		# Remove the character leaving on the left
		if s[i - k] in vowels:
			count -= 1

		max_count = max(max_count, count)

	return max_count






if __name__ == "__main__":
	s="abciiidef"
	p=3
	print(maxVowels_brute(s, p))
	print(maxVowels_optimal(s, p))