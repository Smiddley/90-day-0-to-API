//Find the maximum number of consecutive 1s in a binary array.

package main

import (
	"fmt"
)

func maxSinglePass(arr []int) int {
	if len(arr) == 0 {
		return 0
	}

	max_length := 0
	counter := 0

	for _, x := range arr {
		if x == 1 {
			counter += 1
		} else {
			if counter > max_length {
				max_length = counter
			}
			counter = 0
		}
	}

	return max(max_length, counter)
}

func main() {
	arr := []int{0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1}
	ans_max_single := maxSinglePass(arr)

	fmt.Println(ans_max_single)
}
