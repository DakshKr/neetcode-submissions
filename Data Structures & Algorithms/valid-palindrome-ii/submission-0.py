class Solution:
    def validPalindrome(self, s: str) -> bool:
        # case 1: if palindrome return true
        # case 2: if we reach some s[i] != s[j]
                #( removing s[i] and check if its a palindrome
                                    #or
                # removing s[j] and check if its a palindrome   ) reutnr true?

        def is_palindrome(str1):
            return str1 == str1[::-1]


        i = 0
        j = len(s)-1

        while i<j:
            if s[i] != s[j]:
                return is_palindrome(s[i:j]) or is_palindrome(s[i+1:j+1])

            i+=1
            j-=1

                
        return True
