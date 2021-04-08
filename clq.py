from typing import List

def clq1(amount: int) -> int:#解决方法一
    coins = [1,5,10,20,50,100]
    def baoli(n: int) -> int:
        if n == 0:
            return n
        if n < 0:
            return -1
        res = 10000 #要求得的数量为最小值，因此为初始化最大值来进入递归
        for coin in coins:
            pre = baoli(n - coin)#计算当前子问题的最优解
            if pre == -1:#子问题无解
                continue
            res = min(res, 1+pre)#如果子问题的数量+当前一枚硬币大于已保存的最优解，则更新一次
        return res if res != 10000 else -1
    return baoli(amount)

print(clq1(33))

def clq2(amount: int) -> int:#解决方法二
    coins = [1,5,10,20,50,100]
    memo = dict()#字典
    def beiwanglu(n: int) -> int:
        if n in memo:
            return memo[n]#返回键 n 对应的值
        if n == 0:
            return n
        if n < 0:
            return -1
        res = 10000 
        for coin in coins:
            pre = beiwanglu(n - coin)
            if pre == -1:
                continue
            res = min(res, 1+pre)
        memo[n] = res if res != float('INF') else -1
        return memo[n]
    return beiwanglu(amount)

print(clq2(33))

def clq3(amount: int) -> int:#解决方法三
    dp = [amount+1 for j in range(0,amount+1)]#数组大小为amount+1 ，每个元素值都是amount+1
    dp[0] = 0 #边界条件
    coins = [1,5,10,20,50,100]
    for i in range(amount+1):   
        for coin in coins:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i-coin])
    return -1 if dp[amount] == amount + 1 else dp[amount]

print(clq3(33))