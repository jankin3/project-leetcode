# 字符串异位词分组

### 题目地址

https://leetcode-cn.com/problems/group-anagrams/



### 题目描述

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

```示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```


说明：

所有输入均为小写字母。
不考虑答案输出的顺序。



### 思路

1. （`按照排序后的单词分类`）将每个单词排序，即可得到唯一的标识。然后当做字典的key，值为item的list。

   + 时间O(NKlogK)，其中 N 是 strs 的长度，而 K 是 strs 中字符串的最大长度。当我们遍历每个字符串时，外部循环具有的复杂度为 O(N)
   + 空间复杂度：O(NK)，排序存储在 `ans` 中的全部信息内容

2. （`按照计数分类`）将排序的key，变成计数的标识

   + 时间复杂度：O(NK)，其中 N 是 strs 的长度，而 K 是 strs 中字符串的最大长度。计算每个字符串的字符串大小是线性的，我们统计每个字符串。

   + 空间复杂度：O(NK)，排序存储在 ans 中的全部信息内容。



### 代码

```go
// 字母异位词排序
package main

import (
	"fmt"
	"sort"
	"strings"
)

func toArray(a []string) [][]string {
	strArrMap := map[string][]string{}
	for _, item := range a {
		itemArr := strings.Split(item, "")
		sort.Strings(itemArr)
		newItem := strings.Join(itemArr, "") // 字符串切片如何转换成字符串
		v, ok := strArrMap[newItem]
		if ok {
			strArrMap[newItem] = append(v, item)
		} else {
			strArrMap[newItem] = []string{item}
		}
	}

	var ret [][]string
	for _, item := range strArrMap {
		ret = append(ret, item)
	}
	return ret
}

func toArrayV2(str []string) [][]string {
	strArrMap := map[[26]int][]string{}
	for _, item := range str {
		// 排序变成count计数
		numArrayKey := [26]int{}
		for i := 0; i < len(item); i++ {
			numArrayKey[item[i]-97] ++
		}

		v, ok := strArrMap[numArrayKey]
		if ok {
			strArrMap[numArrayKey] = append(v, item)
		} else {
			strArrMap[numArrayKey] = []string{item}
		}
	}

	var ret [][]string
	for _, item := range strArrMap {
		ret = append(ret, item)
	}
	return ret
}

func main() {
	a := []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	c := toArrayV2(a)
	fmt.Println(c)
}
```





