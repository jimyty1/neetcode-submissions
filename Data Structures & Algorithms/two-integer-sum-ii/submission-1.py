class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = len(nums)-1 -i
            while j > i:
                if(nums[i] + nums[j] < target):
                    i += 1
                if(nums[i] + nums[j] > target):
                    j -= 1
                if(nums[i] + nums[j] == target):
                    return [i+1, j+1]