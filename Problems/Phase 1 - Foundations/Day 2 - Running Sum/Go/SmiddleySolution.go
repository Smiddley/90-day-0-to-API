// Given an array, return a new array where each element at index i is the sum of nums[0..i].

package main

import (
	"errors"
	"fmt"
)

func sumSlice(arr []int) ([]int, error) {
	if arr == nil {
		return nil, errors.New("Slice is nil")
	}
	if len(arr) == 0 {
		return []int{}, nil
	}

	ans := make([]int, 0, len(arr))
	total := 0
	for _, value := range arr {
		total = total + value
		ans = append(ans, total)
	}
	return ans, nil
}

func main() {
	arr := []int{1, 5, 7, 3, -7, 8, 3, 4}
	fmt.Println(sumSlice(arr))
}
