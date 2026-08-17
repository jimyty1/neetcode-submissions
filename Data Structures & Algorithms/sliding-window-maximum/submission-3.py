class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        window = {}

        for i in range(k):
            window[nums[i]] = 1 + window.get(nums[i], 0)

        largest = max(window)
        res.append(largest)

        for r in range(k, len(nums)):
            window[nums[l]] -= 1

            if window[nums[l]] == 0:
                del window[nums[l]]

            l += 1

            window[nums[r]] = 1 + window.get(nums[r], 0)

            largest = max(window)
            res.append(largest)

        return res