package main

import "fmt"

func main(){
	k := make(map[int]struct{})
	k[213] = struct{}{}
	k[2135] = struct{}{}
	v,ok := k[213]
	fmt.Println(v,ok)
}