package main

import "fmt"

func main(){
	s := "asdsaf"
	wordDict := []string{"asd", "saf"}
	r := isCanWordBreak(s, wordDict)
	fmt.Println(r)
}

// 单次拆分 https://leetcode-cn.com/problems/word-break/
// 每一个新的位置能否被拆分取决于上一个位置是否可以被拆分。使用dp
func isCanWordBreak(s string, wd []string) bool{
	// 放入map
	wdMap := make(map[string]struct{})
	for _, item := range wd{
		wdMap[item] = struct{}{}
	}

	dp := make([]bool, len([]rune(s))+1)
	dp[0] = true
	for i:=0;i<len([]rune(s));i++{
		for j:=i-1;j>=-1;j--{
			if dp[j+1] {
				if _,ok := wdMap[s[j+1:i+1]]; ok{
					dp[i+1] = true
					break
				}
			}
		}
	}
	return dp[len([]rune(s))]
}
