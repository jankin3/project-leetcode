# 删除排序数组中的重复项

### 题目地址
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

### 题目描述
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

### 思路
快慢指针

### 代码
```go
// 使用当前位置指针ｃｕｒ（满指针）和偏移值ｌ得出快指针，比较
// 如果　==, 则　ｌ　＋＋
// 否则　替换位置
func removeDuplicates(nums []int) int {
	cur, l := 0, 0
	for cur < len(nums) && cur+l+1 < len(nums) {
		if nums[cur] >= nums[cur+l+1] {
			l++
		} else {
			nums[cur+1], nums[cur+l+1] = nums[cur+l+1], nums[cur+1]
			cur++
		}
	}
	return cur + 1
}

//  更加通俗易懂和优雅的双指针
func removeDuplicatesV2(nums []int) int {
	i := 0 // 慢指针
	for j := 1; j < len(nums); j++ {
		if nums[i] != nums[j] {
			i++
			nums[i] = nums[j]
		}
	}
	return i + 1
}
```