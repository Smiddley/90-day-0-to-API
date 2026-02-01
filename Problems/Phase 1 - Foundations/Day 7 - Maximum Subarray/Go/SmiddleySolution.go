// Problem Statement
// Given an array of integers nums, find the maximum possible sum of a non-empty contiguous subarray.
// A contiguous subarray is a sequence of elements that appear consecutively in the original array.
// You must return the maximum sum, not the subarray itself.

// Input:
//     nums: an array (slice / list) of integers
//     Length: 1 ≤ len(nums) ≤ 10⁵
//     Values: -10⁴ ≤ nums[i] ≤ 10⁴

// Output:
// An integer representing the largest possible sum of any contiguous subarray.

// Constraints & Rules
//     The subarray must be contiguous
//     You may not skip elements.
//     The subarray must contain at least one element
//     Returning 0 is not allowed unless 0 is the maximum achievable sum.
//     The array may contain all negative numbers

// Time complexity target: O(n)
// Space complexity target: O(1) (excluding input)

package main

import (
	"fmt"
)

func maxSubSliceValue(a []int) int {
	max_value := a[0]
	current := 0
	for _, val := range a {
		current = max(val, current+val)
		max_value = max(max_value, current)
	}
	return max_value
}

func main() {
	tests := [][]int{
		{-1, -2, -3},
		{1, 2, 3},
		{-2, 1, -3, 4, -1, 2, 1, -5, 4},
		{-2, 1, -3, 4, -1, 2, 1, -5, 4, 6},
	}

	for _, test := range tests {
		fmt.Println(maxSubSliceValue(test))
	}
}
