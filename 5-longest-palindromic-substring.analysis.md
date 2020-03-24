### 题目地址
https://leetcode-cn.com/problems/longest-palindromic-substring/

### 题目描述
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
### 思路
`中心扩展法`(我采用的，比较简单)：遍历数据，由中心向左右逐渐扩展
优化：考虑奇偶部分可以采用中间插入而都变成奇数处理。

`Manacher 算法` to do
