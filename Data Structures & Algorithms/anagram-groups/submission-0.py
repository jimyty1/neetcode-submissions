class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        anagrams = []
        for i in strs:  
            if "".join(sorted(i)) in myMap:
                myMap["".join(sorted(i))].append(i)
            else:
                myMap["".join(sorted(i))]= [i]
        for i in myMap.values():
            anagrams.append(i)
        return anagrams

            