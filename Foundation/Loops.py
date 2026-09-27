# Concept: Iteration protocols, nested loops, loop control mechanics.
# Challenge: Given two lists of unequal length, write a for loop using enumerate and zip (without importing itertools) that pairs elements up to the shorter list's length, but prints both the pair index and the remaining un-paired elements of the longer list after the loop finishes.

list1 = [10, 20, 30, 40, 50]
list2 = ["a", "b", "c"]


for index, (x, y) in enumerate(zip(list1, list2)):
    print(f"Pair {index}: ({x}, {y})")


longer = list1 if len(list1) > len(list2) else list2
shorter_len = min(len(list1), len(list2))
leftover = longer[shorter_len:]
