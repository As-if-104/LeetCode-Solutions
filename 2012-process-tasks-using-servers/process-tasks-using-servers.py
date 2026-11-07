import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []          # (free_time, weight, index)
        ans = []
        time = 0

        for j, dur in enumerate(tasks):
            time = max(time, j)

            # Release servers that are already free (handles gaps between tasks)
            while busy and busy[0][0] <= time:
                ft, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            # If still no free server, jump to next release time
            if not free:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    ft, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (time + dur, w, i))

        return ans