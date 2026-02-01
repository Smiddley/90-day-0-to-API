"""
Problem Statement
Given an array of integers nums, find the maximum possible sum of a non-empty contiguous subarray.
A contiguous subarray is a sequence of elements that appear consecutively in the original array.
You must return the maximum sum, not the subarray itself.

Input:
    nums: an array (slice / list) of integers
    Length: 1 ≤ len(nums) ≤ 10⁵
    Values: -10⁴ ≤ nums[i] ≤ 10⁴

Output:
An integer representing the largest possible sum of any contiguous subarray.

Constraints & Rules
    The subarray must be contiguous
    You may not skip elements.
    The subarray must contain at least one element
    Returning 0 is not allowed unless 0 is the maximum achievable sum.
    The array may contain all negative numbers

Time complexity target: O(n)
Space complexity target: O(1) (excluding input)

Example:
Input:  [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation:
The contiguous subarray [4, -1, 2, 1] has the largest sum = 6


Notes:
We could brute force calc all possible sublist sums, but that does not meet complexity target.
Still useful to get expected result, had an example not been provided. 
With knowing the expected result, we can probably engineer a faster algorhythm

We only need to track 2 sums; max seen so far, current eval. 
If current eval is greater than max seen, max = current.

every new value we see we have to decide whether to extend the current summation ("window") or start a new one.
But when to do which?
Looking at the edge cases can be illuminating.
If all values are positive, then clearly the best answer is to sum the entire list.
Translating that to indiviual value decision point means either:
    because val is positive, extend window
    because total so far is positive, extend window.

If all valuse are negative, then clearly the best answer is to get the single max value
Translating that to indiviual value decision point means either:
    because val is negatigve, start new window
    because total so far negative, start new window

We see from the example that clearly adding a negative number can still lead to the max possible sublist.
Therefore the logic must be relative to the current sum, not the individual values.

Therefore

max = array_values[0]
for value in array_values
    current = current + value
    if current > max; max = current
    if current < 0; current = 0
"""
def max_subarray(test: list[int]) -> int :
    current = 0
    max_val = test[0]

    for val in test:
        current = max(val, current + val)
        max_val = max(max_val, current)

    return max_val

if __name__=="__main__":
    tests = [
        [-1, -2, -3],
        [1, 2, 3],
        [-2, 1, -3, 4,-1, 2, 1, -5, 4],
        [-2, 1, -3, 4,-1, 2, 1, -5, 4, 6]
    ]
    for test in tests:
        print(max_subarray(test))