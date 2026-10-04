class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Evaluates postfix expressions using stack with integer truncation toward zero.

        Time Complexity: O(N) processing each token exactly once.
        Space Complexity: O(N) auxiliary operand stack.
        """
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))  # Truncates toward zero
            else:
                stack.append(int(token))

        return stack[0]
