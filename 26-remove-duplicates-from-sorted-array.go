package main

import "fmt"

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

func main() {
	nums := []int{0, 0, 1, 1, 1, 3, 3, 4}
	ret := removeDuplicatesV2(nums)
	fmt.Println(ret, nums)
}
