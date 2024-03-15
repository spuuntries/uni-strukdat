from win import Solution

solve = Solution()
res = solve.findTheWinner(5, 2)

print("Expected: 3")
print(f"Results: {res}")
print(f"Passing: {res == 3}")