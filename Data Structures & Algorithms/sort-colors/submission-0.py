class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force approach
        freqs = [0, 0, 0]   # 5 4 3   0 0 0 0 0 1 1 1 1 2 2 2 

        for num in nums:
            freqs[num] += 1
        
        index = 0
        for value, freq in enumerate(freqs):
            while freq > 0 :
                nums[index] = value
                index += 1
                freq -= 1
            