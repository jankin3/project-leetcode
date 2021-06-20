package main

import "fmt"

func main() {
	nums := []int{2, 2, 1, 1, 1, 2, 2}
	ret := majorityElement(nums)
	fmt.Println(ret)
}

// 摩尔投票法
// 解释： 循环遍历，如果当前x值为众数，则一比一和非众数抵消最终剩下来必然是众数。如果当前不是众数，则和其他数抵消最终剩余也是众数
func majorityElement(nums []int) int {
	targetNum := 0
	targetNumCount := 0
	for i := 0; i < len(nums); i++ {
		if targetNumCount == 0 {
			targetNum = nums[i]
			targetNumCount = 1
			continue
		}
		if targetNum != nums[i] {
			targetNumCount--
		} else {
			targetNumCount++
		}
	}
	return targetNum
}
