package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	nums := []int{-1,2,1,-4}
	targetNum := 1
	ret := threeSummaryClosest(nums, targetNum)
	fmt.Printf("ret:%d", ret)
}

func threeSummaryClosest(nums []int, target int) int {
	sort.Ints(nums)
	//fmt.Println(nums)
	closestNum := nums[0]+nums[1]+nums[2]

	for i := 0; i < len(nums)-2; i++ {
		j := i + 1
		k := len(nums) - 1
		for j < k {
			if math.Abs(float64(closestNum-target)) > math.Abs(float64(nums[i]+nums[j]+nums[k] - target)){
				closestNum = nums[i]+nums[j]+nums[k]
			}

			if nums[i]+nums[j]+nums[k] > target {
				k--
			} else if nums[i]+nums[j]+nums[k] < target {
				j++
			} else {
				return nums[i] + nums[j] + nums[k]
			}
		}
	}

	return closestNum
}
