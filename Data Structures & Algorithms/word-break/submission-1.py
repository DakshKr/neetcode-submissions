class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = {}

        def fn(i):
            if i == n: return True

            if i in dp: return dp[i]

            status = False
            for word in wordDict:

                if len(word) > n - i:
                    continue


                temp = i
                isMatched = True
                for char in word:
                    if s[temp] != char:
                        isMatched = False
                        break
                    temp += 1
                
                if isMatched:
                    status = status or fn(temp)

            dp[i] = status
            return status

        return fn(0)
                    



        