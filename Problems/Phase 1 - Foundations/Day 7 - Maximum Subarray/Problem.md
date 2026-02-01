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