class Solution:
    def fourSum(self, nums: List[int], _target: int) -> List[List[int]]:
        nums.sort()

        def ksum(l1, target, k):
            out = []
            if k > 2:
                # Established context: Your outer loop duplicate check is validated.
                dup_check = set()
                for i in range(len(l1)):
                    if l1[i] in dup_check:
                        continue
                    dup_check.add(l1[i])
                    newTarget = target - l1[i]
                    out_rec = ksum(l1[i+1:], newTarget, k-1) 
                    for ans in out_rec:
                        ans.insert(0, l1[i])
                    out += out_rec
            else:
                # The Final Transformation: Set-based 2Sum with duplicate omission
                set1 = set()
                for index in range(len(l1)):
                    newTarget = target - l1[index]
                    if newTarget in set1:
                        # Because the array is sorted, duplicates arrive sequentially.
                        # We jump directly to checking the last appended pair's right-hand value.
                        if not out or out[-1][1] != l1[index]:
                            out.append([newTarget, l1[index]])
                    set1.add(l1[index])
            return out
            
        return ksum(nums, _target, 4)