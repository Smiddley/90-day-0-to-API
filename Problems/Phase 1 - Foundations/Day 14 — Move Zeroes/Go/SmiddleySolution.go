package main

import "fmt"

func moveZeros(nums []int) []int {
	zero_pointer := 0

	for i := 0; i < len(nums); i++ {
		if nums[zero_pointer] == 0 {
			zero_pointer = i
			break
		}
	}

	for i := zero_pointer; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]

			zero_pointer++
		}
	}
	return nums
}

func main() {
	tests := [][]int{
		{1, 2, 4, 5},
		{1, 0, 2, 0, 4},
		{},
		{0, 1, 0, 3},
		{0, 0, 0, 0},
	}

	for _, test := range tests {
		fmt.Println(moveZeros(test))
	}
}
