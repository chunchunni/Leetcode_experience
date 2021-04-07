from typing import List

def clq(amount: int) -> int:
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

print(clq(13))