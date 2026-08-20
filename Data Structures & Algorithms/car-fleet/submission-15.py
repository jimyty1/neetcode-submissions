class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car= []
        for i in range(len(position)):
            car.append([position[i],speed[i]])
        car = sorted(car, key = lambda x:x[0])
        stack = []
        for i in range(len(car) -1, -1,-1):
            stack.append((target-car[i][0])/car[i][1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)