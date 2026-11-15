class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_numbers = []
        even_numbers = []

        for i in range(1, 2*n + 1):
            if i % 2 == 0:
                even_numbers.append(i)
            else:
                odd_numbers.append(i)
        
        sumEven = sum(even_numbers)
        sumOdd = sum(odd_numbers)

        while sumOdd != 0:
            sumEven, sumOdd = sumOdd, sumEven % sumOdd
        
        return sumEven

        # return math.gcd(sumOdd, sumEven)