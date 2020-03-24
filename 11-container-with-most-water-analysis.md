### 题目地址
https://leetcode-cn.com/problems/container-with-most-water/

### 题目描述
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

### 分析
刚开始看这个题目很容易分析到，要通过不断的缩小x轴的width去逐渐接近最大的面积。

错误思路：判断左边前进或者右边后退之后的面积，谁更大来谁移动。这种产生了局部最优但是全局非最优的选择

正向思路: `遍历所有宽度下最优解`。宽度递减，高度取决于最短的点，所以左指针和右指针，选择值小的移动。

`为什么值小的移动?`
1. 因为值小的移动可能会变大，但是值大的移动一定不会变大(不变或者减小)。
2. `最优的面积定包括最高的柱子`，所以谁小谁动。

```python
class Solution:
    def maxArea(self, height):
        max_s = 0
        left_index, right_index = 0, len(height) - 1
        while left_index < right_index:
            cur_s = (right_index - left_index) * min(height[left_index], height[right_index])
            max_s = max_s if max_s > cur_s else cur_s
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return max_s
```