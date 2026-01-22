"""
Write a function that takes an array of integers and returns the sum of all numbers.

Example:

`Input: [1, 2, 3, 4, 5]
Output: 15

Input: []
Output: 0`


Constraints:

Array length: 0 ≤ n ≤ 1000

Integers can be positive, negative, or zero
"""

package main
import "fmt"

func SumInts(arr []int) int{
	total := 0
	for _, value := range arr {
		total = total + value
	}
	return total
}

func main(){
	arr := []int{1,2,3,4,5}
	total := SumInts(arr)
	fmt.Println(total)
}
