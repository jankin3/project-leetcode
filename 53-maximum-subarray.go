package main

import "fmt"


// 思路：将区间二分，区间的最大序列有三种位置：左区间中，右区间中，或者中间位置. 所以可以采取递归的方式求解， 中间位置则需要遍历整个数据获取最大值
// 复杂度：时间复杂度：递归加上求中间值遍历，需要 n^2
func main(){
	nums := []int{-10000}
	r := getMaxSubArray(nums)
	fmt.Println("res:", r)
}

func getMaxSubArray(nums []int)int{
	return getRecursiveMaxSub(nums)
}


func getRecursiveMaxSub(nums []int)int{
	if len(nums) == 1{
		return nums[0]
	}
	if len(nums) == 2{
		return maxInt(maxInt(nums[0], nums[1]), nums[0]+nums[1])
	}
	var m int = len(nums) / 2
	var lNum, rNum, mNum int
	lNum = getRecursiveMaxSub(nums[0:m])
	rNum = getRecursiveMaxSub(nums[m:])
	mNum = getMNum(nums, m)
	return maxInt(maxInt(lNum, rNum), mNum)
}

func getMNum(nums []int, m int) int{
	var lSum, rSum int
	var lMaxSum = nums[m]
	var rMaxSum = nums[m-1]
	for i:=m;i<len(nums);i++{
		lSum += nums[i]
		if lSum > lMaxSum{
			lMaxSum = lSum
		}
	}
	for j:=m-1;j>=0;j--{
		rSum += nums[j]
		if rSum > rMaxSum{
			rMaxSum = rSum
		}
	}
	return lMaxSum + rMaxSum
}

func maxInt(a,b int) int{
	if a < b {
		return b
	}
	return a
}
