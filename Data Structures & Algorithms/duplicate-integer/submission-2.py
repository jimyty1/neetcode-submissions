class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i,j in enumerate(nums):
            if j in nums[i+1:len(nums)]:
                return True
        return False