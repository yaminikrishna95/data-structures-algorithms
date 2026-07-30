class Solution:
	def Anagrams_brute(self, s:str,p:str) -> list[int]:
		result=[]
		s_len=len(s)
		p_len=len(p)
		if s_len < p_len:
			return result
		sorted_p=sorted(p)
		for i in range(s_len -p_len+1):
			window=sorted(s[i:i+p_len])
			if window==sorted_p:
				result.append(i)
		return result

	def Anagrams_optimal(self, s:str,p:str) -> list[int]:
		result=[]
		s_len=len(s)
		p_len=len(p)
		if s_len < p_len:
			return result
		p_count = [0] * 26
		window_count = [0] * 26
		print(p_count)
		print(window_count)
		for i in range(p_len):
			p_count[ord(p[i])-ord('a')]+=1
			window_count[ord(s[i])-ord('a')]+=1
		print(p_count)
		print(window_count)
		matches = sum(1 for i in range(26) if p_count[i] == window_count[i])
		print(matches)
		if matches == 26:
			result.append(0)
		print(result)
		for i in range(p_len, s_len):
			in_char = ord(s[i]) - ord('a')
			out_char = ord(s[i - p_len]) - ord('a')
			print(in_char, out_char)

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
				result.append(i - p_len + 1)

			return result














if __name__ == "__main__":
	s="cbae"
	p="abc"
	sol = Solution()
	#print(sol.Anagrams_brute(s,p))
	print(sol.Anagrams_optimal(s, p))



