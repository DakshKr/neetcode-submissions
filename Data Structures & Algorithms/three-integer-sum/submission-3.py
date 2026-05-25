class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        check = set()
        for i in range(n):
            e1 = nums[i]
            target = -1 * e1
            # now 2 sum problem in array[i+1, n]
            s1 = set()
            for j in range(i+1, n):
                complement = target - nums[j]
                if complement in s1:
                    l1 = [e1, complement, nums[j]]
                    l1.sort()
                    if tuple(l1) not in check:
                        output.append(l1)
                        check.add(tuple(l1))

                s1.add(nums[j])
        return output

