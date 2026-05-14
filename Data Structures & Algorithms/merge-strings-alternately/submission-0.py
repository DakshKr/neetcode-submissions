class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        n, m = len(word1), len(word2)
        
        switch = True
        s = ""
        while i < n and j < m:
            if switch:
                s += word1[i]
                i += 1
                switch = False

            else:
                s += word2[j]
                j += 1
                switch = True

        while i < n:
            s += word1[i]
            i += 1
         
        while j < m:
            s += word2[j]
            j += 1

        return s
        
