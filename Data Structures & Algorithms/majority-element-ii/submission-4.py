class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = None
        count1 = 0

        cand2 = None
        count2 = 0

        for num in nums:
            if count1 == 0 and cand2 != num:
                cand1 = num
                count1 = 1
            elif count2 == 0 and cand1 != num:
                cand2 = num
                count2 = 1
            elif cand1 == num:
                count1 +=1
            elif cand2 == num:
                count2 +=1

            else:
                count1 -= 1
                count2 -= 1

        #checking where elements in this set have freq > n/3
        s1 = {cand1, cand2}
        n = len(nums)
        print(s1)
        req_freq = n//3
        l1 = []

        for element in s1:
            i = 0
            for num in nums:
                if num == element:
                    i +=1
            if i <= req_freq:
                l1.append(element)


        for to_del in l1:
            s1.remove(to_del)

        return list(s1)