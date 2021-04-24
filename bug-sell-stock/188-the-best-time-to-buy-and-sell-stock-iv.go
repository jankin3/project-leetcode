package main

import "fmt"

func main() {
	stocks := []int{3, 2, 6, 5, 0, 3}
	fmt.Println("ret:", maxProfitIv(2, stocks))
}

// maxProfit 表示第i次成交在第j天的价格
func maxProfitIv(k int, prices []int) int {

	var dp [][]int
	for i := 0; i < k; i++ {
		var perTimeProfit []int // 每次成交的最大价值
		for j := 0; j < len(prices); j++ {
			if i == 0 {
				tmp := getOnceDealMaxProfit(prices[:j+1]) //最多成交一次的最大价值
				perTimeProfit = append(perTimeProfit, tmp)
				continue
			}

			newMaxProf := dp[i-1][j] // 上一层的最大利润加上多成交一次的利润
			for k := 1; k < j; k++ {
				tmp := dp[i-1][k] + getOnceDealMaxProfit(prices[k+1:j+1])
				if newMaxProf < tmp {
					newMaxProf = tmp
				}
			}
			perTimeProfit = append(perTimeProfit, newMaxProf)
		}
		fmt.Println(perTimeProfit)
		dp = append(dp, perTimeProfit)
	}
	return dp[k-1][len(prices)-1]
}

func getOnceDealMaxProfit(prices []int) int {
	var minPrice, maxProf int
	minPrice = prices[0]
	for _, item := range prices {
		if item < minPrice {
			minPrice = item
		}

		if item-minPrice > maxProf {
			maxProf = item - minPrice
		}
	}
	return maxProf
}
