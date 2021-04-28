package main

import "fmt"

func main(){
	stocks := []int{7,6,4,3,1}
	fmt.Println("ret:",maxProfit(stocks))
}

func maxProfit(prices []int) int {
	var buyAmount, profit int
	buyAmount = prices[0]

	for i:=1;i<len(prices);i++{
		if prices[i] < prices[i-1] { // 拐点
			if prices[i-1] > buyAmount{
				profit = profit + (prices[i-1] - buyAmount)
			}
			buyAmount = prices[i]
		}

		if i == len(prices) - 1 && prices[i] > buyAmount{ // 最后边界
			profit = profit + (prices[i] - buyAmount)
		}
	}
	return profit
}
