class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = 0
        _max = nums[0]
        val = 0
        isPos = False

        for i in nums:
            if i >= 0 : isPos = True

            if _max < i:
                _max = i
            
            val = max(val+i, 0)
            output = max(output, val)

        
        if not isPos:
            return _max

        return output
            

