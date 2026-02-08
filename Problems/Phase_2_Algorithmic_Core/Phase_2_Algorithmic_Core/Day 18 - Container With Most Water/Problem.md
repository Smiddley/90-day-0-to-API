# Day 18 - Container With Most Water

Problem Statement

You are given an array height, where height[i] represents the height of a vertical line drawn at position i.

Choose two lines that together with the x-axis form a container such that the container holds the maximum amount of water.

Return the maximum area of water the container can store.

Input

height: array of non-negative integers

2 ≤ len(height) ≤ 10⁵

Output

An integer representing the maximum area

Rules & Constraints

The container cannot be tilted

Area is calculated as:

min(height[left], height[right]) × (right - left)


Time complexity target: O(n)

Example
Input:  [1,8,6,2,5,4,8,3,7]
Output: 49

What This Problem Is Testing

Two-pointer optimization

Discarding impossible states intelligently

Cloud Analogy

Maximizing throughput between two rate-limited network nodes.
