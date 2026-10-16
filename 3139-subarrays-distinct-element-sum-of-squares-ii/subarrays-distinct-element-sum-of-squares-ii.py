class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Lazy segment tree over d[0..n-1]
        # Each node stores: sum of d, sum of d^2, lazy add
        size = 1
        while size < n:
            size <<= 1
        
        sm  = [0] * (2 * size)   # sum of d
        sq  = [0] * (2 * size)   # sum of d^2
        lz  = [0] * (2 * size)   # lazy pending add
        ln  = [0] * (2 * size)   # length of segment (for leaves, 1 if within n else 0)
        
        # Initialize lengths
        for i in range(size):
            ln[size + i] = 1 if i < n else 0
        for i in range(size - 1, 0, -1):
            ln[i] = ln[2*i] + ln[2*i+1]
        
        def apply(node, v):
            # add v to every d in this segment
            # sq += 2*v*sum + v^2 * len   (use OLD sm!)
            sq[node] = (sq[node] + 2 * v * sm[node] + v * v * ln[node]) % MOD
            sm[node] = (sm[node] + v * ln[node]) % MOD
            lz[node] = (lz[node] + v) % MOD
        
        def push(node):
            if lz[node]:
                apply(2*node,     lz[node])
                apply(2*node + 1, lz[node])
                lz[node] = 0
        
        def pull(node):
            sm[node] = (sm[2*node] + sm[2*node+1]) % MOD
            sq[node] = (sq[2*node] + sq[2*node+1]) % MOD
        
        def range_add(node, lo, hi, ql, qr, v):
            if qr < lo or hi < ql:
                return
            if ql <= lo and hi <= qr:
                apply(node, v)
                return
            push(node)
            mid = (lo + hi) // 2
            range_add(2*node,   lo,   mid, ql, qr, v)
            range_add(2*node+1, mid+1, hi, ql, qr, v)
            pull(node)
        
        res = 0
        last = {}
        for r in range(n):
            prev = last.get(nums[r], -1)
            range_add(1, 0, size - 1, prev + 1, r, 1)
            res = (res + sq[1]) % MOD
            last[nums[r]] = r
        
        return res