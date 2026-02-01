# Day 17 - 3Sum

Day 17 — 3Sum
Problem Statement

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:

i ≠ j ≠ k

nums[i] + nums[j] + nums[k] = 0

The solution set must not contain duplicate triplets.

Input

nums: array of integers

3 ≤ len(nums) ≤ 3000

-10⁵ ≤ nums[i] ≤ 10⁵

Output

A list of unique triplets that sum to zero

Rules & Constraints

Triplets must be unique, regardless of order

Output order does not matter

Time complexity target: O(n²)

Example
Input:  [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

What This Problem Is Testing

Sorting as a preprocessing step

Two-pointer technique

Duplicate avoidance strategies

Cloud Analogy

Correlating three independent metrics that together indicate a fault condition.