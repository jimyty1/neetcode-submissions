class Solution:
    def evaluate(self, left, right, op):
        match op:
            case "+":
                return left + right
            case "-":
                return left - right
            case "*":
                return left * right
            case "/":
                return int(left / right)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                right = stack.pop()
                left = stack.pop()

                result = self.evaluate(left, right, token)
                stack.append(result)

            else:
                stack.append(int(token))

        return stack[0]