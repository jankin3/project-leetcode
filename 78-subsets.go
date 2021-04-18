package main

import "fmt"

func main() {
	a := []int{1,3,4,5}
	fmt.Printf("a_addr:%p \n", &a)
	b := append(a, 6)
	fmt.Printf("a_val:%v||a_addr:%p||b_val:%v||b_addr:%p \n", a, &a,b,&b)

	// test
	//nums := []int{1,2,3,4}
	//fmt.Println("res:",subsetsV2(nums))
}

func subsets(nums []int) [][]int {
	if len(nums) == 0 {
		return [][]int{[]int{}}
	} else if len(nums) == 1 {
		return [][]int{nums}
	}

	var ret [][]int
	for i := 0; i < len(nums)-1; i++ {
		ret = append(ret, subsets(nums[:i+1])...)
		ret = append(ret, subsets(nums[i+1:])...)
	}
	return append(ret, nums)
}

func subsetsV2(nums []int) [][]int{
	if len(nums) == 0 {
		return [][]int{[]int{}}
	}

	ret := [][]int{[]int{}}
	for i := 0; i < len(nums); i++{
		cur := nums[i]
		retLen := len(ret)
		fmt.Println(ret)
		for j:=0;j<retLen;j++{
			fmt.Printf("i:%v||j:%v\n",i,j)
			//if cur == 5 && len(ret[j]) == 3{
			//	fmt.Println("test")
			//}
			fmt.Println("--1---")
			for k,_ := range ret{
				fmt.Printf("%v|%p|val=%v \n", k, &ret[k],ret[k])
			}
			fmt.Println("--1---")
			//fmt.Println("p:%p", ret[j])
			//fmt.Println("ret:",ret)
			//curCopy := cur
			newR := append(ret[j], cur)
			ret = append(ret, newR)

			fmt.Println("--2---")
			for k,_ := range ret{
				fmt.Printf("%v|%p|val=%v \n", k, &ret[k],ret[k])
			}
			fmt.Println("---2--")
			//fmt.Printf("newR:%v||retj:%v\n", newR,ret[j])
		}
	}
	return ret
}

//func subsetsV3(nums []int) [][]int{
	//if len(nums) == 0 {
	//	return [][]int{[]int{}}
	//}
	//
	//ret := [][]int{[]int{}}
	//for i := 0; i < len(nums); i++{
	//	cur := nums[i]
	//	retLen := len(ret)
	//	fmt.Println(ret)
	//	var moreList [][]int{}
	//	for j:=0;j<retLen;j++{
	//		fmt.Printf("i:%v||j:%v\n",i,j)
	//		fmt.Println("--1---")
	//		for k,_ := range ret{
	//			fmt.Printf("%v|%p|val=%v \n", k, &ret[k],ret[k])
	//		}
	//		fmt.Println("--1---")
	//		newR := append(ret[j], cur)
	//		moreList = append(moreList, newR)
	//
	//		fmt.Println("--2---")
	//		for k,_ := range ret{
	//			fmt.Printf("%v|%p|val=%v \n", k, &ret[k],ret[k])
	//		}
	//		fmt.Println("---2--")
	//	}
	//}
	//return ret
//}