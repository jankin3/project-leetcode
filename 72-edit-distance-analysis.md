# 编辑距离



### 题目地址

https://leetcode-cn.com/problems/edit-distance/



### 题目描述

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


示例 1：

```
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```



### 思路

联想: 如果hors到ros距离为x, 则horse到ros不会超过x+1(执行插入操作)

能不能将删除和替换同样转换成类似的子问题?



目标: horse->ros

若hors->ros为x, 则不超过x+1 (插入)

若roe->ro为y,则不超过 y+1(删除)

若ho->ro为z,则不超过z+1(替换)

注意此处为不超过,表示三种策略应该取最小值



此时使用dp的画表的方法

|      | #    | r    | o    | s    |
| ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |
| ...  | ...  | ...  |      | ...  |
| :--: | ---- | ---- | ---- | ---- |
|  #   | 0    | 1    | 2    | 3    |
|  h   | 1    | 1    | 2    | 3    |
|  o   | 2    | 2    |      |      |
|  r   | 3    | 2    |      |      |
|  s   | 4    |      |      |      |
|  e   | 5    |      |      |      |



递推的关系:

```go
if word1[i-1] == word2[j-1] { // 从一开始,所以是-1
	dp[i][j] = dp[i-1][j-1] // 如果值相等,则相当于对角线过来,没有额外操作
} else {
	dp[i][j] = Min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 // 否则相当于左侧,上侧和对角线的最小值加1
}
```

 

### 代码

```go 3
package main

import (
	"fmt"
)

func getEditDistance(word1 string, word2 string) int {
	dp := make([][]int, len(word1)+1)
	// init
	for i := 0; i <= len(word1); i++ {
		col := make([]int, len(word2)+1)
		dp[i] = col
	}
	// init dp  when i = 0 or j = 0
	for j := 0; j <= len(word2); j++ {
		for i := 0; i <= len(word1); i++ {
			if i == 0 {
				dp[i][j] = j
			}
			if j == 0 {
				dp[i][j] = i
			}
		}
	}

	// 核心部分
	for j := 1; j <= len(word2); j++ {
		for i := 1; i <= len(word1); i++ {
			if word1[i-1] == word2[j-1] { // 从一开始,所以是-1
				dp[i][j] = dp[i-1][j-1]
			} else {
				dp[i][j] = Min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
			}
		}
	}
	return dp[len(word1)][len(word2)]
}

func Min(x, y, z int) int {
	if x < y {
		if x < z {
			return x
		} else {
			return z
		}
	} else {
		if y < z {
			return y
		} else {
			return z
		}
	}
}

func main() {
	word1 := "horse"
	word2 := "ros"
	num := getEditDistance(word1, word2)
	fmt.Println(num)
}
```







