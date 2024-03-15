class RecentCounter:
    def __init__(self):
        self.queue = []
    def ping(self, t: int) -> int:
        self.queue.append(t)
        res = []
        for it in reversed(self.queue):
            if it >= t - 3000 and it <= t: res.append(it)
            else: break
        return len(res)