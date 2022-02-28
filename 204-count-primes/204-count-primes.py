import math


class Solution:
    # def countPrimes(self, n: int) -> int:
#         if n < 3: return 0
        
#         primes = [2]
        
#         for i in range(3, n):
#             for j in primes:
#                 if (i % j == 0):
#                     break
#                 if (j > math.sqrt(i) + 1):
#                     primes.append(i)
#                     break
#             else:
#                 primes.append(i)
        
#         return len(primes)

    def countPrimes(self, n: int) -> int:
        
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            # for j in range(i * i, n, i):
            #     primes[j] = False
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        
        return sum(primes)

    