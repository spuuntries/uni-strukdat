from calls import RecentCounter

recentCounter = RecentCounter()
res = [recentCounter.ping(1),
recentCounter.ping(100),
recentCounter.ping(3001),  
recentCounter.ping(3002)]

print("Inputs: [1, 100, 3001, 3002]")
print("Expected: [1, 2, 3, 3]")
print(f"Results: {res}")
print(f"Passing: {[None] + res == [None, 1, 2, 3, 3]}")
