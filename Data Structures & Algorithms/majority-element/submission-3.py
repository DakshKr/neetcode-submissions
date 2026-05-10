class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        freq = len(nums) // 2
        table = {}
        
        for element in nums:
            if element in table:
                table[element] += 1
            else:
                table[element] = 1
        
        for number in table:
            if table[number] >= freq:
                return number
        """
        # morse voting algo
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else: count-=1



        return candidate # only works if we know there exist a majority element 