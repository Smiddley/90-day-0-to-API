// ### Problem Statement

// Given a string s containing only the characters ()[]{}, determine if the input string is valid.

// A string is valid if:
// - Open brackets are closed by the same type

// - Open brackets are closed in the correct order

// - Every closing bracket has a corresponding open bracket

// ### Input

// s: string

// ### Output

// true or false

// ### Example
// ```
// Input:  "()[]{}"
// Output: true

// Input:  "(]"
// Output: false
// ```

// ### Concept

// Stack (LIFO)

// State tracking

// ### Cloud Analogy

// Nested configs / firewall rules must unwind in the correct order.

package main

func isValid(s string) bool {
	pairs := map[rune]rune{"(": ")", "{":"}","[":"]"}
	fmt.PrintLn(pairs)
	// for _, ch := range s{

	// }
}

func main(){
	isValid("test")
}