package main

import (
	"fmt"
)

func main() {
	nums := []int{0}
	ok := isCanJumpV2(nums)
	fmt.Println("ret:", ok)
}

// 反向回溯
func isCanJump(nums []int) bool {
	canJumpSlice := make([]bool, len(nums)) // false表示对应位置不可到，true表示可到
	canJumpSlice[len(canJumpSlice)-1] = true
	var rightPos int // 当前节点能到达的最大右边位置
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i]+i > len(nums)-1 {
			rightPos = len(nums) - 1
		} else {
			rightPos = nums[i] + i
		}

		for j := i + 1; j <= rightPos; j++ {
			if canJumpSlice[j] {
				canJumpSlice[i] = true
				break
			}
		}
	}
	return canJumpSlice[0]
}

// 正向圈定范围
func isCanJumpV2(nums []int) bool {
	var rightPos int
	for i := 0; i < len(nums); i++ {
		println(rightPos)
		if i > rightPos{
			break
		}
		if rightPos < i+nums[i] {
			rightPos = i + nums[i]
		}
		if rightPos >= len(nums)-1 {
			return true
		}
	}
	return false
}
