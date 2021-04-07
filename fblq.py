from typing import List
def fb(n: int) -> int:
    memo = [0]*(n+1)

    def fb_remember(memo: List[int], n: int)-> int:
        if n == 0 or n == 1:
            return n
        if memo[n] != 0:
            return memo[n]
        memo[n] = fb_remember(memo,n-1) + fb_remember(memo,n-2)
        return memo[n]

    return fb_remember(memo,n)

print(fb(7))

