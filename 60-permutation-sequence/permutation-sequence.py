class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n + 1)]
    
        # Precompute factorials up to (n-1)!
        # factorials[i] will store i!
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
            
        # Convert k to 0-indexed index to match 0-indexed list operations
        k -= 1
        
        result = []
        
        # Determine the digits one by one from left to right
        for i in range(n - 1, -1, -1):
            # Calculate how many permutations belong to each block of the remaining choices
            # For the first position, block size is (n-1)!
            block_size = factorials[i]
            
            # Determine the index of the digit to pick next
            digit_index = k // block_size
            
            # Append the picked digit and remove it from the choices pool
            result.append(digits.pop(digit_index))
            
            # Update k to represent the remaining index within the chosen block
            k %= block_size
            
        return "".join(result)