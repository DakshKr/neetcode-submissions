class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if 0 < mid < n-1 and nums[mid-1] >= nums[mid] <= nums[mid+1]:
                return nums[mid]
            
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid -1
        
            return min(nums)