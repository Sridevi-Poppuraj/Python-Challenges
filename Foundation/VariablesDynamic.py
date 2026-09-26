# Concept: Dynamic binding, variable assignment, type inspection, and reference swapping.
# Challenge: Given two variables a = [1, 2, 3] and b = "Python", swap their values without using a temporary variable, without using tuple unpacking a, b = b, a, and without hardcoding the values. Verify their memory IDs change using id().

# variable assignment
a = [1, 2, 3]
b = "Python"

values = [a, b]
print("inputs :", values)
reverse = values[::-1]

a = reverse[0]
b = reverse[1]

print(a, b)
