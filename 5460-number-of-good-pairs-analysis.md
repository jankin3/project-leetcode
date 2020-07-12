# 好数对的数目

### 题目地址
https://leetcode-cn.com/problems/number-of-good-pairs/

### 题目描述
给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。

```
示例 1：

输入：nums = [1,2,3,1,1,3]
输出：4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始
示例 2：

输入：nums = [1,1,1,1]
输出：6
解释：数组中的每组数字都是好数对
示例 3：

输入：nums = [1,2,3]
输出：0
```

### 解题思路
1. 遍历数组
2. 使用count统计总数，使用map存储每个元素的出现次数
3. 当当前元素已经存在的时候，则count加上map中元素的值，因为相同的元素增加x个的时候则总数增加x-1个（和原来的每一个数字结合依次）
	当前元素不存在的时候则初始化为1
4. 结果则为count

### 代码
```golang
func numIdenticalPairs(nums []int) int {
	numMap := map[int]int{}
	count := 0
	for _, item := range nums{
		v, ok := numMap[item]
		if ok {
			count += v
			numMap[item] ++
		}else{
			numMap[item] = 1
		}
	}
	return count
}
```