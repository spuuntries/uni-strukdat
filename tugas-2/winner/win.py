class Solution():
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        i = 0
        while len(friends) > 1:
            remove_index = (i + k - 1) % len(friends)
            friends.pop(remove_index)
            i = remove_index
        return friends[0]