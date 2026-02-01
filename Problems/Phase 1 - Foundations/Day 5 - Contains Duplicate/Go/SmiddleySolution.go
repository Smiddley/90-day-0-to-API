// Check if an array contains any duplicates.
// no built in Counter module

package main

import (
	"cmp"
	"fmt"
	"slices"
)

func hasDupesSet[T cmp.Ordered](arr []T) bool {
	temp := make([]T, len(arr))
	copy(temp, arr)
	slices.Sort(temp)
	return len(slices.Compact(temp)) != len(arr)
}

func hasDupesDict[T comparable](arr []T) bool {
	seen := make(map[T]int)
	for _, char := range arr {
		if _, exists := seen[char]; exists {
			return true
		}
		//prepped for extension into "How many of each dupes?"
		seen[char] = seen[char] + 1
	}
	return false
}

func main() {
	testsInt := [][]int{
		{1, 2, 3, 4, 5, 6},
		{1, 2, 2, 3}}
	testString := [][]string{
		{"a", "b", "c"},
		{"a", "a", "b"},
		{""},
	}

	for _, test := range testsInt {
		fmt.Println(hasDupesSet(test))
		fmt.Println(hasDupesDict(test))
	}
	for _, test := range testString {
		fmt.Println(hasDupesSet(test))
		fmt.Println(hasDupesDict(test))
	}
}
