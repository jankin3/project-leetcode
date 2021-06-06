package main

// 改进点： 定义了每个区间的四个属性。 所以当获取中间位置的结果时可以方便取值， 时间复杂度只剩下递归：n
// lSum 表示 [l,r] 内以 l 为左端点的最大子段和
// rSum 表示 [l,r] 内以 r 为右端点的最大子段和
// mSum 表示 [l,r] 内的最大子段和
// iSum 表示 [l,r] 的区间和

func maxSubArray(nums []int) int {
	return get(nums, 0, len(nums)-1).mSum
}

func pushUp(l, r Status) Status {
	iSum := l.iSum + r.iSum
	lSum := max(l.lSum, l.iSum+r.lSum)
	rSum := max(r.rSum, r.iSum+l.rSum)
	mSum := max(max(l.mSum, r.mSum), l.rSum+r.lSum)
	return Status{lSum, rSum, mSum, iSum}
}

func get(nums []int, l, r int) Status {
	if l == r {
		return Status{nums[l], nums[l], nums[l], nums[l]}
	}
	m := (l + r) >> 1
	lSub := get(nums, l, m)
	rSub := get(nums, m+1, r)
	return pushUp(lSub, rSub)
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

type Status struct {
	lSum, rSum, mSum, iSum int
}
