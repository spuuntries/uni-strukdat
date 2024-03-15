from browser import BrowserHistory

target = [None,None,None,None,"facebook.com","google.com","facebook.com",None,"linkedin.com","google.com","leetcode.com"]
browserHistory = BrowserHistory("leetcode.com")
history = [
browserHistory.visit("google.com"),
browserHistory.visit("facebook.com"),    
browserHistory.visit("youtube.com"),
browserHistory.back(1),                
browserHistory.back(1),          
browserHistory.forward(1),               
browserHistory.visit("linkedin.com"),
browserHistory.forward(2),    
browserHistory.back(2),               
browserHistory.back(7)
]         

print("Expected: " + ",".join(map(lambda x: str(x), target)))
print("Results: " + ",".join(map(lambda x: str(x), [None] + history)))
print("Passing: " + str([None] + history == target))