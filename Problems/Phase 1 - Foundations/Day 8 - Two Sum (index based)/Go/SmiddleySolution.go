// Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

// ### You may assume:
// Exactly one solution exists
// You may not use the same element twice
// Return the indices in any order.

// ### Input
// nums: array of integers
// target: integer

// ### Output
// A pair of integers `[i, j]` such that `nums[i] + nums[j] == target`

// ### Constraints
// ```
// 2 ≤ len(nums) ≤ 10⁵
// -10⁴ ≤ nums[i] ≤ 10⁴
// ```

// ### Example
// ```
// Input:  nums = [2,7,11,15], target = 9
// Output: [0,1]
// ```

package main

import "fmt"

func twoSum(a []int, t int) []int {
	seen := make(map[int]int, len(a))
	ans := []int{}
	for i, num := range a {

		if _, ok := seen[t-num]; ok {
			ans = append(ans, seen[t-num], i)
			return ans

		} else {
			seen[num] = i
		}
	}

	return ans
}

func main() {
	testSlices := [][]int{
		{2, 7, 11, 15},
		{-4, 2, 6, -2, 9, 4},
	}

	testTargets := []int{9, 5}

	// make sure have same number of targets and slices. else test loop fails
	if len(testSlices) == len(testTargets) {
		for i := range testSlices {
			fmt.Println(twoSum(testSlices[i], testTargets[i]))
		}
	} else {
		fmt.Println("Slice and Target mismatch")
	}
}
