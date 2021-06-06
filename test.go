package main

import (
	"fmt"
)

func main() {
	s1 := "string"
	s2 := s1
	s3 := s1[:]
	fmt.Println(&s1, &s2, &s3)
}