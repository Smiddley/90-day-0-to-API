# Day 20 - Product of Array Except Self

Problem Statement

Given an array nums, return an array output such that:

output[i] = product of all elements of nums except nums[i]


You must solve this without using division.

Input

nums: array of integers

2 ≤ len(nums) ≤ 10⁵

-30 ≤ nums[i] ≤ 30

Output

An array of integers

Rules & Constraints

Do not use division

Time complexity: O(n)

Space complexity: O(1) extra space (excluding output)

Example
Input:  [1,2,3,4]
Output: [24,12,8,6]

What This Problem Is Testing

Prefix and suffix products

Space optimization

Handling zero values correctly

Cloud Analogy

Computing impact of removing one node from a distributed system.