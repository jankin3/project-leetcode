# 计算 x 的 n 次幂函数

### 题目地址

https://leetcode-cn.com/problems/powx-n/

### 题目描述

实现 pow(x, n) ，即计算 x 的 n 次幂函数。

```go
示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
```



### 思路-递归

计算x的n次幂，可以由x的n/2次幂的平方得到.(奇偶分条件)

代码见下面



### 思路-迭代

难点，如果把迭代正向思考，在于如何确定时候奇偶。

比如：

```go
10=（2*2+1）*2+1
```

关键在于拆解n

x^n = x^a * x^b * x^c

n = a + b + c

正向迭代，也就是每次对现有的数进行平方。举个例子

3^1, 3^2, 3^4, 3^8

从指数的角度思考就是每次`指数*2`。从而的出，只要把n用以2的m次方相加起来，也就是n的2进制表示

```go
curXi := x
ret := float64(1)
for ; n > 0; n = n / 2 {
  more := n % 2
  if more == 1 {
    ret = ret * curXi
  }
  curXi = curXi * curXi
}
```





### 代码

```go
package main

import "fmt"

// 递归
func myPow(x float64, n int) float64 {
	if n == 1 {
		return x
	} else if n < 0 {
		return 1 / myPow(x, -n)
	} else {
		if n%2 == 0 {
			sub := myPow(x, n/2)
			return sub * sub
		} else {
			sub := myPow(x, n/2)
			return sub * sub * x
		}
	}
}

// 迭代
func myPowV2(x float64, n int) float64 {
	if n == 0{
		return 1
	}

	isPositive := true
	if n < 0{
		isPositive = false
		n = -n
	}

	curXi := x
	ret := float64(1)
	for ; n > 0; n = n / 2 {
		more := n % 2
		if more == 1 {
			ret = ret * curXi
		}
		curXi = curXi * curXi
	}

	if isPositive{
		return ret
	}else{
		return 1/ret
	}
}

func main() {
	//fmt.Println(myPow(2.00000, -2))
	r := myPowV2(2, -2)
	fmt.Println(r)
}
```

