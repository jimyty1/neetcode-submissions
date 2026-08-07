class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set(nums)
        count = 0
        print(temp)
        for num in temp:
            if num-1 not in temp:
                length =1
                while(num+length) in temp:
                    length +=1
                count = max(length, count)
        return count