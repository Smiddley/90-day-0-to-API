# Day 15 - Best Time to Buy and Sell Stock II

Problem Statement

You are given an array of integers prices, where prices[i] represents the price of a stock on day i.

You may complete as many transactions as you like, but:

You may only hold one share of the stock at a time

You must sell the stock before buying again

Your goal is to calculate the maximum profit you can achieve.

Return the maximum possible profit.

Input

prices: an array of integers

1 ≤ len(prices) ≤ 10⁵

0 ≤ prices[i] ≤ 10⁴

Output

An integer representing the maximum profit achievable

Rules & Constraints

You may buy and sell on the same day only if you sell before you buy again (effectively a no-op)

You may not hold multiple shares

If no profitable transactions exist, return 0

Time complexity target: O(n)

Space complexity target: O(1)

Examples
Example 1
Input:  [7,1,5,3,6,4]
Output: 7
Explanation:
Buy at 1, sell at 5 (profit = 4)
Buy at 3, sell at 6 (profit = 3)
Total profit = 7