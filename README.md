# Pythonproject
#python programming project
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False

        for j in range(1, len(p) + 1):
            dp[0][j] = dp[0][j - 1] and (p[j - 1] == '*')

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                dp[i][j] = False
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[len(s)][len(p)]
