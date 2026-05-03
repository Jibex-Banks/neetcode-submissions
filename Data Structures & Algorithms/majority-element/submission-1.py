class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        elements = dict()
        uniq = set(nums)
        result = 0
        
        for i in uniq:
            cnt = nums.count(i)
            elements[i] = cnt     
        
        for i in uniq:
            if elements.get(i) > n/2:
                result = i
        return result