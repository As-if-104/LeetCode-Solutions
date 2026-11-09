from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = SortedList(range(k))
        busy = []
        count = [0] * k
        n = len(arrival)

        for i in range(n):
            t = arrival[i]
            while busy and busy[0][0] <= t:
                free.add(heapq.heappop(busy)[1])

            if not free:
                continue

            choice = i % k
            index = free.bisect_left(choice)

            if index == len(free):
                index = 0

            s = free[index]
            free.pop(index)
            count[s] += 1

            heapq.heappush(busy, (t + load[i], s))

        max_count = max(count)

        return [i for i in range(k) if count[i] == max_count]