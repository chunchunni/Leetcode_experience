from typing import List
def fb1(n: int) -> int: #解决方法一
    memo = [0]*(n+1)

    def fb_remember(memo: List[int], n: int)-> int:
        if n == 0 or n == 1:
            return n
        if memo[n] != 0:
            return memo[n]
        memo[n] = fb_remember(memo,n-1) + fb_remember(memo,n-2)
        return memo[n]

    return fb_remember(memo,n)

print(fb1(10))

def fb2(n: int) -> int:#解决方法二
    if n == 0 or n == 1:
        return n
    dp_0 = 0
    dp_1 = 1
    for i in range(2,n+1):
        temp = dp_1
        dp_1 = dp_0 + dp_1
        dp_0 = temp
    return dp_1

print(fb2(10))


