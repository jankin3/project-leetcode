package main

import (
	"fmt"
	"sort"
)

//https://leetcode-cn.com/problems/merge-intervals/
func main(){
	//intervals = [[1,3],[2,6],[8,10],[15,18]]
	nums := [][]int{
		//{2,6},{2,7},
		//{1,3},{2,6},{8,10},{15,18},
		{1,3},{2,4},
	}
	fmt.Println("ret:", mergeIntervalsV2(nums))
}

// 想复杂了，通过在数轴上打点计算结果
func mergeIntervals(nums [][]int) [][]int{
	line := make(map[int]int, 2*len(nums))
	// calculate
	for _, points := range nums{
		for i, point := range points{
			if i == 0{
				line[point] += -1
			}else{
				line[point] += 1
			}
		}
	}

	var j int
	lineKeys := make([]int, len(line))
	for k := range line {
		lineKeys[j] = k
		j++
	}
	sort.Ints(lineKeys)

	//fmt.Println(lineKeys,line)

	var ret [][]int
	var sum int
	var start,end int
	for _, item := range lineKeys{
		if sum == 0 {
			start = item // 初始点
		}
		sum += line[item]

		end = item
		if sum == 0{
			ret = append(ret, []int{start,end})
		}
	}
	return ret
}

// 官方解法，直接排序然后合并. 大道至简。。。
func mergeIntervalsV2(nums [][]int) [][]int{
	sort.Slice(nums, func(i, j int) bool {
		return nums[i][0] < nums[j][0]
	})

	var ret [][]int
	for _, points := range nums{
		if len(ret) == 0 || ret[len(ret)-1][1] < points[0]{
			ret = append(ret, points)
		}else{
			if points[1] > ret[len(ret)-1][1]{
				ret[len(ret)-1][1] = points[1]
			}
		}
	}
	return ret
}