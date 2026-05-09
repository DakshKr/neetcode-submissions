class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s: str, t: str) -> bool:
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
            
        output = []
        for string in strs:
            
            found = False
            for anagram_list in output:
                anagram_list_word = anagram_list[0]
                if isAnagram(string, anagram_list_word):
                    anagram_list.append(string)
                    found = True
                    break;
            if not found:
                output.append([string])
        return output
