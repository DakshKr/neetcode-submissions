class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output = 0
        i = 0
        k = 0
        n = len(nums)
        while i < n:
            output+=1
            j = i+1
            while j < n:
                if nums[j] != nums[i]:
                    break
                j+=1
            nums[k] = nums[i]
            k+=1
            i = j     
                
        return output