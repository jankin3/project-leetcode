# 整数反转

### 题目位置
https://leetcode-cn.com/problems/reverse-integer/

### 题目描述
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。


### 思路
1. 反转可以直接采用弹出的方法
```
//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;
```

2. 这个题目的重点在于溢出判断


### 代码
```golang
package main

import (
	"errors"
	//"errors"
	"fmt"
	"strconv"
)

const Int32Max = int32(^uint32(0) >> 1)
const Int32Min = ^Int32Max

func reverse(x int) (result int32, err error) {
	s := strconv.Itoa(x)
	// 获取符号
	c := int32(1)
	if string(s[0]) == "-" {
		c = -1
		s = s[1:]
	}

	isHead := true
	for i := len(s) - 1; i >= 0; i-- {
		if isHead {
			if string(s[i]) == "0" {
				continue
			} else {
				isHead = false
			}
		}
		n, err := strconv.Atoi(string(s[i]))
		if err != nil {
			return result, errors.New("error1")
		}
		if c == int32(1) && (result > Int32Max/10 || int32(n) > Int32Max-(result*10)) {
			return 0, nil
		} else if c == int32(-1) && (result > (Int32Min/10)*c || c*int32(n) < Int32Min-c*(result*10)) { // 超出
			return 0, nil
		} else {
			result = result*10 + int32(n)
		}
	}
	return c * result, nil
}

func reverseV2(x int32) int32 {
	result := int32(0)
	for x != 0 {
		pop := x % 10
		x = x / 10
		if result > Int32Max/10 || pop+result*10 > Int32Max {
			return 0
		}
		if result < Int32Min/10 || pop+result*10 < Int32Min {
			return 0
		}
		result = result*10 + pop
	}
	return result
}

func main() {
	fmt.Println(Int32Min, Int32Max)
	s := reverseV2(-123)
	fmt.Println(s)
}

```
