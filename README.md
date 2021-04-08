# Leetcode_experience

## 一、动态规划

动态规划 -> 求最值 -> 穷举 <- 存在重叠子问题，无法直接暴力穷举（指数级别的复杂度） -> 引入DP Table
对于一个整体求最值问题，拆解为多个子问题，求解子问题的最优，从而得到原问题最值。
在动态规划的过程中，对于DP Table的遍历顺序有多种情况：正向、反向、斜向（例如左下到右上）等等。使用的标准在于1：遍历过程中所使用的状态以及计算过。2：遍历的重点是所需结果的状态。


### 1、斐波那契
    对于诸如斐波拉契数列，直接的暴力解法相当于求一遍递归树所有的节点，即2^n的复杂度。其中原因就是重复计算了大量节点。
    
解决方法1--自顶向下：可以在递归调用重复调参的同时，使用一个数组（备忘录）来记录已经结算过的子问题的值。这样就达到了空间换时间的目的，最终时间为n。[代码](https://github.com/chunchunni/Leetcode_experience/blob/main/fblq.py)

解决方法2--自底向上：可以将递归问题转化为迭代问题。从当前已经解决的问题出发，构建DP Table，循环计算。[代码](https://github.com/chunchunni/Leetcode_experience/blob/main/fblq.py)

### 2、凑零钱
    对于指定金额，给出在币值范围内进行组合的最少数量解。

解决方法1--暴力递归：遍历币值列表，计算金额-当前币值i的最优解（即子问题），然后在 前一个保留下来的最优解 和 当前子问题的最优解之间 之间选出最小者。无论当前金额是多少，所做的选择就是从面额列表中选择一枚硬币，此时金额就会减少。[代码](https://github.com/chunchunni/Leetcode_experience/blob/main/clq.py)

解决方法2--带备忘录：使用一个备忘录来计算已经求过的金额所需的虽小币数，当再次递归到这个金额时，直接查找备忘录中是否计算过，有则直接读取。[代码](https://github.com/chunchunni/Leetcode_experience/blob/main/clq.py)

解决方法3--DP迭代：使用自底向上的DP Table来消除重叠子问题，类似于备忘录。[代码](https://github.com/chunchunni/Leetcode_experience/blob/main/clq.py)

后两者解法与第一种的区别在于优化了重叠的子问题，而状态转移方程部分其实是一致的。
