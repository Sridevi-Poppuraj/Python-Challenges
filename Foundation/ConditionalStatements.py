# Concept: Control flow branching, complex conditions, nested logic optimization.
# Challenge: Build a single-expression inline ternary check that accepts an integer score (0–100) and returns 'A' (90+), 'B' (80-89), 'C' (70-79), 'D' (60-69), or 'F' (<60). The solution must be a single line containing only nested ternary expressions without using if/elif/else blocks or dictionary lookups.

score = 87
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F" 
print (grade)
