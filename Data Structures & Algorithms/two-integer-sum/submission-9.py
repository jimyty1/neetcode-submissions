class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(nums[i]+nums[j] == target and j!= i):
                    return([i,j])