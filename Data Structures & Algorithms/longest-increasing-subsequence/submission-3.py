class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       
        n = len(nums)

        dp = {}

        def fn(i, prev):
            if i == n:
                return 0
            
            if (i, prev) in dp:
                return dp[(i, prev)]
         
            
            if prev == -1 or nums[i] > nums[prev]:
                dp[(i, prev)] = max(fn(i+1, prev), 1 + fn(i+1, i))
                return  dp[(i, prev)] 

            dp[(i, prev)]  = 0 + fn(i+1, prev)
            return  dp[(i, prev)] 
        
        return fn(0, -1)

