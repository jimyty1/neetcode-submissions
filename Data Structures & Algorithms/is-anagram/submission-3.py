class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = [i for i in s]
        lt = [i for i in t]
        ls.sort()
        lt.sort()
        if ls == lt:
            return True
        else:
            return False