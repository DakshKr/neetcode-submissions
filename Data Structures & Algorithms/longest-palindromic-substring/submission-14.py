class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        maxLen = 0
        mi = -1
        mj = -1

        n = len(s)

        for i in range(n):

            l, r = i, i
            newLen = 0
            while  l>=0 and r<n and  s[l] == s[r]:
                r += 1
                l -= 1
            if r - l + 1 > maxLen:
                maxLen = r-l+1
                mi = l
                mj = r
            
            l,r = i, i + 1
            while  l>=0 and r<n and  s[l] == s[r]:
                r += 1
                l -= 1
            if r - l + 1 > maxLen:
                maxLen = r-l+1
                mi = l
                mj = r
        
        print(mi,mj)
        return s[mi+1: mj]
    


