//Check if a string of parentheses is valid (open/close pairs match)

package main

import "fmt"

func CheckValid(s string) bool {
	if len(s) == 0 {
		return true
	}
	count := 0

	for _, char := range s {
		if char == '(' {
			count++
		} else if char == ')' {
			count--
		}

		if count < 0 {
			return false
		}
	}
	if count != 0 {
		return false
	}

	return true
}

func main() {
	testCase := []string{"()()()()()(())((()))",
		")(((())))(",
		"",
		"(((())))("}

	for _, test := range testCase {
		fmt.Println(CheckValid(test))
	}
}
