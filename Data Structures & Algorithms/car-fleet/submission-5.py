import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        l1 = sorted(zip(position, speed), reverse=True)

        stack = []
        for pos, sp in l1:
            stack.append((target-pos)/sp)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
