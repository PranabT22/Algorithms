1. Basic Bubble Sort Implementation

You are given an unsorted array of integers.

Write a program to sort the array in ascending order using Bubble Sort.

Requirements:

Do not use built-in sort functions

Perform pairwise swaps of adjacent elements

Print the array after sorting

2. Bubble Sort in Descending Order

Given an array of integers, sort it in descending order using Bubble Sort.

Think About:

How comparison logic changes

Whether the number of passes changes

3. Count the Number of Swaps

Given an array, sort it using Bubble Sort and return:

The sorted array

The total number of swaps performed

This helps understand how Bubble Sort behaves on different inputs.

4. Check If Array Is Already Sorted

You are given an array.

Before sorting, determine whether the array is already sorted.

If it is, return the array immediately without performing unnecessary passes.

5. Bubble Sort with Step-by-Step Output

Given an array, apply Bubble Sort and print the array after every full pass.

Goal:

Understand how elements “bubble” to their correct positions

🟡 MEDIUM (6–14): Optimization & Variations
6. Optimized Bubble Sort Using Early Termination

Modify Bubble Sort so that it stops early if no swaps occur during a pass.

Task:

Implement this optimization

Compare number of passes with standard Bubble Sort

7. Sorting Strings Using Bubble Sort

You are given an array of strings.

Sort them in lexicographical order using Bubble Sort.

Consider:

Case sensitivity

Comparing strings correctly

8. Sorting Custom Objects

You are given a list of students, each having:

name

marks

Sort the students by marks in ascending order using Bubble Sort.

If two students have the same marks, keep their relative order unchanged.

9. Bubble Sort for Nearly Sorted Arrays

An array is almost sorted, with only a few elements out of place.

Use Bubble Sort to efficiently sort the array and analyze why it performs well here.

10. Largest Element After Each Pass

Given an array, show which element reaches its final position after each pass of Bubble Sort.

Goal:

Demonstrate understanding of Bubble Sort invariants

11. Find K Largest Elements Using Bubble Sort

Without fully sorting the array, find the k largest elements using Bubble Sort logic.

Hint:

Observe what happens after k passes

12. Sort Based on Absolute Difference

Given an array of integers and a value x, sort the array based on the absolute difference from x using Bubble Sort.

If two values have the same difference, maintain their original order.

13. Bubble Sort with Index Tracking

While sorting an array, also maintain an array of original indices.

After sorting, output:

Sorted values

Their original indices

14. Partial Sorting with Bubble Sort

Given an array and an integer k, perform exactly k passes of Bubble Sort and output the resulting array.

Think:

What part of the array becomes sorted?

🔴 TOP INTERVIEW LEVEL (15–30): TikTok / Microsoft / AWS Style

These questions test algorithmic judgment, trade-offs, and understanding of Bubble Sort limitations, not just implementation.

15. Detect If Bubble Sort Is a Bad Choice

You are given an array and system constraints (input size, memory limits).

Write a program that:

Uses Bubble Sort

Detects if input size exceeds safe limits

Returns a warning message if Bubble Sort is inefficient

(Tests understanding of time complexity)

16. Compare Bubble Sort vs Built-In Sort

Given multiple arrays of varying sizes:

Sort them using Bubble Sort

Sort them using the language’s built-in sort

Measure and compare execution time

Explain when Bubble Sort becomes impractical.

17. Minimum Swaps to Sort an Array

Using Bubble Sort logic, calculate the minimum number of swaps required to sort an array.

Important:

Do not perform unnecessary swaps

Return only the count

(Microsoft-style reasoning question)

18. Stability Verification

You are given records with:

id

value

Sort them using Bubble Sort by value.

Verify through code that Bubble Sort preserves the relative order of records with equal values.

19. Sorting a Streaming Input

You receive numbers one at a time.

After each insertion, maintain the array in sorted order using Bubble Sort-style adjacent swaps only.

(AWS streaming-data style question)

20. Bubble Sort for Linked Lists

Implement Bubble Sort on a singly linked list.

Restrictions:

Do not convert the list to an array

Swap nodes, not values

21. Worst-Case Input Generator

Write a program that generates an input array of size n that forces Bubble Sort to take maximum time.

Explain why this input is worst-case.

22. Hybrid Sorting Strategy

Given an array:

Use Bubble Sort if the array is nearly sorted

Otherwise switch to another sorting technique

Implement logic to detect which case applies.

(TikTok-style optimization question)

23. Bubble Sort in Memory-Constrained Systems

You are working on an embedded system with:

Very limited memory

No recursion allowed

Implement Bubble Sort and justify why it fits these constraints.

24. Sorting with Swap Cost

Each swap has a cost.

Modify Bubble Sort to minimize total swap cost, even if it means performing more comparisons.

(Microsoft-level thinking problem)

25. Parallel Bubble Sort Analysis

Assume you have multiple processors.

Analyze whether Bubble Sort can be parallelized and implement a partial parallel approach if possible.

26. Bubble Sort Visualization Engine

Write a program that outputs every swap operation so that a UI can visualize the sorting process.

Ensure the output format is structured and consistent.

27. Detect Sorted Prefix Length

After every pass of Bubble Sort, detect how much of the array is already sorted and skip unnecessary comparisons.

28. Sorting with Restricted Swaps

You are allowed to swap elements only if their difference is ≤ K.

Determine whether Bubble Sort can still fully sort the array.

(AWS-style constraints problem)

29. Reverse Engineering Bubble Sort Output

You are given the intermediate array states after each pass of Bubble Sort.

Determine whether these states are valid and reconstruct the original array if possible.

30. Prove Bubble Sort Correctness via Code

Write a program that:

Demonstrates invariants of Bubble Sort

Shows why it always produces a sorted array

Outputs reasoning steps along with execution

(Advanced interview + theory blend)
