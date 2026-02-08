# Day 26 - Daily Temperatures

Problem Statement

Given an array temperatures, where temperatures[i] represents the temperature on day i, return an array such that:

For each day, the value is the number of days you would have to wait until a warmer temperature occurs.

If no future day exists with a warmer temperature, use 0 for that position.

Input

temperatures: array of integers

Output

An array of integers representing days until a warmer temperature

Example
Input:  [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

What This Problem Is Testing

Monotonic stack pattern

Deferred resolution of state

Index-based reasoning

Cloud Analogy

Predicting how long until load exceeds current capacity.