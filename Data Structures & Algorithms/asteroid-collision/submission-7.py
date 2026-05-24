class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
            elif stack[-1] > 0 and ast < 0:
                status = True
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(ast):
                        stack.pop()
                    elif stack[-1] == abs(ast):
                        stack.pop()
                        status = False
                        break
                    else:
                        status = False
                        break
                if status:
                    stack.append(ast)
            else:
                stack.append(ast)           
        return stack