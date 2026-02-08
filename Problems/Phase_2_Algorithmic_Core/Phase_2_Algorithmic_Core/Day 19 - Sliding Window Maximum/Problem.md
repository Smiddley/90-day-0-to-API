# Day 19 - Sliding Window Maximum

Day 19 — Sliding Window Maximum
Problem Statement

Given an array of integers nums and an integer k, return an array of the maximum value in every contiguous subarray of size k.

Input

nums: array of integers

k: window size

1 ≤ k ≤ len(nums)

Output

Array of integers representing the maximum of each window

Example
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

What This Problem Is Testing

Deques / monotonic queues

Efficient window eviction logic

Avoiding redundant comparisons

Cloud Analogy

Rolling max CPU utilization over a fixed observation window.