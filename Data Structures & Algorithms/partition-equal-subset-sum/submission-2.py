class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2 == 1: return False

        _sum = _sum//2
        n = len(nums)
        # now i just need to check whether there exist
        # a subsequence with sum = _sum
        dp = {}
        def fn(i, s):
            if s == _sum:
                return True
            elif i == n:
                return False
            elif (i, s) in dp:
                return dp[(i, s)]

            dp[(i,s)] =  fn(i+1, s) or fn(i+1, s + nums[i])
            return dp[(i,s)]


        return fn(0,0)