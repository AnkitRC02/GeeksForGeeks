
from typing import List

class Solution:
    def getPrimes(self, n: int) -> List[int]:
        if n < 2:
            return [-1, -1]
        
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        
        p = 2
        while (p * p <= n):
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
            p += 1
        
        primes = [p for p, is_prime in enumerate(sieve) if is_prime]
        prime_set = set(primes)
        
        for a in primes:
            b = n - a
            if b in prime_set:
                return [a, b]
        
        return [-1, -1]

        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends