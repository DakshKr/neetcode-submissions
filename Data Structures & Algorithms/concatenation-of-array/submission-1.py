class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length * 2

        for i in range(0, 2 * length):
            ans[i] = nums[ i % length ]
        
        return ans