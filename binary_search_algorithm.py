🟢 EASY (1–5): Build Binary Search Intuition
1. Classic Binary Search with Edge Handling

You are given a sorted array of integers arr of size n sorted in non-decreasing order and an integer target.

Your task is to implement binary search without using any built-in search functions.

Return:

The index of target if it exists

-1 if it does not exist

Important considerations:

The array can be empty

n can be as small as 0 or as large as 10⁵

Your solution must run in O(log n) time

2. First Occurrence in a Large Dataset

You are given a very large sorted array that may contain millions of duplicate values.

Given a value target, find the first index at which target appears.

Constraints & Challenges:

You must not scan linearly

If target does not exist, return -1

Think carefully about how binary search boundaries change when duplicates exist

3. Last Occurrence with Boundary Safety

Given a sorted array with duplicate values, find the last occurrence of a target element.

Special Cases to Consider:

Target occurs only once

Target occurs at the end of the array

Target does not exist at all

4. Counting Frequency Efficiently

Given a sorted array arr and a number x, determine how many times x occurs.

Rules:

Your algorithm must run in O(log n)

You may only use binary search logic

Think about how first and last occurrence can be combined

5. Search Insert Position in a Growing System

You are building a system that maintains a sorted list of numbers.

Given a sorted array and a value x:

If x exists, return its index

Otherwise, return the index where x should be inserted to keep the array sorted

Edge Cases:

Insert at beginning

Insert at end

Insert between duplicates

🟡 MEDIUM (6–10): Reasoning + Variants
6. Floor and Ceil in a Sensor System

A sensor continuously generates sorted readings.

Given a sorted array and a value x, find:

Floor(x): largest element ≤ x

Ceil(x): smallest element ≥ x

If floor or ceil does not exist, return -1 for that value.

Think About:

What happens when x is smaller than all elements?

What happens when x is larger than all elements?

7. Searching in a Rotated Database

A database was originally sorted but rotated at an unknown pivot.

Given this rotated sorted array and a target value, find the index of the target.

Key Challenges:

Identify which half is sorted

Decide where the target can exist

Ensure O(log n) time

8. Minimum Value in a Rotated System

Given a rotated sorted array with no duplicate elements, find the minimum element.

You must:

Use binary search

Avoid scanning the array

Correctly handle cases where the array is not rotated

9. Finding a Peak in Performance Metrics

You are analyzing performance metrics represented as an array.

A peak element is defined as an element strictly greater than its immediate neighbors.

Find any one peak element using binary search.

Notes:

The array may contain multiple peaks

Edge elements can also be peaks

You must achieve O(log n) time

10. Square Root Without Math Libraries

Given a non-negative integer n, compute the integer square root of n.

That is, find the largest integer x such that x * x ≤ n.

Restrictions:

Do not use built-in square root functions

Handle large values up to 10⁹

Avoid integer overflow

🔵 HARD (11–14): Binary Search Patterns
11. Single Element Among Pairs

You are given a sorted array where:

Every element appears exactly twice

Except one element that appears only once

Find the single element in O(log n) time and O(1) space.

Hint:
Observe index parity before and after the unique element.

12. Searching in a Nearly Sorted Array

In a nearly sorted array, every element may be misplaced by at most one position from its correct sorted location.

Find the index of a target element using binary search.

Key Thinking:

Standard binary search assumptions do not fully apply

Check neighboring indices carefully

13. Allocate Minimum Pages (Binary Search on Answer)

You are given n books, each with a certain number of pages, and m students.

Books must be allocated:

In contiguous order

Each student gets at least one book

Minimize the maximum number of pages assigned to any student.

Important:

Use binary search on the answer

Understand feasibility checking

14. Aggressive Cows Problem

You are given positions of stalls along a line and k cows.

Place the cows such that the minimum distance between any two cows is maximized.

Challenges:

Sort first

Binary search on distance

Greedy placement check

🔴 TOP INTERVIEW (15–20): Microsoft / AWS / TikTok Level
15. Median of Two Sorted Arrays

You are given two sorted arrays of possibly different sizes.

Without merging them:

Find the median

Achieve O(log(min(n, m))) time

Think About:

Partitioning logic

Even vs odd total length

Boundary conditions

16. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where:

Rows are sorted left to right

Columns are sorted top to bottom

Find the kth smallest element.

Restrictions:

Do not flatten the matrix

Optimize for large n

17. Minimum Days to Make Bouquets

You are given an array where each element represents the day a flower blooms.

To make one bouquet:

You need k adjacent flowers that have bloomed

Find the minimum day to make m bouquets.

Edge Cases:

Impossible scenarios

Very large bloom days

Adjacency constraints

18. Split Array Largest Sum

Given an array and an integer k, split the array into k non-empty contiguous subarrays.

Minimize the largest subarray sum.

Focus On:

Binary search over possible sums

Greedy validation

19. Shipping Packages Within D Days

Packages must be shipped in order.

Each day:

You load packages until capacity is reached

Find the minimum ship capacity to ship all packages in D days.

Think About:

Lower and upper bounds

Feasibility checks

20. Smallest Divisor Under Threshold

Given an array of integers and a threshold value.

Find the smallest divisor such that:

sum(ceil(arr[i] / divisor)) ≤ threshold


Why this is hard:

Binary search on answer

Handling large numbers

Optimization required
