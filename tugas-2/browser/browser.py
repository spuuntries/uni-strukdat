class BrowserHistory:
    def __init__(self, homepage: str):
        # NOTE: Uses an implicit stack structure (LIFO)
        self.pages = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        # NOTE: This keeps LIFO by clearing out everything past current index 
        # and setting url as the latest
        self.pages = self.pages[:self.curr + 1 if self.curr + 1 else 1] + [url]
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = self.curr - steps if self.curr - steps > 0 else 0
        return self.pages[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = self.curr + steps if self.curr + steps < len(self.pages) else len(self.pages) - 1
        return self.pages[self.curr]