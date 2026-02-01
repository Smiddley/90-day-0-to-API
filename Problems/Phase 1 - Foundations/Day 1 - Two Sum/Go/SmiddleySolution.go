// Given an array of integers nums and a target integer target, return the indices of two numbers that add up to the target.

// Example:

// nums = [2,7,11,15], target = 9 → [0,1]
// nums = [3,2,4], target = 6 → [1,2]

// Cloud Analogy: Connection tracking table: hash map maps value → index.

// mental notes:
// Same concept as with python, but without the built in enumerate function.
// Go explicitly tracks the index in the for loop, so its actually more 'language native'

// Function takes []int, int, returns []int.
// build map of seen values from the nums array. Seen map will be at most length len(nums)
// Will preserve the O(1) average complexity

package main

import (
	"fmt"
)

func compliment_calculator(arr []int, X int) []int {
	seen := make(map[int]int)

	for index, value := range arr {
		compliment := X - value
		val, ok := seen[compliment]
		if ok {
			return []int{val, index}
		} else {
			seen[value] = index
		}

	}
	return nil
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Println(compliment_calculator(nums[:], target))

	nums = []int{3, 2, 4}
	target = 6
	fmt.Println(compliment_calculator(nums[:], target))
}
