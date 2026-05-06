class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProduct = float('-inf')
        currProductForward = 1
        currProductBackward = 1
        
        n = len(nums)

        for i in range(0, n):
            if currProductForward == 0: currProductForward = 1
            if currProductBackward == 0: currProductBackward = 1
        
            currProductForward *= nums[i]
            currProductBackward *= nums[(n-1)-i]

            maxProduct = max(currProductForward, currProductBackward, maxProduct)


        return maxProduct