package main

import "fmt"

func main(){
	weights := []int{10,50,100,100,50,100,100,100}
	d := 5
	fmt.Println(getMinCapacity(weights,d))
}

//https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/
// 二分查找法获取D天内运送包裹的能力
func getMinCapacity(w []int, d int) int{
	var left,right int
	for _, v := range w{
		if left < v {
			left = v
		}
		right += v
	}
	ret := right
	for left <= right{
		mid := (left + right) /2
		needDays := getNeedDays(mid,w) // 判断mid是否符合
		fmt.Println(left,right,mid,needDays)
		if needDays > d{
			left = mid + 1
		}else{
			ret = mid
			right = mid -1
		}
	}
	return ret
}

func getNeedDays(c int,w []int) int{
	var needDays = 1
	var curCarry int
	for _, item := range w{
		curCarry += item
		if curCarry > c{ // 到达最大运输量
			needDays ++
			curCarry = item
		}
	}
	return needDays
}
