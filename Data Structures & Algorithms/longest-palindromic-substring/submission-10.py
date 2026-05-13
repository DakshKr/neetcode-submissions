class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
       
        max_i = -1
        max_j = -1
        max_len = 0
        for index in range(len(s)):
          
            i,j = index, index
            while i > -1 and j < n and s[i] == s[j]:        
                if j - i + 1 > max_len :   
                    max_i = i 
                    max_j = j
                    max_len = j - i + 1 
                i -= 1
                j += 1

            i, j = index, index+1
           
            while i > -1 and j < n and s[i] == s[j]:
                if j - i + 1 > max_len :   
                    max_i = i 
                    max_j = j
                    max_len = j - i + 1 
                i -= 1
                j += 1
                
        return s[max_i: max_j + 1]

