
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = {}

        def dfs(i):
            if i >= len(s): return 1
            if i in dp: return dp[i]

            t = 0
            for word in wordDict:
                if word == s[i:i+len(word)]:
                    t = dfs(i+len(word))
                    if t: break
                    
            dp[i] = t
            return t

        return dfs(0)