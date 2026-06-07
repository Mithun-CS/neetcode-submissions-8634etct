from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        cooldown_queue = []
        
        while max_heap or cooldown_queue:
            time += 1
            
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt < 0:
                    cooldown_queue.append((cnt, time + n))
            
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(max_heap, cooldown_queue.pop(0)[0])
                
        return time
        