class Solution:
	def PermutationString_brute(self, s:str,p:str) -> bool:

		s_len=len(s)
		p_len=len(p)
		if s_len < p_len:
			return -1
		sorted_p=sorted(p)
		for i in range(s_len -p_len+1):
			window=sorted(s[i:i+p_len])
			if window==sorted_p:
			   return True

"""
	def PermutationString_optimal(self, s:str,p:str) -> bool:
		s_len=len(s)
		p_len=len(p)
		if s_len < p_len:
			return False

		p_count = [0] * 26
		window_count = [0] * 26
		for i in range(p_len):
			p_count[ord(p[i])-ord('a')]+=1
			window_count[ord(s[i])-ord('a')]+=1
		matches = sum(1 for i in range(26) if p_count[i] == window_count[i])
		if matches == 26:
			return True
		for i in range(p_len, s_len):
			in_char = ord(s[i]) - ord('a')

			out_char = ord(s[i - p_len]) - ord('a')
			window_count[in_char] += 1
			if window_count[in_char] == p_count[in_char]:
				matches += 1
			elif window_count[in_char] == p_count[in_char] + 1:
				matches -= 1

			window_count[out_char] -= 1
			if window_count[out_char] == p_count[out_char]:
				matches += 1
			elif window_count[out_char] == p_count[out_char] - 1:
				matches -= 1
			if matches == 26:
				return True
			else:
				return False

"""
if __name__ == "__main__":
	s="eidboaooo"
	p="ab"
	sol = Solution()
	print(sol.PermutationString_brute(s,p))
	#print(sol.PermutationString_optimal(s, p))



