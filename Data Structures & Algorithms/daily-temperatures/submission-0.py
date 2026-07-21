class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #brute force
        n = len(temperatures)
        output = [0] * n

        for i, temp in enumerate(temperatures):
            count = 0
            for j in range(i+1, n):
                count += 1
                if temperatures[j] > temp:
                    output[i] = count
                    break
        
        return output
