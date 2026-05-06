class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(min(nums))
            nums.remove(min(nums))
        return result
        