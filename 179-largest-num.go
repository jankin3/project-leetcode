package main

import (
	"fmt"
	"sort"
	"strconv"
)

// https://leetcode-cn.com/problems/largest-number/
func main(){
	t := []int{10,2}
	r := largestNumber(t)
	fmt.Println(r)
}

// 按照最高位进行排序，如果最高位相同则比较
func largestNumber(nums []int) string {
	sort.Slice(nums, func(i,j int) bool{
		x, y := nums[i], nums[j]
		xdigit, ydigit := 10, 10
		for xdigit <= x{
			xdigit *= 10
		}
		for ydigit <= y{
			ydigit *= 10
		}
		return x*ydigit + y > y*xdigit + x
	})

	if nums[0] == 0 {
		return "0"
	}

	var ret []byte
	for _,item := range nums {
		ret = append(ret, strconv.Itoa(item)...)
	}
	return string(ret)
}
