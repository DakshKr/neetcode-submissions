class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for index, element in enumerate(nums):
            required_number = target - element 
            if required_number in hash_table:
                return [ hash_table[required_number], index ]
            
            else:
                hash_table[element] = index
        
        return [-1, -1]
