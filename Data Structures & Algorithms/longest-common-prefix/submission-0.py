class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)

        if length == 1:
            return strs[0]
    
        lcp = strs[0]
        for index in range(1, length):
            current_word = strs[index]
            length_current_word = len(current_word)
            length_lcp = len(lcp)

            if length_current_word < length_lcp:
                lcp = lcp[ : length_current_word]
                length_lcp = length_current_word

            counter = length_lcp - 1
            while counter >= 0:
                if current_word[counter] != lcp[counter]:
                    lcp = lcp[:counter]
                counter -= 1

        return lcp

