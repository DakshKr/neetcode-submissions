class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       
        n = len(nums)

        dp = {}

        def fn(i, prev):
            if i == n:
                return 0
            
            if (i, prev) in dp:
                return dp[(i, prev)]
         
            _len = 0 + fn(i+1, prev)
            if prev == -1 or nums[i] > nums[prev]:
                _len = max(_len, 1 + fn(i+1, i))
            
            dp[(i, prev)] = _len

            return _len
        
        return fn(0, -1)

