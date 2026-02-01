# Day 16 - Minimum Window Substring

Problem Statement

Given two strings s and t, return the smallest substring of s that contains all characters of t, including duplicates.

If no such substring exists, return an empty string "".

Input

s: source string

t: target string

1 ≤ len(s), len(t) ≤ 10⁵

Strings consist of uppercase and lowercase English letters

Output

The minimum-length substring of s that contains all characters in t

Rules & Constraints

All characters in t must appear in the window

Character frequency matters

If t = "AABC", the window must contain two A’s

If multiple valid windows exist, return any one

Time complexity target: O(n)

Example
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

What This Problem Is Testing

Sliding window mechanics

Frequency maps

Window expansion vs contraction logic

Cloud Analogy

Think of:

A log stream (s)

A required set of security events (t)

You want the shortest log segment that proves compliance