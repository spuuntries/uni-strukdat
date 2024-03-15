from lunch import Solution

solve = Solution()
res = [solve.countStudents([1,1,0,0], [0,1,0,1]), solve.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1])]

print("Expected: [0, 3]")
print(f"Results: {res}")
print(f"Passing: {res == [0, 3]}")