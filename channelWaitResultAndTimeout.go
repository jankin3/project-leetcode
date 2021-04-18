package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	//aStr := "abcdefg"
	//println(string(aStr[0]))
	goChannelWaitG()
}

// 使用channel控制等待所有协程执行完毕，并且添加超时时间
func goChannelWaitG() {
	ctx, cancel := context.WithTimeout(context.Background(), 1000*time.Millisecond)
	c := make(chan int, 3)
	defer close(c)
	for i := 0; i < 3; i++ {
		go worker(ctx, i, c)
	}
	var count int
	for i := 0; i < 3; i++ {
		select {
		case item := <-c:
			fmt.Printf("item:%v\n", item)
			count++
			if count == 3 {
				break
			}
		case <-ctx.Done():
			fmt.Printf("time out")
			break
		}
	}
	cancel()
}

func worker(ctx context.Context, i int, c chan int) {
	if i == 2{
		time.Sleep(1500*time.Millisecond)
	}
	select {
	case <-ctx.Done():
		fmt.Printf("worker:%v done\n", i)
		return
	case c <- i:
		fmt.Printf("worker:%v finish\n", i)
	}
}
