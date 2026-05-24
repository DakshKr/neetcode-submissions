class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        operation = {"+", "C", "D"}

        for op in operations:
            if op not in operation:
                stack.append(int(op))
            elif op == "C":
                stack.pop()
            elif op == "D":
                val = stack[-1] * 2
                stack.append(val)
            elif op == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
            else:
                return "Error"
        
        return sum(stack)
            
        
        