package main

import (
	"fmt"
	"strconv"
)

// 传统解法，转换为字符串，双指针遍历
func isPalindromeV1(x int) bool {
	if x < 0{
		return false
	}

	isOdd := len(strconv.Itoa(x)) % 2 == 1
	var lPos, rPos int // 左坐标和右坐标
	lPos = len(strconv.Itoa(x)) / 2 - 1
	if isOdd{
		rPos = lPos + 2
	}else{
		rPos = lPos + 1
	}

	xBytes := []byte(strconv.Itoa(x))
	for {
		if lPos < 0{
			break
		}
		if xBytes[lPos] != xBytes[rPos]{
			return false
		}
		lPos --
		rPos ++
	}
	return true
}

// 转换x的后半部分，然后对比
func isPalindromeV2(x int) bool{
	if x < 0 {
		return false
	}

	var len int
	xCopy := x
	for {
		if xCopy < 10{
			len ++
			break
		}
		xCopy = xCopy / 10
		len ++
	}

	var reverseRightHalfX int
	xCopy = x
	for i:=0;i<len/2;i++ {
		reverseRightHalfX = xCopy % 10 + reverseRightHalfX * 10
		xCopy = xCopy / 10
	}
	if len % 2 == 1{
		xCopy = xCopy / 10
	}

	if reverseRightHalfX == xCopy{
		return true
	}

	return false
}

// 同V2, 优化获取长度部分
func isPalindromeV2Optimize(x int) bool{
	if x < 0 || (x % 10 == 0 && x != 0){
		return false
	}

	var reverseRightHalfX int
	for x > reverseRightHalfX {
		reverseRightHalfX = x % 10 + reverseRightHalfX * 10
		x = x / 10
	}

	return x == reverseRightHalfX || x == reverseRightHalfX / 10
}

func main(){
	ret := isPalindromeV2Optimize(10)
	fmt.Println(ret)
}