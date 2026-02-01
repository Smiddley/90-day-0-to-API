//Return intersection of two arrays (unique elements only).

package main

import (
	"fmt"
)

func uniqueSlice(arr []int) []int {

	ans := make([]int, 0, len(arr))
	seen := make(map[int]struct{})

	for _, val := range arr {
		if _, ok := seen[val]; !ok {
			seen[val] = struct{}{}
			ans = append(ans, val)
		}
	}
	return ans
}

func intersection(a []int, b []int) []int {
	ans := []int{}

	if len(a) == 0 || len(b) == 0 {
		return ans
	}

	seen := make(map[int]struct{})
	for _, v := range a {
		seen[v] = struct{}{}
	}

	added := make(map[int]struct{})

	for _, val := range b {
		if _, ok := seen[val]; ok {
			if _, dup := added[val]; !dup {
				ans = append(ans, val)
				added[val] = struct{}{}
			}
		}
	}

	return ans
}

func main() {
	tests := [][]int{
		{1, 2, 3},
		{2, 3},
		{2, 3},
		{4, 5},
		{},
	}

	for i := 0; i+1 < len(tests); i++ {
		fmt.Println(intersection(tests[i], tests[i+1]))
	}
}
