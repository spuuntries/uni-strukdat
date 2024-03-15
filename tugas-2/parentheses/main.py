from parent import Solution

solve = Solution()

print('Test = "(()())(())" -> "()()()"')
print(f'Passing: {solve.removeOuterParentheses("(()())(())") == "()()()"}')