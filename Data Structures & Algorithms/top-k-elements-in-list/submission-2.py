class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        output = []
        for i in nums:
            if i in myMap:
                myMap[i] += 1
            else:
                myMap[i] = 1
        for j in range(k):
            maxK = max(myMap, key = myMap.get)
            print(myMap[maxK])
            output.append(maxK)
            myMap[maxK] = 0
            print(myMap[maxK])
        return output
        