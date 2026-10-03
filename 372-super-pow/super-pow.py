class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337

        def normal_pow(base: int, exponent: int) -> int:
            res = 1
            base = base % MOD

            for _ in range(exponent):
                res = (res * base) % MOD
            return res
        
        if not b:
            return 1

        last_digit = b.pop()

        part1 = normal_pow(self.superPow(a, b), 10)
        part2 = normal_pow(a, last_digit)

        return (part1 * part2) % MOD 
