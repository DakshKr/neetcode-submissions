class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length_nums = len(nums)
        
        i,j, k = 0,0,0
        while i < length_nums:
            if nums[i] == val:
                while j < length_nums - 1:
                    j += 1
                    if nums[j] != val:
                        k += 1
                        nums[i], nums[j] = nums[j], val
                        break
            else:
                k+=1
            i += 1
            j = max(j, i)
        
        

        return k

