class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        result = []
        n = len(rain)
        alice_needs = 0
        bob_needs = 0

        for i in range(n):
            alice = (rain[i] == 1) and (i < n-1 and rain[i+1] == 1)
            bob = (rain[i] == 1)
            
            if not alice and not bob:
                result.append("None")
            elif alice and not bob:
                result.append("Alice")
                alice_needs += 1
            elif bob and not alice:
                result.append("Bob")
                bob_needs += 1
            else:
                if alice_needs <= bob_needs:
                    result.append("Alice")
                    alice_needs += 1
                else:
                    result.append("Bob")
                    bob_needs += 1

        return result