from collections import deque
from time import time

class RateLimiter:
    def __init__(self, limit: int, interval: int):
        self.limit = limit
        self.interval = interval
        self.requests = deque()

    def is_request_allowed(self) -> bool:
        current_time = time()
        
        while self.requests and self.requests[0] < current_time - self.interval:
            self.requests.popleft()
        
        if len(self.requests) < self.limit:
            self.requests.append(current_time)
            return True
        else:
            return False

rate_limiter = RateLimiter(limit=10, interval=60)

for i in range(15):
    if rate_limiter.is_request_allowed():
        print(f"Request {i} - allowed.")
    else:
        print(f"Request {i} - denied.")
