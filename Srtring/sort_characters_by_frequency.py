from collections import Counter
import heapq

class Solution:

	def chars_frequency_brute(self, s: str) -> bool:
		# Check if strings are of the same length
		char_counts = Counter(s)

		sorted_chars = sorted(char_counts.items(), key=lambda item: -item[1],reverse=True)


		result = ''.join(char * freq for char, freq in sorted_chars)

		return result

	def chars_frequency_optimal(self, s: str) -> bool:
		# Check if strings are of the same length
		freq = [0] * 128

		# Count frequency of each character in str1
		for char in s:
			freq[ord(char)] += 1
		minH=[]
		for i in range(128):
			if freq[i] > 0:
				heapq.heappush(minH, [freq[i], chr(i)])

		ans = ""
		while minH:
			count, ch = heapq.heappop(minH)
			ans += ch * count

		return ans

sol = Solution()

print(sol.chars_frequency_brute("ABC"))
print(sol.chars_frequency_optimal("ABC"))