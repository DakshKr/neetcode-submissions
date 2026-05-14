class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        if find the biggest palindrome with 
            x as the center
        
            abc...zxz....cba  
            then total palindrom with x as centre = (len(palindrome) - 1 / 2) + 1

            even length
            abccba then we have len(palindrome) / 2
        """
        n = len(s)

        count = 0
        for index in range(len(s)):
          
            i,j = index, index
            while i > -1 and j < n and s[i] == s[j]:        
                count += 1
                i -= 1
                j += 1

            i, j = index, index+1
           
            while i > -1 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
                
        return count

