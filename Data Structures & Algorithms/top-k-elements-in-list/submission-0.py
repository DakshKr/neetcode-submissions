class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        n = len(nums)
        freqBucket = [[] for _ in range(n+1)]

        for key in freq:
            f = freq[key]
            freqBucket[f].append(key)
        
        output = []
        idx = n-1
        while k > 0:
            if not freqBucket[idx]:
                idx -= 1
                continue
            
            k-=1
            val = freqBucket[idx].pop()
            output.append(val)
        
        return output
            