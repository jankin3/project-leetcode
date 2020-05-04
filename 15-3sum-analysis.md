### 题目地址
https://leetcode-cn.com/problems/3sum/

### 题目描述
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

### 我的解题思路-hash法
题目分析，三数之和为0，x+y+z=0, 这意味着3元方程，`暴力法直接遍历三次`。 优化方向是减少变量
1. contains 0, 转化为 x+y=0, 使用2数之和
2. not contains 0,分为2正1负，和2负1正(我想的过于复杂了),其实就是循环整个list, 然后在寻找2数之和等于0-z的情况的优化版本

我的思路从根本上说还是转化为2数之和的情况，来求解，时间复杂度为O(n^2)

### 参考其他思路：
1. 双指针
先排序，然后遍历，对于每个遍历的值，对其右边的数进行双指针移动查找(从两端向中间缩进)

    `思考`：同样是O(n^2), 这对于转化为两数之和的解法有什么优势？
     自答：更快，因为双指针的移动比hash的单指针更加有针对性，更快速找到结果
       
       
### 具体代码 
位置： 15-3sum.py

我的思路 复杂版hash解法 -> threeSum_complicate_hash()
简化版hash解法 -> threeSum_simple_hash()
双指针版本 -> double_needle()