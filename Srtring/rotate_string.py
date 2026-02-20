class Solution:


		def rotateString_brute(self, s: str, goal: str) -> bool:
			# Check if strings are of the same length
			if len(s) != len(goal):
				return False
			for i in range(len(s)):
				rotated = s[i:] + s[:i]
				if rotated == goal:
					return True

			return False
		def rotateString_optimal(self, s: str, goal: str) -> bool:
			if len(s) != len(goal):
				return False
			double_string=s+ s
			return goal in double_string





# Test case
sol = Solution()

print(sol.rotateString_brute("rotation", "tionrota"))
print(sol.rotateString_optimal("rotation", "tionrota"))