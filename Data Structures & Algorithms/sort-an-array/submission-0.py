class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def MergeSort(array, start, end):
            if start < end:
                mid = ((end - start ) // 2) + start
                MergeSort(nums, start, mid)
                MergeSort(nums, mid + 1, end)
                Merge(nums, start, mid, end)

        def Merge(nums, start, mid, end):
            l1 = [nums[index] for index in range(start, mid+1)]
            l2 = [nums[index] for index in range(mid+1,end+1)]

            n,m = len(l1), len(l2)
            i,j = 0,0
            k = start
            while i < n and j < m:
                if l1[i] < l2[j]:
                    nums[k] = l1[i]
                    i += 1
                else:
                    nums[k] = l2[j]
                    j += 1
                k += 1
            
            while i < n:
                nums[k] = l1[i]
                i += 1
                k += 1
            while j < m:
                nums[k] =  l2[j] 
                j += 1 
                k += 1

        MergeSort(nums, 0, len(nums) - 1)
        return nums