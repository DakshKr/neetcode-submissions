class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(  nums[0], nums[1]  )

        prev2a = 0
        prev1a = nums[0]

        prev2b =  0
        prev1b =  nums[1]

        for index in range( 1, n ):
            if index != n-1:
                curr_a = max( prev1a , prev2a + nums[index])
                prev2a = prev1a
                prev1a = curr_a

            if index != 1:
                curr_b = max( prev1b , prev2b + nums[index])
                prev2b = prev1b
                prev1b = curr_b

        return max(prev1a, prev1b)






