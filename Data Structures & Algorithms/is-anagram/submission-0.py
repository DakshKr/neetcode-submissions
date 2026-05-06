class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force method i can think of 
        s_length = len(s)
        t_length = len(t)

        if s_length != t_length:
            return False


        hash_table = {}
        for i in s:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1
        
        for j in t:
            if j not in hash_table or hash_table[j] == 0:
                return False
            hash_table[j] -= 1
        
        return True
        