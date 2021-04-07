# Leetcode_experience

## 一、动态规划

动态规划 -> 求最值 -> 穷举 <- 存在重叠子问题，无法直接暴力穷举（指数级别的复杂度） -> 引入DP Table
对于一个整体求最值问题，拆解为多个子问题，求解子问题的最优，从而得到原问题最值。

### 1、斐波那契
    对于诸如斐波拉契数列，直接的暴力解法相当于求一遍递归树所有的节点，即2^n的复杂度。其中原因就是重复计算了大量节点。
    
解决方法1--自顶向下：可以在递归调用重复调参的同时，使用一个数组（备忘录）来记录已经结算过的子问题的值。这样就达到了空间换时间的目的，最终时间为n。[代码](https://github.com/chunchunni/Leetcode_experience/blob/main/fblq.py)

解决方法2--自底向上：可以将递归问题转化为迭代问题。从当前已经解决的问题出发，构建DP Table，循环计算。[代码](https://github.com/chunchunni/Leetcode_experience/blob/main/fblq.py)

### 2、凑零钱
    对于指定金额，给出在币值范围内进行组合的最少数量解。

解决方法1--暴力递归：遍历币值列表，计算金额-当前币值i的最优解（即子问题），然后在 前一个保留下来的最优解 和 当前子问题的最优解之间 之间选出最小者。[代码](https://github.com/chunchunni/Leetcode_experience/blob/main/clq.py)
