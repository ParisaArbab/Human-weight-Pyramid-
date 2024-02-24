# Human-weight-Pyramid-
This Python program aims to identify if there exists a pair of numbers within a randomly generated list that sums up to a target value specified by the user. The program combines the use of binary search with the generation of random numbers to efficiently solve the problem. Here's a brief overview:

User Input: The program starts by asking the user for the length of the list and the target sum they're interested in finding.

Generate Random List: It then creates a list of random integers (between 0 and 100) of the specified length.

Binary Search for Sum: The has_sum_in_list function takes the sorted list and the target sum as inputs. It iterates through each number in the list, using binary search to find if there exists another number in the list that, when added to the current number, equals the target sum.

Binary Search Mechanism: For each number in the list, the function calculates its complement (the difference between the target sum and the current number). It then performs a binary search on the remaining elements of the list to find this complement.
If a pair is found, it returns the numbers; otherwise, it continues the search. If no such pair exists in the list, the function returns None.
Output: The main function then checks if the has_sum_in_list function has found a pair of numbers that sum up to the target. If so, it prints the numbers; otherwise, it informs the user that no such pair exists.

Efficiency: The sorting of the list takes O(n log n) time, and the subsequent binary search for each element (in the worst case, for all elements) also takes O(n log n) time, making the overall approach efficient for this problem.

This program effectively demonstrates an application of binary search in solving the two-sum problem, showcasing an efficient way to find if two numbers in a list sum up to a given target.
