class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s

        max_i = 0
        max_j = -1 

        for index in range(len(s)):
            if max_j - max_i + 1  < 1:
                max_j = index
                max_i = index     
        
            i,j = index-1, index+1
            
            while i > -1 and j < n:
                if s[i] != s[j]:
                    break

                else:
                    len_palindrome = j - i + 1
                    if max_j - max_i +1 < len_palindrome :
                        max_i = i 
                        max_j = j
                    i -= 1
                    j += 1

            i, j = index-1, index+1
            if j<n and s[index] == s[j]:
                if max_j - max_i + 1 < 2 :
                        max_i = index
                        max_j = j


                j += 1
                while i > -1 and j < n:
                    if s[i] != s[j]:
                        break
                    else:
                        len_palindrome2 = j - i + 1
                        if max_j - max_i +1 < len_palindrome2 :
                            max_i = i 
                            max_j = j
                        i -= 1
                        j += 1
                


        return s[max_i: max_j + 1]

